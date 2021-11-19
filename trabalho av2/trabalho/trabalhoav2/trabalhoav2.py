
import sqlite3

conn = sqlite3.connect("trabalhoav2/cad_e_consul.db")
cursor = conn.cursor()

#Criando a tabela
try:
    cursor.execute('''CREATE TABLE if not exists cad_e_consul
                        (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        matricula INTEGER,
                        av1 FLOAT,
                        av2 FLOAT,
                        av3 FLOAT,
                        avd FLOAT,
                        avds FLOAT,
                        email TEXT,
                        endereço TEXT,
                        campus TEXT,
                        periodo INTEGER);''')

except sqlite3.Error as e:
    print('ERRO: Falha ao criar banco\nErro TIPO: ', e)

#Fim da criação do banco

#Inserindo os dados

nome = str(input('Nome: '))
matricula = int(input('Matricula: '))
av1 = float(input('AV1: '))
av2 = float(input('AV2: '))
av3 = float(input('AV3: '))
avd = float(input('AVD: '))
avds = float(input('AVDS: '))
email = str(input('Email: '))
endereço = str(input('Endereço: '))
campus = str(input('Campus: '))
periodo = int(input('Periodo: '))

lista = [(nome, matricula, av1, av2, av3, avd, avds, email, endereço, campus, periodo)]

#Inserindo os dados na tabela
cursor.executemany("""INSERT INTO cad_e_consul
                    (nome, matricula, av1, av2, av3, avd, avds, email, endereço, campus, periodo) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", lista)
conn.commit()
#Fim da inserção dos dados na tabela.

#Exibir os dados na tela
cursor.execute('''SELECT * FROM cad_e_consul''')
for linha in cursor:
    print(linha)
conn.close()

