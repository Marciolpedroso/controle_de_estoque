import sqlite3

conn = sqlite3.connect('estoque.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS itens_estoque (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    tipo TEXT,
    valor TEXT,
    quantidade INTEGER NOT NULL
)
''')
conn.commit()

def cadastrar_item(nome, tipo, valor, quantidade):
    try:
        cursor.execute(
            "INSERT INTO itens_estoque (nome, tipo, valor, quantidade) VALUES (?, ?, ?, ?)",
            (nome, tipo, valor, quantidade)
        )
        conn.commit()
        return True
    except Exception as e:
        print("Erro ao cadastrar:", e)
        return False

def consultar_todos():
    cursor.execute("SELECT * FROM itens_estoque")
    return cursor.fetchall()

def remover_quantidade(id_item, quantidade_remover):
    try:
        cursor.execute("SELECT quantidade FROM itens_estoque WHERE id = ?", (id_item,))
        resultado = cursor.fetchone()

        if not resultado:
            return False, "Item não encontrado!"

        estoque_atual = resultado[0]

        if quantidade_remover <= 0:
            return False, "Quantidade deve ser maior que zero."

        if quantidade_remover > estoque_atual:
            return False, f"Não é possível remover {quantidade_remover}, estoque atual é {estoque_atual}."

        nova_quantidade = estoque_atual - quantidade_remover
        cursor.execute("UPDATE itens_estoque SET quantidade = ? WHERE id = ?", (nova_quantidade, id_item))
        conn.commit()

        return True, f"Quantidade atualizada para {nova_quantidade}."
    except Exception as e:
        print("Erro ao remover:", e)
        return False, "Erro ao atualizar estoque."

def adicionar_quantidade(id_item, quantidade_adicionar):
    try:
        cursor.execute("SELECT quantidade FROM itens_estoque WHERE id = ?", (id_item,))
        resultado = cursor.fetchone()

        if not resultado:
            return False, "Item não encontrado!"

        if quantidade_adicionar <= 0:
            return False, "Quantidade deve ser maior que zero."

        estoque_atual = resultado[0]
        nova_quantidade = estoque_atual + quantidade_adicionar

        cursor.execute("UPDATE itens_estoque SET quantidade = ? WHERE id = ?", (nova_quantidade, id_item))
        conn.commit()

        return True, f"Quantidade atualizada para {nova_quantidade}."
    except Exception as e:
        print("Erro ao adicionar:", e)
        return False, "Erro ao atualizar estoque."
