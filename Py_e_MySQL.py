import MySQLdb

#Parâmetros da conexão

host= "localhost"
user = "aplicacao"
password = "123456"
db = "escola_curso"
port = 3306

con = MySQLdb.connect(host, user, password, db, port)

# Função para transformar resultado em tupla de dicionários

c = con.cursor(MySQLdb.cursors.DictCursor)

# Criação da seleção

def select(colunas, tabelas, where=None):
    global c
    query = "SELECT" + colunas + "FROM" + tabelas
    if (where):
        query = query + "WHERE" + where
    c.execute(query)
    return c.fetchall()

selecao = select("nome","alunos","id_aluno=1")

print(selecao)

# Criação de inserção

def insert(valores, tabela, colunas=None):
    global c, con
    query = "INSERT INTO" + tabela
    if (colunas):
        query = query + " ("+ colunas + ") "
    query = query + "valores" + ",".join(["(" + v + ")" for v in valores])

    c.execute(query)
    con.commit()

    print(query)

insercao = ["Default, 'João Pedro', '2000-01-01', 'Av das Pedras', 'Betim', 'MG', '12345678911'"]

insert(insercao, "alunos")

# Criação da atualização

def update(sets, tabela, where=None):

    global c,con

    query = "UPDATE" + tabela
    query = query + "SET" + ",".join([coluna + " = '" + valor + "'" for coluna, valor in sets.items()])
    if(where):
        query = query + "WHERE" + where

    c.execute(query)
    con.commit()

set = update({"nome":"João Martins"}, "alunos")

# Criação da deleção

def delete (tabela,where):

    global c, con

    query = "DELETE FROM " + tabela + "WHERE" + where

    c.execute(query)
    con.commit()

deletar = delete("alunos","id_aluno=9")


