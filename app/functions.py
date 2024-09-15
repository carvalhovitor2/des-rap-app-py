# app/functions.py
from app.database import SessionLocal
from app.models import Prato, Pedido, pedido_prato

def add_pedido(pratos_quantidades):
    session = SessionLocal()
    
    valor_total = 0
    for prato_id, quantidade in pratos_quantidades:
        prato = session.query(Prato).get(prato_id)
        valor_total += prato.preco * quantidade
    
    novo_pedido = Pedido(valor_total=valor_total)
    session.add(novo_pedido)
    session.commit()  

    for prato_id, quantidade in pratos_quantidades:
        stmt = pedido_prato.insert().values(pedido_id=novo_pedido.id, prato_id=prato_id, quantidade=quantidade)
        session.execute(stmt)
    
    session.commit() 
    session.close()

def add_prato(nome, descricao, preco):
    session = SessionLocal()
    novo_prato = Prato(nome=nome, descricao=descricao, preco=preco)
    session.add(novo_prato)
    session.commit()
    session.close()

def list_pratos():
    session = SessionLocal()
    pratos = session.query(Prato).all()
    session.close()
    return pratos

def list_pedidos():
    session = SessionLocal()
    pedidos = session.query(Pedido).all()
    session.close()
    return pedidos
