
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