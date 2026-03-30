from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app import crud, schemas

router = APIRouter(prefix="/chamados", tags=["Chamados"])


@router.post("/", response_model=schemas.ChamadoResponse, status_code=201)
def criar_chamado(chamado: schemas.ChamadoCreate, db: Session = Depends(get_db)):
    """
    Cria um novo chamado.

    Returns:
        Representação completa do chamado criado.
    """
    try:
        return crud.create_chamado(db, chamado)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/{chamado_id}", response_model=schemas.ChamadoResponse)
def atualizar_chamado(
    chamado_id: int,
    chamado: schemas.ChamadoUpdate,
    db: Session = Depends(get_db)
):
    """
    Atualiza parcialmente os dados de um chamado pelo seu ID.

    Apenas os campos fornecidos no corpo da requisição serão modificados;
    os demais permanecem inalterados.

    Args:
        chamado_id:
            Identificador do chamado a ser atualizado.
        chamado:
            Payload com dados parciais do chamado.
        db:
            Sessão do banco injetada via dependência.

    Returns:
        O chamado atualizado.

    Raises:
        HTTPException(404):
            Se o chamado não for encontrado.
        HTTPException(500):
            Se ocorrer erro inesperado durante a operação.
    """
    try:
        chamado_atualizado = crud.update_chamado(db, chamado_id, chamado)

        if not chamado_atualizado:
            raise HTTPException(status_code=404, detail="Chamado não encontrado")

        return chamado_atualizado
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/{chamado_id}/status", response_model=schemas.ChamadoResponse)
def atualizar_status_chamado(
    chamado_id: int,
    status_data: schemas.ChamadoStatusUpdate,
    db: Session = Depends(get_db)
):
    """
    Atualiza exclusivamente o status operacional de um chamado.

    Endpoint recomendado para uso operacional do helpdesk, pois restringe
    a alteração ao fluxo de status e ao técnico responsável.

    Args:
        chamado_id:
            Identificador do chamado a ser atualizado.
        status_data:
            Payload contendo o novo status e, opcionalmente, o técnico.
        db:
            Sessão do banco de dados.

    Returns:
        O chamado atualizado após a mudança de status.

    Raises:
        HTTPException(404):
            Se o chamado não existir.
        HTTPException(500):
            Se ocorrer erro inesperado na atualização.
    """
    try:
        chamado_atualizado = crud.update_chamado_status(db, chamado_id, status_data)

        if not chamado_atualizado:
            raise HTTPException(status_code=404, detail="Chamado não encontrado")

        return chamado_atualizado
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))