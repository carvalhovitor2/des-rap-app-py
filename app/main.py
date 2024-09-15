# app/main.py
import tkinter as tk
from tkinter import ttk, messagebox
from app.functions import add_pedido, list_pratos, list_pedidos, add_prato
from app.database import init_db

# Inicializa o banco de dados
init_db()

# Função para registrar um novo pedido
def registrar_pedido():
    pratos_selecionados = []
    
    # Pega as quantidades inseridas para cada prato
    for prato_entry in prato_entries:
        prato_id = prato_entry['prato_id']
        quantidade = prato_entry['quantidade_entry'].get()
        if quantidade.isdigit() and int(quantidade) > 0:
            pratos_selecionados.append((prato_id, int(quantidade)))
    
    if pratos_selecionados:
        add_pedido(pratos_selecionados)
        messagebox.showinfo("Sucesso", "Pedido registrado com sucesso!")
        listar_pedidos_ui()  # Atualiza a lista de pedidos
        for prato_entry in prato_entries:  # Limpa as caixas de quantidade após o pedido
            prato_entry['quantidade_entry'].delete(0, tk.END)
    else:
        messagebox.showwarning("Erro", "Insira uma quantidade válida para pelo menos um prato.")

# Função para listar pratos na interface e adicionar caixas de entrada de quantidade
def listar_pratos_ui():
    for widget in prato_frame.winfo_children():  # Limpa o frame de pratos
        widget.destroy()

    global prato_entries
    prato_entries = []

    pratos = list_pratos()

    for i, prato in enumerate(pratos):
        # Cria rótulos para nome e preço do prato
        ttk.Label(prato_frame, text=f"{prato.nome} - {prato.preco:.2f}").grid(row=i, column=0)
        
        # Cria uma caixa de entrada para a quantidade
        quantidade_entry = ttk.Entry(prato_frame, width=5)
        quantidade_entry.grid(row=i, column=1)

        # Armazena os IDs dos pratos e as caixas de quantidade
        prato_entries.append({'prato_id': prato.id, 'quantidade_entry': quantidade_entry})

# Função para listar pedidos na interface
def listar_pedidos_ui():
    pedido_list.delete(*pedido_list.get_children())  # Limpa a lista
    pedidos = list_pedidos()
    for pedido in pedidos:
        pedido_list.insert("", "end", values=(pedido.id, pedido.valor_total))

# Função para aplicar um estilo moderno com tons de amarelo
def aplicar_estilo_moderno():
    style = ttk.Style()
    style.theme_use('clam')

    # Estilo moderno com tons de amarelo
    style.configure("TFrame", background="#FFFACD")  # Fundo amarelo claro
    style.configure("TLabel", background="#FFFACD", font=('Helvetica', 12), foreground="#333")
    style.configure("TButton", background="#FFD700", font=('Helvetica', 12), foreground="#000000")  # Botão amarelo ouro
    style.configure("Treeview", background="#FFFACD", foreground="black", rowheight=25, fieldbackground="#FFFACD")
    style.configure("TNotebook", background="#FFD700", tabmargins=[2, 5, 2, 0])  # Aba amarela
    style.map("TButton", background=[('active', '#FFD700')])

# Interface principal
root = tk.Tk()
root.title("Sistema de Pedidos - Food Truck Alex")
root.geometry("800x600")

# Aplicar o estilo moderno
aplicar_estilo_moderno()

# Aba de pedidos (Página principal)
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

frame_pedidos = ttk.Frame(notebook)
notebook.add(frame_pedidos, text="Pedidos")

# Frame para os pratos e suas quantidades
prato_frame = ttk.Frame(frame_pedidos)
prato_frame.grid(row=0, column=0, columnspan=2, pady=10)

# Lista de pedidos já feitos (Maior destaque)
ttk.Label(frame_pedidos, text="Pedidos Registrados:").grid(row=4, column=0, columnspan=2)

pedido_list = ttk.Treeview(frame_pedidos, columns=("ID", "Valor Total"), show='headings', height=8)
pedido_list.heading("ID", text="ID")
pedido_list.heading("Valor Total", text="Valor Total")
pedido_list.grid(row=5, column=0, columnspan=2)

# Botão para registrar o pedido
btn_add_pedido = ttk.Button(frame_pedidos, text="Registrar Pedido", command=registrar_pedido)
btn_add_pedido.grid(row=6, column=0, columnspan=2, pady=10)

# Aba de pratos para registrar novos pratos (caso necessário)
frame_pratos = ttk.Frame(notebook)
notebook.add(frame_pratos, text="Registrar Prato")

ttk.Label(frame_pratos, text="Nome do Prato:").grid(row=0, column=0)
entry_nome_prato = ttk.Entry(frame_pratos)
entry_nome_prato.grid(row=0, column=1)

ttk.Label(frame_pratos, text="Descrição:").grid(row=1, column=0)
entry_descricao_prato = ttk.Entry(frame_pratos)
entry_descricao_prato.grid(row=1, column=1)

ttk.Label(frame_pratos, text="Preço:").grid(row=2, column=0)
entry_preco_prato = ttk.Entry(frame_pratos)
entry_preco_prato.grid(row=2, column=1)

btn_add_prato = ttk.Button(frame_pratos, text="Registrar Prato", command=add_prato)
btn_add_prato.grid(row=3, column=0, columnspan=2)

# Inicializa a interface com dados
listar_pratos_ui()
listar_pedidos_ui()

# Executa a interface
root.mainloop()

