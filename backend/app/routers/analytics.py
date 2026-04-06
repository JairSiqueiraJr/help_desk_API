from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app import crud, schemas

router = APIRouter(prefix="/analytics", tags=["Analytics"])


@router.get("/sla", response_model=list[schemas.SlaChamadoResponse])
def listar_sla(db: Session = Depends(get_db)):
    """
    Retorna a listagem analítica de SLA por chamado.
    """
    try:
        return crud.get_sla_chamados(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/dashboard", response_model=schemas.DashboardResumoResponse)
def obter_dashboard_resumo(db: Session = Depends(get_db)):
    """
    Retorna o resumo executivo do dashboard analítico.

    Métricas entregues:
        - total de chamados
        - chamados abertos
        - chamados em atendimento
        - chamados fechados/resolvidos
        - percentual dentro do SLA
        - percentual fora do SLA
        - tempo médio real de atendimento

    Returns:
        DashboardResumoResponse:
            Estrutura agregada para consumo por frontend ou ferramentas analíticas.
    """
    try:
        return crud.get_dashboard_resumo(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))