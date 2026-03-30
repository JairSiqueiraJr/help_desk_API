from datetime import datetime
from pydantic import BaseModel, ConfigDict


class SlaChamadoResponse(BaseModel):
    chamado_id: int
    categoria: str | None = None
    subcategoria: str | None = None
    sla_efetivo_horas: int | None = None
    tempo_real_horas: int | None = None
    status_sla: str | None = None

    model_config = ConfigDict(from_attributes=True)


class ChamadoCreate(BaseModel):
    titulo: str
    descricao: str | None = None
    usuario_id: int
    tecnico_id: int | None = None
    categoria_id: int
    subcategoria_id: int | None = None
    prioridade_id: int
    status_id: int


class ChamadoUpdate(BaseModel):
    titulo: str | None = None
    descricao: str | None = None
    usuario_id: int | None = None
    tecnico_id: int | None = None
    categoria_id: int | None = None
    subcategoria_id: int | None = None
    prioridade_id: int | None = None
    status_id: int | None = None


class ChamadoResponse(BaseModel):
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