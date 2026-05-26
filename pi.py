import sqlite3

conexao = sqlite3.connect("banco_Pi.db")

cursor = conexao.cursor()

# Criar tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS pessoas (
    Nome TEXT,
    Idade INTEGER,
    Genero TEXT,
    Tipo de Machucado TEXT,
    Gravidade do Machucado TEXT            )
""")

# Inserir dados
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Carlos Silva",34,'Masculino','Fratura Fechada (Braço)','Moderada'))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Mariana Costa",22,'Feminino','Corte profundo (Mão)','Moderada'))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Roberto Souza",45,'Masculino','Contusão torácica','Grave' ))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Ana Júlia Lima",8,'Feminino','Escoreação (Joelho)','Leve' ))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Ricardo Oliveira",61,'Masculino','Entorse de tornozelo','Leve' ))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Beatriz Santos",29,'Feminino','Queimadura','Grave' ))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Fernando Almeida",73,'Masculino','Traumatismo Craniano leve','Critica' ))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Camila Ribeiro",19,'Feminino','Picada de inseto com alergia','Moderada' ))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Lucas Martins",41,'Masculino','Lacerção no pé','Moderada' ))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Juliana Rocha",55,'Feminino','Luxação de ombro','Moderada' ))

# Salvar mudanças
conexao.commit()

# Mostrar dados
cursor.execute("SELECT * FROM pessoas")
print(cursor.fetchall())

# Fechar conexão
conexao.close()