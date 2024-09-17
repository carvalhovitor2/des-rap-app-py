from sqlalchemy import Column, Integer, String, Float, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Item(Base):
    __tablename__ = 'items'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String(30), nullable=False)
    descricao = Column(String(120), nullable=False)
    preco = Column(Float, nullable=False)
    tipo = Column(String(10), nullable=False)

class Pedido(Base):
    __tablename__ = 'pedidos'
    
    id = Column(Integer, primary_key=True)
    valor_total = Column(Float, nullable=False)
    entregue = Column(Boolean, default=False)

engine = create_engine('sqlite:///foodtruck.db')
Base.metadata.create_all(engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
