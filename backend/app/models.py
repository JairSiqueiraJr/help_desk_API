from sqlalchemy import Column, BigInteger, String, Text, DateTime, ForeignKey
from app.database import Base


class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(BigInteger, primary_key=True, index=True)


class Categoria(Base):
    __tablename__ = "categorias"
    id = Column(BigInteger, primary_key=True, index=True)


class Subcategoria(Base):
    __tablename__ = "subcategorias"
    id = Column(BigInteger, primary_key=True, index=True)


class Prioridade(Base):
    __tablename__ = "prioridade"
    id = Column(BigInteger, primary_key=True, index=True)


class Status(Base):
    __tablename__ = "status"
    id = Column(BigInteger, primary_key=True, index=True)


class VwSlaChamado(Base):
    __tablename__ = "vw_sla_chamados"

    chamado_id = Column(BigInteger, primary_key=True, index=True)
    categoria = Column(String(100), nullable=True)
    subcategoria = Column(String(100), nullable=True)
    sla_efetivo_horas = Column(BigInteger, nullable=True)
    tempo_real_horas = Column(BigInteger, nullable=True)
    status_sla = Column(String(50), nullable=True)


class Chamado(Base):
    __tablename__ = "chamados"

    id = Column(BigInteger, primary_key=True, index=True)
    titulo = Column(String(200), nullable=False)
    descricao = Column("descricao", Text, nullable=True)
    usuario_id = Column(BigInteger, ForeignKey("usuarios.id"), nullable=False)
    tecnico_id = Column(BigInteger, ForeignKey("usuarios.id"), nullable=True)
    categoria_id = Column(BigInteger, ForeignKey("categorias.id"), nullable=False)
    subcategoria_id = Column(BigInteger, ForeignKey("subcategorias.id"), nullable=True)
    prioridade_id = Column(BigInteger, ForeignKey("prioridade.id"), nullable=False)
    status_id = Column(BigInteger, ForeignKey("status.id"), nullable=False)
    criado_em = Column(DateTime, nullable=True)
    atualizado_em = Column(DateTime, nullable=True)