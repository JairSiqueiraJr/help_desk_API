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
    

@router.get("/dashboard/detalhado", response_model=schemas.DashboardDetalhadoResponse)
def obter_dashboard_detalhado(
    status_id: int | None = None,
    categoria_id: int | None = None,
    tecnico_id: int | None = None,
    db: Session = Depends(get_db)
):
    """
    Retorna o dashboard detalhado com suporte a filtros operacionais.

    Query params suportados:
        - status_id
        - categoria_id
        - tecnico_id

    Exemplos:
        /analytics/dashboard/detalhado?status_id=2
        /analytics/dashboard/detalhado?categoria_id=1&tecnico_id=2

    Returns:
        DashboardDetalhadoResponse:
            Estrutura detalhada filtrada conforme os parâmetros informados.

    Raises:
        HTTPException(500):
            Em caso de falha inesperada na consulta analítica.
    """
    try:
        return crud.get_dashboard_detalhado(
            db=db,
            status_id=status_id,
            categoria_id=categoria_id,
            tecnico_id=tecnico_id
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))