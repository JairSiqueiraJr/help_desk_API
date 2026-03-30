from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app import crud

router = APIRouter(prefix="/analytics", tags=["Analytics"])


@router.get("/sla")
def listar_sla(db: Session = Depends(get_db)):
    try:
        dados = crud.get_sla_chamados(db)
        return {"total": len(dados)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))