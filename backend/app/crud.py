"""
Módulo de operações CRUD relacionadas a chamados (tickets) no banco de dados.

Centraliza as funções de acesso a dados para criação, consulta e manipulação
de chamados e suas views associadas.
"""

from sqlalchemy.orm import Session
from app import models, schemas
from datetime import datetime


def get_sla_chamados(db: Session) -> list[models.VwSlaChamado]:
    """
    Retorna todos os registros da view de SLA de chamados.

    Consulta a view `VwSlaChamado`, que agrega informações de chamados
    com seus respectivos dados de SLA (prazo, status de conformidade, etc.).

    Args:
        db (Session): Sessão ativa do SQLAlchemy para interação com o banco de dados.

    Returns:
        list[VwSlaChamado]: Lista com todos os registros da view. Retorna
        uma lista vazia se não houver registros.

    Example:
        >>> sla_data = get_sla_chamados(db)
        >>> for registro in sla_data:
        ...     print(registro.chamado_id, registro.status_sla)
    """
    return db.query(models.VwSlaChamado).all()


def create_chamado(db: Session, chamado: schemas.ChamadoCreate) -> models.Chamado:
    """
    Cria e persiste um novo chamado no banco de dados.

    Instancia um objeto `Chamado` a partir dos dados validados pelo schema
    Pydantic, define o timestamp de criação e o persiste via SQLAlchemy.

    Args:
        db (Session): Sessão ativa do SQLAlchemy para interação com o banco de dados.
        chamado (schemas.ChamadoCreate): Schema Pydantic com os dados do novo chamado.
            Todos os campos obrigatórios do schema devem estar preenchidos.

    Returns:
        models.Chamado: Instância do chamado recém-criado, atualizada com o
        `id` gerado pelo banco de dados e os demais valores persistidos.

    Raises:
        sqlalchemy.exc.IntegrityError: Se houver violação de chave estrangeira
            (ex: `usuario_id`, `tecnico_id` ou `categoria_id` inexistentes).
        sqlalchemy.exc.SQLAlchemyError: Em caso de falha genérica na transação.

    Example:
        >>> payload = schemas.ChamadoCreate(
        ...     titulo="Sem acesso ao sistema",
        ...     descricao="Usuário não consegue logar desde ontem.",
        ...     usuario_id=1,
        ...     tecnico_id=4,
        ...     categoria_id=2,
        ...     subcategoria_id=5,
        ...     prioridade_id=2,
        ...     status_id=1,
        ... )
        >>> novo = create_chamado(db, payload)
        >>> print(novo.id)  # ID gerado pelo banco
    """
    # Instancia o modelo ORM com os dados recebidos do schema
    novo_chamado = models.Chamado(
        titulo=chamado.titulo,
        descricao=chamado.descricao,
        usuario_id=chamado.usuario_id,
        tecnico_id=chamado.tecnico_id,
        categoria_id=chamado.categoria_id,
        subcategoria_id=chamado.subcategoria_id,
        prioridade_id=chamado.prioridade_id,
        status_id=chamado.status_id,
        criado_em=datetime.now()  # Timestamp definido na camada da aplicação
    )

    db.add(novo_chamado)      # Adiciona o objeto à sessão (ainda não persiste)
    db.commit()               # Persiste a transação no banco de dados
    db.refresh(novo_chamado)  # Sincroniza a instância com o estado retornado pelo banco

    return novo_chamado



def update_chamado(
    db: Session,
    chamado_id: int,
    chamado_data: schemas.ChamadoUpdate
) -> models.Chamado | None:
    """
    Atualiza parcialmente os dados de um chamado existente no banco de dados.

    Utiliza o método `model_dump(exclude_unset=True)` para aplicar apenas os
    campos explicitamente fornecidos no payload, preservando os demais valores
    já persistidos no registro (comportamento de PATCH).

    Args:
        db (Session): Sessão ativa do SQLAlchemy para interação com o banco de dados.
        chamado_id (int): Identificador único do chamado a ser atualizado.
        chamado_data (schemas.ChamadoUpdate): Schema Pydantic com os campos a atualizar.
            Campos ausentes ou `None` são ignorados na atualização.

    Returns:
        models.Chamado: Instância atualizada do chamado, com os dados mais recentes do banco.
        None: Se nenhum chamado for encontrado com o `chamado_id` informado.

    Raises:
        sqlalchemy.exc.SQLAlchemyError: Em caso de falha na transação com o banco de dados.

    Example:
        >>> payload = schemas.ChamadoUpdate(status_id=3, tecnico_id=7)
        >>> chamado = update_chamado(db, chamado_id=42, chamado_data=payload)
        >>> if chamado is None:
        ...     print("Chamado não encontrado.")
    """
    # Busca o chamado pelo ID; retorna None imediatamente se não existir
    chamado = db.query(models.Chamado).filter(models.Chamado.id == chamado_id).first()
    if not chamado:
        return None

    # Extrai apenas os campos enviados explicitamente no payload (ignora os omitidos)
    dados_update = chamado_data.model_dump(exclude_unset=True)

    # Aplica dinamicamente cada campo ao objeto ORM
    for campo, valor in dados_update.items():
        setattr(chamado, campo, valor)

    # Registra o momento exato da atualização
    chamado.atualizado_em = datetime.now()

    db.commit()       # Persiste as alterações no banco
    db.refresh(chamado)  # Sincroniza a instância com o estado atual do banco

    return chamado