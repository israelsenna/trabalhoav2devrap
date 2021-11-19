import tkinter as tk

import sqlite3

conn = sqlite3.connect("trabalhoav2/cad_e_consul.db")
cursor = conn.cursor()

def mostrar_alunos():
    print("Nome: %s\nMatricula: %s\nAv1: %s\nAv2: %s\nAv3: %s\nAvd: %s\nAvds: %s\nE-mail: %s\nEndereço: %s\nCampus: %s\nPeríodo: %s\n" % (e1.get(), e2.get(), e3.get(), e4.get(), e5.get(), e6.get(), e7.get(), e8.get(), e9.get(), e10.get(), e11.get()))

def exibir_dados():
    cursor.execute('''SELECT * FROM cad_e_consul''')
    for linha in cursor:
        print(linha)
    conn.close()

def salvar_alunos():
    import trabalhoav2 

janela = tk.Tk()
janela.title("CADASTRO ALUNO")
tk.Label(janela, text="Nome").grid(row=0)
tk.Label(janela, text="Matricula").grid(row=1)
tk.Label(janela, text="Av1").grid(row=2)
tk.Label(janela, text="Av2").grid(row=3)
tk.Label(janela, text="Av3").grid(row=4)
tk.Label(janela, text="Avd").grid(row=5)
tk.Label(janela, text="Avds").grid(row=6)
tk.Label(janela, text="E-mail").grid(row=7)
tk.Label(janela, text="Endereço").grid(row=8)
tk.Label(janela, text="Campus").grid(row=9)
tk.Label(janela, text="Período").grid(row=10)


e1 = tk.Entry(janela)
e2 = tk.Entry(janela)
e3 = tk.Entry(janela)
e4 = tk.Entry(janela)
e5 = tk.Entry(janela)
e6 = tk.Entry(janela)
e7 = tk.Entry(janela)
e8 = tk.Entry(janela)
e9 = tk.Entry(janela)
e10 = tk.Entry(janela)
e11 = tk.Entry(janela)

e1.grid(row=0, column=2)
e2.grid(row=1, column=2)
e3.grid(row=2, column=2)
e4.grid(row=3, column=2)
e5.grid(row=4, column=2)
e6.grid(row=5, column=2)
e7.grid(row=6, column=2)
e8.grid(row=7, column=2)
e9.grid(row=8, column=2)
e10.grid(row=9, column=2)
e11.grid(row=10, column=2)

tk.Button(janela, text='Sair',
    command=janela.quit).grid(row=12,
    column=1,
    sticky=tk.W,
    pady=4)

#tk.Button(janela, text='Exibir Dados do Aluno', command=mostrar_alunos).grid(row=12,
 #   column=2,
  #  sticky=tk.W,
   # pady=4)

tk.Button(janela, text='Exibir Dados do Aluno', command=exibir_dados).grid(row=12,
    column=2,
    sticky=tk.W,
    pady=4)

tk.Button(janela, text='Salvar Dados do Aluno', command=salvar_alunos).grid(row=12,
    column=4,
    sticky=tk.W,
    pady=4)

tk.mainloop()