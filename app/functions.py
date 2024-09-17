from app.models import SessionLocal, Item, Pedido

# Função para registrar um novo prato ou bebida e atualizar a lista na UI
def registrar_item_ui():
    nome = entry_nome.get()
    descricao = entry_descricao.get()
    preco = entry_preco.get()
    tipo = tipo_var.get()

    if registrar_item(nome, descricao, preco, tipo):
        messagebox.showinfo("Sucesso", f"{tipo.capitalize()} registrado com sucesso!")
        carregar_itens_ui()  # Atualiza a lista de itens após registrar
    else:
        messagebox.showerror("Erro", "Erro ao registrar o item. Verifique os dados.")

def registrar_item(nome, descricao, preco, tipo):
    session = SessionLocal()
    if len(nome) > 30 or len(descricao) > 120:
        return False
    try:
        preco = round(float(preco), 2)
    except ValueError:
        return False
    novo_item = Item(nome=nome, descricao=descricao, preco=preco, tipo=tipo)
    session.add(novo_item)
    session.commit()
    session.close()
    return True

def listar_itens(tipo):
    session = SessionLocal()
    items = session.query(Item).filter_by(tipo=tipo).all()
    session.close()
    return items

def adicionar_pedido(itens_selecionados):
    if len(itens_selecionados) == 0:
        return False  # Verificação de pedido vazio
    session = SessionLocal()
    valor_total = sum([item['preco'] * item['quantidade'] for item in itens_selecionados])
    novo_pedido = Pedido(valor_total=valor_total)
    session.add(novo_pedido)
    session.commit()
    session.close()
    return True

def listar_pedidos():
    session = SessionLocal()
    pedidos = session.query(Pedido).all()
    session.close()
    return pedidos

def marcar_entregue(pedido_id):
    session = SessionLocal()
    pedido = session.query(Pedido).filter_by(id=pedido_id).first()
    if pedido:
        pedido.entregue = True
        session.commit()
    session.close()

def carregar_pedidos():
    session = SessionLocal()
    pedidos = session.query(Pedido).filter_by(entregue=False).all()
    session.close()
    return pedidos

def carregar_pedidos_entregues():
    session = SessionLocal()
    pedidos_entregues = session.query(Pedido).filter_by(entregue=True).all()
    session.close()
    return pedidos_entregues

