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



class ChamadoStatusUpdate(BaseModel):
    """
    Schema de entrada para atualização operacional de status de um chamado.

    Campos:
        status_id:
            Identificador do novo status do chamado.
        tecnico_id:
            Identificador do técnico responsável pela alteração.
            Campo opcional, mas recomendado para rastreabilidade operacional.
    """
    status_id: int
    tecnico_id: int | None = None



class DashboardResumoResponse(BaseModel):
    """
    Schema de resposta para o resumo analítico do dashboard.

    Campos:
        total_chamados:
            Quantidade total de chamados cadastrados.
        chamados_abertos:
            Quantidade de chamados atualmente abertos.
        chamados_em_atendimento:
            Quantidade de chamados em atendimento.
        chamados_fechados:
            Quantidade de chamados encerrados.
        percentual_dentro_sla:
            Percentual de chamados dentro do SLA.
        percentual_fora_sla:
            Percentual de chamados fora do SLA.
        tempo_medio_horas:
            Tempo médio real de atendimento em horas.
    """
    total_chamados: int
    chamados_abertos: int
    chamados_em_atendimento: int
    chamados_fechados: int
    percentual_dentro_sla: float
    percentual_fora_sla: float
    tempo_medio_horas: float