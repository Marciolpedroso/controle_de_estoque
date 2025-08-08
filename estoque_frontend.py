import tkinter as tk
from tkinter import messagebox
from estoque_backend import cadastrar_item, consultar_todos, remover_quantidade, adicionar_quantidade

root = tk.Tk()
root.title("Controle de Estoque")

# --- Cadastro ---

tk.Label(root, text="Nome").grid(row=0, column=0, sticky="e")
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1)

tk.Label(root, text="Tipo").grid(row=1, column=0, sticky="e")
entry_tipo = tk.Entry(root)
entry_tipo.grid(row=1, column=1)

tk.Label(root, text="Valor").grid(row=2, column=0, sticky="e")
entry_valor = tk.Entry(root)
entry_valor.grid(row=2, column=1)

tk.Label(root, text="Quantidade").grid(row=3, column=0, sticky="e")
entry_quantidade = tk.Entry(root)
entry_quantidade.grid(row=3, column=1)

def salvar_item():
    nome = entry_nome.get().strip()
    tipo = entry_tipo.get().strip()
    valor = entry_valor.get().strip()
    quantidade_str = entry_quantidade.get().strip()

    if not nome or not quantidade_str:
        messagebox.showwarning("Aviso", "Nome e Quantidade são obrigatórios!")
        return

    if not quantidade_str.isdigit():
        messagebox.showwarning("Aviso", "Quantidade deve ser um número inteiro!")
        return

    quantidade = int(quantidade_str)
    if quantidade < 0:
        messagebox.showwarning("Aviso", "Quantidade deve ser zero ou maior!")
        return

    sucesso = cadastrar_item(nome, tipo, valor, quantidade)
    if sucesso:
        messagebox.showinfo("Sucesso", "Item cadastrado com sucesso!")
        limpar_campos()
        atualizar_lista()
    else:
        messagebox.showerror("Erro", "Falha ao cadastrar item.")

def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_tipo.delete(0, tk.END)
    entry_valor.delete(0, tk.END)
    entry_quantidade.delete(0, tk.END)

btn_cadastrar = tk.Button(root, text="Cadastrar Item", command=salvar_item)
btn_cadastrar.grid(row=4, column=0, columnspan=2, pady=5)

# --- Lista de Itens ---

lista_itens = tk.Listbox(root, width=60)
lista_itens.grid(row=0, column=2, rowspan=15, padx=10, pady=5)

def atualizar_lista():
    lista_itens.delete(0, tk.END)
    itens = consultar_todos()
    for item in itens:
        linha = f"ID {item[0]} | Nome: {item[1]} | Tipo: {item[2]} | Valor: {item[3]} | Qtde: {item[4]}"
        lista_itens.insert(tk.END, linha)

atualizar_lista()

# --- Remover Quantidade ---

tk.Label(root, text="ID para remover:").grid(row=5, column=0, sticky="e")
entry_id_remover = tk.Entry(root)
entry_id_remover.grid(row=5, column=1)

tk.Label(root, text="Qtd a remover:").grid(row=6, column=0, sticky="e")
entry_qnt_remover = tk.Entry(root)
entry_qnt_remover.grid(row=6, column=1)

def remover_item_interface():
    id_remover = entry_id_remover.get().strip()
    qnt_remover = entry_qnt_remover.get().strip()

    if not id_remover or not qnt_remover:
        messagebox.showwarning("Aviso", "Informe o ID e a quantidade para remover!")
        return

    if not id_remover.isdigit() or not qnt_remover.isdigit():
        messagebox.showwarning("Aviso", "ID e quantidade devem ser números inteiros!")
        return

    id_int = int(id_remover)
    qnt_int = int(qnt_remover)

    sucesso, mensagem = remover_quantidade(id_int, qnt_int)
    if sucesso:
        messagebox.showinfo("Sucesso", mensagem)
        atualizar_lista()
    else:
        messagebox.showerror("Erro", mensagem)

btn_remover = tk.Button(root, text="Remover do Estoque", command=remover_item_interface)
btn_remover.grid(row=7, column=0, columnspan=2, pady=5)

# --- Adicionar Quantidade ---

tk.Label(root, text="ID para adicionar:").grid(row=8, column=0, sticky="e")
entry_id_adicionar = tk.Entry(root)
entry_id_adicionar.grid(row=8, column=1)

tk.Label(root, text="Qtd a adicionar:").grid(row=9, column=0, sticky="e")
entry_qnt_adicionar = tk.Entry(root)
entry_qnt_adicionar.grid(row=9, column=1)

def adicionar_item_interface():
    id_add = entry_id_adicionar.get().strip()
    qnt_add = entry_qnt_adicionar.get().strip()

    if not id_add or not qnt_add:
        messagebox.showwarning("Aviso", "Informe o ID e a quantidade para adicionar!")
        return

    if not id_add.isdigit() or not qnt_add.isdigit():
        messagebox.showwarning("Aviso", "ID e quantidade devem ser números inteiros!")
        return

    id_int = int(id_add)
    qnt_int = int(qnt_add)

    sucesso, mensagem = adicionar_quantidade(id_int, qnt_int)
    if sucesso:
        messagebox.showinfo("Sucesso", mensagem)
        atualizar_lista()
    else:
        messagebox.showerror("Erro", mensagem)

btn_adicionar = tk.Button(root, text="Adicionar ao Estoque", command=adicionar_item_interface)
btn_adicionar.grid(row=10, column=0, columnspan=2, pady=5)

root.mainloop()
