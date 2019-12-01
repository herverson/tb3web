import sqlite3

connection = sqlite3.connect('dado.db')
cursor = connection.cursor()

criar_tabela = """CREATE TABLE IF NOT EXISTS usuarios 
                (id INTEGER PRIMARY KEY, nome text,
                senha text)"""
cursor.execute(criar_tabela)

criar_tabela = """CREATE TABLE IF NOT EXISTS topicos 
                (nome text, preco real)"""
cursor.execute(criar_tabela)
criar_tabela = """CREATE TABLE IF NOT EXISTS relacionamentos 
                (descricao text, id_topico1 INTEGER, id_topico2 INTEGER, id_disciplina1 INTEGER, id_disciplina2 INTEGER)"""
cursor.execute(criar_tabela)

connection.commit()
connection.close()
