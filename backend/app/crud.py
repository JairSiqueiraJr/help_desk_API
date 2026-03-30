from datetime import datetime
from sqlalchemy.orm import Session
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