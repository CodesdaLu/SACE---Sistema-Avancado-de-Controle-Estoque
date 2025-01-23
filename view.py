import sqlite3 as lite

# CRIANDO CONEXAO DB
conexao = lite.connect('control.db')

def inserir_info(i):

    if i:  # Verifica se a lista não está vazia
        with conexao:
            cur = conexao.cursor()
            query = "INSERT INTO formulario (Codigo_produto, Nome_produto, Loja, Quantidade, Atualizado_em) VALUES (?, ?, ?, ?, ?)"
            cur.execute(query, i)
    else:
        print("Lista vazia. Não foram inseridos dados.")




## ACESSAR INFO ##

def mostrar_info():
    lista = []

    with conexao:
        cur = conexao.cursor()
        query = "SELECT * FROM formulario"
        cur.execute(query)
        info = cur.fetchall()
    
    for i in info:
        lista.append(i)
    return lista
        
    



## UPDATE INFO ##

def atualizar_info(i):
    
    with conexao:
        cur = conexao.cursor()
        query = "UPDATE formulario SET Codigo_produto =?, Nome_produto=? , Loja=? , Quantidade=? , Atualizado_em=? WHERE id=?"
        cur.execute(query,i)
    

    

## DELETE INFO ##
def deletar_info(i):
    with conexao:
        cur = conexao.cursor()
        query = "DELETE FROM formulario WHERE id=?"
        cur.execute(query, i) 
    
