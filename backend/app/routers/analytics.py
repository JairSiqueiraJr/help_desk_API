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
    """
    try:
        return crud.get_dashboard_resumo(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.get("/dashboard/detalhado", response_model=schemas.DashboardDetalhadoResponse)
def obter_dashboard_detalhado(
    status_id: int | None = None,
    categoria_id: int | None = None,
    tecnico_id: int | None = None,
    data_inicio: str | None = None,
    data_fim: str | None = None,
    db: Session = Depends(get_db)
):
    """
    Retorna o dashboard detalhado com suporte a filtros operacionais e temporais.

    Query params suportados:
        - status_id
        - categoria_id
        - tecnico_id
        - data_inicio (YYYY-MM-DD)
        - data_fim (YYYY-MM-DD)

    Exemplos:
        /analytics/dashboard/detalhado?status_id=2
        /analytics/dashboard/detalhado?categoria_id=1&tecnico_id=2
        /analytics/dashboard/detalhado?data_inicio=2026-03-01&data_fim=2026-03-31

    Args:
        status_id:
            Filtro opcional por status do chamado.
        categoria_id:
            Filtro opcional por categoria.
        tecnico_id:
            Filtro opcional por técnico responsável.
        data_inicio:
            Filtro opcional de data inicial com base em criado_em.
        data_fim:
            Filtro opcional de data final com base em criado_em.
        db:
            Sessão ativa do banco de dados.

    Returns:
        schemas.DashboardDetalhadoResponse:
            Estrutura detalhada contendo:
            - chamados por categoria
            - SLA por categoria
            - ranking de técnicos

    Raises:
        HTTPException(500):
            Retornada em caso de falha inesperada na consulta analítica.
    """
    
    try:
        return crud.get_dashboard_detalhado(
            db=db,
            status_id=status_id,
            categoria_id=categoria_id,
            tecnico_id=tecnico_id,
            data_inicio=data_inicio,
            data_fim=data_fim
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))