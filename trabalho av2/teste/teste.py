import sqlite3

conn = sqlite3.connect("cadastro.db")
cursor = conn.cursor()

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


def salvar():
    cursor.executemany("""INSERT INTO cad_e_consul
                    (nome, matricula) VALUES (?, ?)""", lista)
    conn.commit()
    
    mostrar_nome = print("Nome: ", nome.get())
    mostrar_matricula = print("Matricula: ", matricula.get())
    


from tkinter import *

root = Tk()
root.geometry("400x400")
root.title("Cadastro de alunos")

Label(text="nome").grid(row=0,column=0)
nome = Entry()
nome.grid(row=0, column=2)

Label(text="matricula").grid(row=1,column=0)
matricula = Entry()
matricula.grid(row=1, column=2)

lista = [(nome, matricula)]

Button(text='salvar', command=salvar).grid(row=2, column=0)



root.mainloop()