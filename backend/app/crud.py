from datetime import datetime
from sqlalchemy.orm import Session
from app import models, schemas
from sqlalchemy import text


def get_sla_chamados(db: Session):
    """
    Retorna todos os registros da view analítica de SLA.
    """
    return db.query(models.VwSlaChamado).all()


def create_chamado(db: Session, chamado: schemas.ChamadoCreate):
    """
    Cria um novo chamado no banco de dados.

    Observação:
        O campo criado_em é preenchido no momento da criação.
        Triggers do banco podem complementar regras de histórico.
    """
    novo_chamado = models.Chamado(
        titulo=chamado.titulo,
        descricao=chamado.descricao,
        usuario_id=chamado.usuario_id,
        tecnico_id=chamado.tecnico_id,
        categoria_id=chamado.categoria_id,
        subcategoria_id=chamado.subcategoria_id,
        prioridade_id=chamado.prioridade_id,
        status_id=chamado.status_id,
        criado_em=datetime.now()
    )
    db.add(novo_chamado)
    db.commit()
    db.refresh(novo_chamado)
    return novo_chamado


def update_chamado(db: Session, chamado_id: int, chamado_data: schemas.ChamadoUpdate):
    """
    Atualiza parcialmente os dados de um chamado existente.

    Args:
        db:
            Sessão ativa do banco.
        chamado_id:
            Identificador do chamado a ser atualizado.
        chamado_data:
            Dados parciais recebidos da camada de API.

    Returns:
        O chamado atualizado, ou None se não encontrado.
    """
    chamado = db.query(models.Chamado).filter(models.Chamado.id == chamado_id).first()

    if not chamado:
        return None

    dados_update = chamado_data.model_dump(exclude_unset=True)

    for campo, valor in dados_update.items():
        setattr(chamado, campo, valor)

    chamado.atualizado_em = datetime.now()

    db.commit()
    db.refresh(chamado)
    return chamado


def update_chamado_status(
    db: Session,
    chamado_id: int,
    status_data: schemas.ChamadoStatusUpdate
):
    """
    Atualiza exclusivamente o status operacional de um chamado.

    Regras:
        - altera o status_id
        - opcionalmente atualiza o tecnico_id responsável
        - atualiza o campo atualizado_em
        - caso o status mude, o trigger do banco deve registrar o histórico

    Args:
        db:
            Sessão ativa do banco.
        chamado_id:
            Identificador do chamado.
        status_data:
            Payload contendo novo status e, opcionalmente, técnico responsável.

    Returns:
        O chamado atualizado, ou None se não encontrado.
    """
    chamado = db.query(models.Chamado).filter(models.Chamado.id == chamado_id).first()

    if not chamado:
        return None

    chamado.status_id = status_data.status_id

    if status_data.tecnico_id is not None:
        chamado.tecnico_id = status_data.tecnico_id

    chamado.atualizado_em = datetime.now()

    db.commit()
    db.refresh(chamado)
    return chamado


def _build_chamados_filters(status_id=None, categoria_id=None, tecnico_id=None):
    """
    Monta dinamicamente cláusulas SQL e parâmetros para filtros sobre a tabela
    de chamados.

    Args:
        status_id:
            Identificador do status do chamado.
        categoria_id:
            Identificador da categoria do chamado.
        tecnico_id:
            Identificador do técnico responsável.

    Returns:
        tuple[str, dict]:
            - cláusula SQL pronta para ser concatenada ao WHERE
            - dicionário de parâmetros para bind seguro
    """
    filtros = []
    params = {}

    if status_id is not None:
        filtros.append("c.status_id = :status_id")
        params["status_id"] = status_id

    if categoria_id is not None:
        filtros.append("c.categoria_id = :categoria_id")
        params["categoria_id"] = categoria_id

    if tecnico_id is not None:
        filtros.append("c.tecnico_id = :tecnico_id")
        params["tecnico_id"] = tecnico_id

    where_clause = ""
    if filtros:
        where_clause = " WHERE " + " AND ".join(filtros)

    return where_clause, params


def get_dashboard_detalhado(
    db: Session,
    status_id: int | None = None,
    categoria_id: int | None = None,
    tecnico_id: int | None = None
):
    """
    Retorna dados detalhados do dashboard com suporte a filtros operacionais.

    Filtros suportados:
        - status_id
        - categoria_id
        - tecnico_id

    Blocos retornados:
        - chamados_por_categoria
        - sla_por_categoria
        - ranking_tecnicos

    Estratégia:
        - usa a tabela 'chamados' como base de filtro
        - cruza com categorias, usuários e a view 'vw_sla_chamados'
        - mantém COALESCE para evitar quebra analítica por dados incompletos

    Args:
        db:
            Sessão ativa do banco.
        status_id:
            Filtro opcional por status.
        categoria_id:
            Filtro opcional por categoria.
        tecnico_id:
            Filtro opcional por técnico responsável.

    Returns:
        dict:
            Estrutura compatível com DashboardDetalhadoResponse.
    """
    where_clause, params = _build_chamados_filters(
        status_id=status_id,
        categoria_id=categoria_id,
        tecnico_id=tecnico_id
    )

    # ---------------------------------------------------------------------
    # Bloco 1: Volume de chamados por categoria
    # ---------------------------------------------------------------------
    query_categorias = text(f"""
        SELECT
            COALESCE(cat.nome, 'Não Informada') AS categoria,
            COUNT(*) AS total_chamados
        FROM chamados c
        LEFT JOIN categorias cat ON c.categoria_id = cat.id
        {where_clause}
        GROUP BY COALESCE(cat.nome, 'Não Informada')
        ORDER BY total_chamados DESC, categoria ASC
    """)

    categorias_result = db.execute(query_categorias, params).mappings().all()

    chamados_por_categoria = [
        {
            "categoria": row["categoria"],
            "total_chamados": int(row["total_chamados"])
        }
        for row in categorias_result
    ]

    # ---------------------------------------------------------------------
    # Bloco 2: SLA por categoria
    # ---------------------------------------------------------------------
    query_sla_categoria = text(f"""
        SELECT
            COALESCE(v.categoria, 'Não Informada') AS categoria,
            COALESCE(
                ROUND(
                    SUM(CASE WHEN v.status_sla = 'Dentro do SLA' THEN 1 ELSE 0 END) * 100.0
                    / NULLIF(COUNT(*), 0),
                    2
                ),
                0
            ) AS percentual_dentro_sla,
            COALESCE(
                ROUND(
                    SUM(CASE WHEN v.status_sla = 'Fora do SLA' THEN 1 ELSE 0 END) * 100.0
                    / NULLIF(COUNT(*), 0),
                    2
                ),
                0
            ) AS percentual_fora_sla
        FROM vw_sla_chamados v
        INNER JOIN chamados c ON c.id = v.chamado_id
        {where_clause}
        GROUP BY COALESCE(v.categoria, 'Não Informada')
        ORDER BY categoria ASC
    """)

    sla_result = db.execute(query_sla_categoria, params).mappings().all()

    sla_por_categoria = [
        {
            "categoria": row["categoria"],
            "percentual_dentro_sla": float(row["percentual_dentro_sla"]),
            "percentual_fora_sla": float(row["percentual_fora_sla"]),
        }
        for row in sla_result
    ]

    # ---------------------------------------------------------------------
    # Bloco 3: Ranking de técnicos por volume de chamados atribuídos
    # ---------------------------------------------------------------------
    query_ranking_tecnicos = text(f"""
        SELECT
            u.id AS tecnico_id,
            COALESCE(u.nome, 'Técnico não identificado') AS tecnico_nome,
            COUNT(c.id) AS total_chamados
        FROM chamados c
        INNER JOIN usuarios u ON c.tecnico_id = u.id
        {where_clause}
        GROUP BY u.id, COALESCE(u.nome, 'Técnico não identificado')
        ORDER BY total_chamados DESC, tecnico_nome ASC
    """)

    ranking_result = db.execute(query_ranking_tecnicos, params).mappings().all()

    ranking_tecnicos = [
        {
            "tecnico_id": int(row["tecnico_id"]),
            "tecnico_nome": row["tecnico_nome"],
            "total_chamados": int(row["total_chamados"]),
        }
        for row in ranking_result
    ]

    return {
        "chamados_por_categoria": chamados_por_categoria,
        "sla_por_categoria": sla_por_categoria,
        "ranking_tecnicos": ranking_tecnicos,
    }