# app/models.py
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Tabela associativa entre pedidos e pratos (pedido_prato)
pedido_prato = Table(
    'pedido_prato', Base.metadata,
    Column('pedido_id', ForeignKey('pedidos.id'), primary_key=True),
    Column('prato_id', ForeignKey('pratos.id'), primary_key=True),
    Column('quantidade', Integer, nullable=False)
)

# Modelo de Tabela 'Pratos'
class Prato(Base):
    __tablename__ = 'pratos'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    descricao = Column(String, nullable=False)
    preco = Column(Float, nullable=False)

# Modelo de Tabela 'Pedidos'
class Pedido(Base):
    __tablename__ = 'pedidos'
    
    id = Column(Integer, primary_key=True)
    valor_total = Column(Float, nullable=False)
    pratos = relationship('Prato', secondary=pedido_prato, backref='pedidos')
