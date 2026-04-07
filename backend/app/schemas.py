from datetime import datetime
from pydantic import BaseModel, ConfigDict


class SlaChamadoResponse(BaseModel):
    """
    Schema de resposta para consulta analítica de SLA.
    """
    chamado_id: int
    categoria: str | None = None
    subcategoria: str | None = None
    sla_efetivo_horas: int | None = None
    tempo_real_horas: int | None = None
    status_sla: str | None = None

    model_config = ConfigDict(from_attributes=True)


class ChamadoCreate(BaseModel):
    """
    Schema de entrada para criação de um chamado.
    """
    titulo: str
    descricao: str | None = None
    usuario_id: int
    tecnico_id: int | None = None
    categoria_id: int
    subcategoria_id: int | None = None
    prioridade_id: int
    status_id: int


class ChamadoUpdate(BaseModel):
    """
    Schema de entrada para atualização parcial de um chamado.
    Todos os campos são opcionais.
    """
    titulo: str | None = None
    descricao: str | None = None
    usuario_id: int | None = None
    tecnico_id: int | None = None
    categoria_id: int | None = None
    subcategoria_id: int | None = None
    prioridade_id: int | None = None
    status_id: int | None = None


class ChamadoStatusUpdate(BaseModel):
    """
    Schema de entrada para atualização operacional de status de um chamado.

    Uso recomendado:
        - movimentação de fluxo (aberto, em atendimento, resolvido, fechado)
        - registro do técnico responsável pela transição
    """
    status_id: int
    tecnico_id: int | None = None


class ChamadoResponse(BaseModel):
    """
    Schema de resposta para operações de leitura, criação e atualização de chamados.
    """
    id: int
    titulo: str
    descricao: str | None = None
    usuario_id: int
    tecnico_id: int | None = None
    categoria_id: int
    subcategoria_id: int | None = None
    prioridade_id: int
    status_id: int
    criado_em: datetime | None = None
    atualizado_em: datetime | None = None

    model_config = ConfigDict(from_attributes=True)


class DashboardResumoResponse(BaseModel):
    """
    Schema de resposta para o resumo analítico do dashboard.
    """
    total_chamados: int
    chamados_abertos: int
    chamados_em_atendimento: int
    chamados_fechados: int
    percentual_dentro_sla: float
    percentual_fora_sla: float
    tempo_medio_horas: float


class DashboardCategoriaItem(BaseModel):
    """
    Item de agregação por categoria.
    """
    categoria: str
    total_chamados: int


class DashboardSlaCategoriaItem(BaseModel):
    """
    Item de SLA agregado por categoria.
    """
    categoria: str
    percentual_dentro_sla: float
    percentual_fora_sla: float


class DashboardTecnicoRankingItem(BaseModel):
    """
    Item de ranking de técnicos por volume de chamados atribuídos.
    """
    tecnico_id: int
    tecnico_nome: str
    total_chamados: int


class DashboardDetalhadoResponse(BaseModel):
    """
    Estrutura de resposta do dashboard detalhado.

    Blocos:
        chamados_por_categoria:
            Distribuição de volume por categoria.
        sla_por_categoria:
            Indicadores percentuais de SLA agrupados por categoria.
        ranking_tecnicos:
            Ranking de técnicos por quantidade de chamados atribuídos.
    """
    chamados_por_categoria: list[DashboardCategoriaItem]
    sla_por_categoria: list[DashboardSlaCategoriaItem]
    ranking_tecnicos: list[DashboardTecnicoRankingItem]