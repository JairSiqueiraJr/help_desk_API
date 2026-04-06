from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy import text
from app import models, schemas


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


def get_dashboard_resumo(db: Session):
    """
    Retorna o resumo analítico principal do dashboard.

    Estratégia:
        - usa a tabela 'chamados' para contagem operacional por status
        - usa a view 'vw_sla_chamados' para indicadores de SLA
        - calcula tempo médio apenas sobre chamados concluídos
          (status Resolvido ou Fechado), evitando distorção com chamados ainda abertos

    Returns:
        dict:
            Estrutura compatível com o schema DashboardResumoResponse.
    """
    query = text("""
        SELECT
            (SELECT COUNT(*) FROM chamados) AS total_chamados,

            (
                SELECT COUNT(*)
                FROM chamados
                WHERE status_id = 1
            ) AS chamados_abertos,

            (
                SELECT COUNT(*)
                FROM chamados
                WHERE status_id = 2
            ) AS chamados_em_atendimento,

            (
                SELECT COUNT(*)
                FROM chamados
                WHERE status_id IN (3, 4)
            ) AS chamados_fechados,

            (
                SELECT COALESCE(
                    ROUND(
                        SUM(CASE WHEN status_sla = 'Dentro do SLA' THEN 1 ELSE 0 END) * 100.0
                        / NULLIF(COUNT(*), 0),
                        2
                    ),
                    0
                )
                FROM vw_sla_chamados
            ) AS percentual_dentro_sla,

            (
                SELECT COALESCE(
                    ROUND(
                        SUM(CASE WHEN status_sla = 'Fora do SLA' THEN 1 ELSE 0 END) * 100.0
                        / NULLIF(COUNT(*), 0),
                        2
                    ),
                    0
                )
                FROM vw_sla_chamados
            ) AS percentual_fora_sla,

            (
                SELECT COALESCE(
                    ROUND(AVG(v.tempo_real_horas), 2),
                    0
                )
                FROM vw_sla_chamados v
                INNER JOIN chamados c ON c.id = v.chamado_id
                WHERE c.status_id IN (3, 4)
            ) AS tempo_medio_horas
    """)

    resultado = db.execute(query).mappings().first()

    return {
        "total_chamados": int(resultado["total_chamados"] or 0),
        "chamados_abertos": int(resultado["chamados_abertos"] or 0),
        "chamados_em_atendimento": int(resultado["chamados_em_atendimento"] or 0),
        "chamados_fechados": int(resultado["chamados_fechados"] or 0),
        "percentual_dentro_sla": float(resultado["percentual_dentro_sla"] or 0),
        "percentual_fora_sla": float(resultado["percentual_fora_sla"] or 0),
        "tempo_medio_horas": float(resultado["tempo_medio_horas"] or 0),
    }