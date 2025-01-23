# importanto SQLite

import sqlite3 as lite

# criando conexao

conexao = lite.connect('control.db')


# criando tabela
with conexao:
    cur = conexao.cursor()
    cur.execute("CREATE TABLE formulario (id INTEGER PRIMARY KEY AUTOINCREMENT, Codigo_produto NUMERIC, Nome_produto TEXT, Loja TEXT, Quantidade NUMERIC, Atualizado_em DATE)")
