
#from fastapi import APIRouter, Depends, HTTPException
#from sqlalchemy.orm import Session
#from app.database import get_db
#from app import crud, schemas

#router = APIRouter(prefix="/analytics", tags=["Analytics"])


#@router.get("/sla", response_model=list[schemas.SlaChamadoResponse])
#def listar_sla(db: Session = Depends(get_db)):
 #   return crud.get_sla_chamados(db)



#router = APIRouter(prefix="/chamados", tags=["Chamados"])


#@router.post("/", response_model=schemas.ChamadoResponse, status_code=201)
#def criar_chamado(chamado: schemas.ChamadoCreate, db: Session = Depends(get_db)):
 #   try:
  #      return crud.create_chamado(db, chamado)
   # except Exception as e:
    #    db.rollback()
     #   raise HTTPException(status_code=500, detail=str(e))//

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app import crud, schemas

router = APIRouter(prefix="/chamados", tags=["Chamados"])


@router.post("/", response_model=schemas.ChamadoResponse, status_code=201)
def criar_chamado(chamado: schemas.ChamadoCreate, db: Session = Depends(get_db)):
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
    Atualiza parcialmente os dados de um chamado pelo seu ID (PATCH semântico via PUT).

    Apenas os campos fornecidos no corpo da requisição serão modificados;
    os demais permanecem inalterados. Em caso de falha inesperada, a transação
    é revertida via `rollback` antes de retornar o erro ao cliente.

    Args:
        chamado_id (int): Identificador único do chamado a ser atualizado.
            Informado diretamente na URL (path parameter).
        chamado (schemas.ChamadoUpdate): Corpo da requisição com os campos
            a atualizar. Todos os campos são opcionais.
        db (Session): Sessão do banco de dados injetada automaticamente
            pelo mecanismo de dependência do FastAPI (`Depends(get_db)`).

    Returns:
        schemas.ChamadoResponse: Representação completa do chamado após
        a atualização, serializada conforme o schema de resposta.

    Raises:
        HTTPException (404): Se nenhum chamado for encontrado com o `chamado_id` informado.
        HTTPException (500): Se ocorrer qualquer erro inesperado durante a atualização.
            A transação é revertida com `db.rollback()` antes de lançar o erro.

    Example:
        >>> PUT /chamados/42
        ... {
        ...     "status_id": 3,
        ...     "tecnico_id": 7
        ... }
        # Resposta 200 — chamado atualizado
        # Resposta 404 — chamado com id 42 não existe
    """
    try:
        chamado_atualizado = crud.update_chamado(db, chamado_id, chamado)

        # Retorna 404 se a camada de CRUD não encontrar o chamado
        if not chamado_atualizado:
            raise HTTPException(status_code=404, detail="Chamado não encontrado")

        return chamado_atualizado

    except HTTPException:
        # Re-lança HTTPExceptions sem interceptar (404, etc.)
        raise

    except Exception as e:
        # Reverte a transação para evitar estado inconsistente no banco
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))