import sqlite3

conexao = sqlite3.connect('cadastros_casa_de_apostas.db')
cursor = conexao.cursor()

#CRIAR UMA TABELA 

cursor.execute('''
       CREATE TABLE IF NOT EXISTS pessoas(
          id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
          nome TEXT NOT NULL,
          idade INTERGER NOT NULL,
          cidade TEXT NOT NULL
    )
    ''')

#inserir dados na tabela

nome = input('Digite um nome')
idade = int(input('Digite sua idade'))
cidade = input('Digite sua cidade')

cursor.execute('''
        INSERT INTO pessoas (nome, idade, cidade)
        VALUES (?, ?, ?)
''', (nome, idade, cidade))


# Confirmação a transação

conexao.commit()

# Consultar dados da tabela

cursor.execute('SELECT * FROM pessoas')
pessoas = cursor.fetchall()

# Mostrar os dados consultados
for pessoa in pessoas:
    print(f''' ID: {pessoa[0]}, Nome: {pessoa[1]}, Idade: {pessoa[2]}, Cidade: {pessoa[3]}''')

conexao.closed()