import tkinter as tk
from tkinter import ttk, messagebox

from app.functions import registrar_item, listar_itens, adicionar_pedido, carregar_pedidos, carregar_pedidos_entregues, marcar_entregue

root = tk.Tk()
root.title("Sistema de Pedidos")

notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

frame_pedidos = ttk.Frame(notebook)
notebook.add(frame_pedidos, text="Pedidos")

frame_entregues = ttk.Frame(notebook)
notebook.add(frame_entregues, text="Pedidos Entregues")

frame_gestao = ttk.Frame(notebook)
notebook.add(frame_gestao, text="Gestão")

notebook.select(frame_pedidos)

# UI para registrar item
ttk.Label(frame_gestao, text="Nome").grid(row=0, column=0)
entry_nome = ttk.Entry(frame_gestao)
entry_nome.grid(row=0, column=1)

ttk.Label(frame_gestao, text="Descrição").grid(row=1, column=0)
entry_descricao = ttk.Entry(frame_gestao)
entry_descricao.grid(row=1, column=1)

ttk.Label(frame_gestao, text="Preço").grid(row=2, column=0)
entry_preco = ttk.Entry(frame_gestao)
entry_preco.grid(row=2, column=1)

ttk.Label(frame_gestao, text="Tipo").grid(row=3, column=0)
tipo_var = tk.StringVar()
tipo_menu = ttk.OptionMenu(frame_gestao, tipo_var, "prato", "prato", "bebida")
tipo_menu.grid(row=3, column=1)

def registrar_item_ui():
    nome = entry_nome.get()
    descricao = entry_descricao.get()
    preco = entry_preco.get()
    tipo = tipo_var.get()

    if registrar_item(nome, descricao, preco, tipo):
        messagebox.showinfo("Sucesso", f"{tipo.capitalize()} registrado com sucesso!")
        carregar_itens_ui()
    else:
        messagebox.showerror("Erro", "Erro ao registrar o item. Verifique os dados.")

def carregar_itens_ui():
    for i in tree_pratos.get_children():
        tree_pratos.delete(i)
    for item in listar_itens("prato"):
        tree_pratos.insert('', 'end', values=(item.nome, item.descricao, item.preco))

    for i in tree_bebidas.get_children():
        tree_bebidas.delete(i)
    for item in listar_itens("bebida"):
        tree_bebidas.insert('', 'end', values=(item.nome, item.descricao, item.preco))

# Função para o diálogo de novo pedido com coluna "Quantidade" editável na linha do item
def novo_pedido_dialog():
    dialog = tk.Toplevel()
    dialog.title("Novo Pedido")

    ttk.Label(dialog, text="Itens").grid(row=0, column=0, padx=10, pady=10)

    tree_itens_dialog = ttk.Treeview(dialog, columns=('Nome', 'Preço', 'Quantidade'), show='headings')
    tree_itens_dialog.heading('Nome', text='Nome')
    tree_itens_dialog.heading('Preço', text='Preço')
    tree_itens_dialog.heading('Quantidade', text='Quantidade')
    tree_itens_dialog.grid(row=1, column=0, padx=10, pady=10)

    quantidade_vars = {}

    def carregar_itens_dialog():
        for i in tree_itens_dialog.get_children():
            tree_itens_dialog.delete(i)
        for item in listar_itens("prato") + listar_itens("bebida"):
            tree_itens_dialog.insert('', 'end', values=(item.nome, item.preco, ""))
            quantidade_vars[item.nome] = tk.StringVar(value="0")

        for idx, item in enumerate(tree_itens_dialog.get_children()):
            nome_item = tree_itens_dialog.item(item, 'values')[0]
            quantidade_entry = tk.Entry(tree_itens_dialog, textvariable=quantidade_vars[nome_item], width=5)
            tree_itens_dialog.set(item, 'Quantidade', quantidade_vars[nome_item].get())
            quantidade_entry.place(x=450, y=28 + idx * 20)  # Corrigir a posição correta da caixa de entrada na célula

    def confirmar_pedido():
        itens_selecionados = []
        total_quantidade = 0

        for item in tree_itens_dialog.get_children():
            nome, preco, _ = tree_itens_dialog.item(item, 'values')
            quantidade = quantidade_vars[nome].get()
            if quantidade and int(quantidade) > 0:
                total_quantidade += int(quantidade)
                itens_selecionados.append({'nome': nome, 'preco': float(preco), 'quantidade': int(quantidade)})

        if total_quantidade <= 0:
            messagebox.showerror("Erro", "O pedido deve conter pelo menos um item.")
            return

        if not adicionar_pedido(itens_selecionados):
            messagebox.showerror("Erro", "Erro ao processar o pedido.")
            return

        carregar_pedidos_ui()
        dialog.destroy()

    ttk.Button(dialog, text="Confirmar Pedido", command=confirmar_pedido).grid(row=2, column=0, pady=10)
    carregar_itens_dialog()

def marcar_pedido_entregue():
    selected = tree_pedidos.selection()
    if selected:
        pedido_id = tree_pedidos.item(selected[0], 'values')[0]
        marcar_entregue(pedido_id)
        carregar_pedidos_ui()
        carregar_pedidos_entregues_ui()

def carregar_pedidos_ui():
    for i in tree_pedidos.get_children():
        tree_pedidos.delete(i)
    for pedido in carregar_pedidos():
        tree_pedidos.insert('', 'end', values=(pedido.id, pedido.valor_total, 'Não'))

def carregar_pedidos_entregues_ui():
    for i in tree_entregues.get_children():
        tree_entregues.delete(i)
    for pedido in carregar_pedidos_entregues():
        tree_entregues.insert('', 'end', values=(pedido.id, pedido.valor_total, 'Sim'))

ttk.Button(frame_pedidos, text="Novo Pedido", command=novo_pedido_dialog).pack(pady=10)

tree_pedidos = ttk.Treeview(frame_pedidos, columns=('ID', 'Valor Total', 'Entregue'), show='headings')
tree_pedidos.heading('ID', text='ID')
tree_pedidos.heading('Valor Total', text='Valor Total')
tree_pedidos.heading('Entregue', text='Entregue')
tree_pedidos.pack(pady=10)

btn_marcar_entregue = ttk.Button(frame_pedidos, text="Marcar como Entregue", command=marcar_pedido_entregue)
btn_marcar_entregue.pack(pady=5)

tree_entregues = ttk.Treeview(frame_entregues, columns=('ID', 'Valor Total', 'Entregue'), show='headings')
tree_entregues.heading('ID', text='ID')
tree_entregues.heading('Valor Total', text='Valor Total')
tree_entregues.heading('Entregue', text='Entregue')
tree_entregues.pack(pady=10)

carregar_pedidos_ui()
carregar_pedidos_entregues_ui()

btn_add_item = ttk.Button(frame_gestao, text="Registrar", command=registrar_item_ui)
btn_add_item.grid(row=4, column=0, columnspan=2)

tree_pratos = ttk.Treeview(frame_gestao, columns=('Nome', 'Descrição', 'Preço'), show='headings')
tree_pratos.heading('Nome', text='Nome')
tree_pratos.heading('Descrição', text='Descrição')
tree_pratos.heading('Preço', text='Preço')
tree_pratos.grid(row=5, column=0, columnspan=2)

tree_bebidas = ttk.Treeview(frame_gestao, columns=('Nome', 'Descrição', 'Preço'), show='headings')
tree_bebidas.heading('Nome', text='Nome')
tree_bebidas.heading('Descrição', text='Descrição')
tree_bebidas.heading('Preço', text='Preço')
tree_bebidas.grid(row=6, column=0, columnspan=2)

carregar_itens_ui()

root.mainloop()
