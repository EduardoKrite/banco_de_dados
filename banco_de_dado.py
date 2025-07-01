import tkinter  
from tkinter import messagebox  
import sqlite3 
import os


def criar_tabela():
    conexao = sqlite3.connect("cadastro.db")
    cursor = conexao.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tb_contatos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        T_NOMECONTATOS TEXT NOT NULL,
        T_TELEFONECONTATOS TEXT,
        T_EMAILCONTATOS TEXT,
        T_OBS TEXT
    )
    """)
    conexao.commit()
    conexao.close()
#  Criar  um site

app = tkinter.Tk()
app.title("Cadastro de um site")
app.geometry("500x500")

#texto de boas vindas
bem_vindo = tkinter.Label(app, text="Castraste o seu perfil", font=("Arial", 30))
bem_vindo.pack()
    
# Salvar em uma pagina 
def sal_pag():
    if tb_nome.get() != "":
        vnome=tb_nome.get()   
        vtelefone= tb_telefone.get()
        vemail=tb_email.get()
        vobs = tb_obs.get("1.0",tkinter.END)
        vquery = "INSERT INTO tb_contatos(T_NOMECONTATOS,T_TELEFONECONTATOS,T_EMAILCONTATOS,T_OBS)VALUES('"+vnome+"','"+vtelefone+"','"+vemail+"', '"+vobs+"')"
        

        print ("Dados Enviados")
    else:
        print("Erro")   

  
    
def limpar():
    tb_nome.delete(0,tkinter.END)
    tb_email.delete(0,tkinter.END)
    tb_telefone.delete(0,tkinter.END)
    tb_obs.delete("1.0", tkinter.END)



tb_nome = tkinter.Label(app, text="Nome:", font=("Arial",10))
tb_nome.place( x=30, y=60)
tb_nome = tkinter.Entry(app, width=70)
tb_nome.place(x=30, y=80)

tb_email = tkinter.Label(app, text="Email:", font=("Arial",10))
tb_email.place(x=30, y=110)
tb_email= tkinter.Entry(app, width=70)
tb_email.place(x=30, y=130)

tb_telefone = tkinter.Label(app, text="Telefone:", font=("Arial",10))
tb_telefone.place(x=30, y=160)
tb_telefone = tkinter.Entry(app, width=70)
tb_telefone.place(x=30, y=180)

tb_obs = tkinter.Label(app, text="Observação:", font=("Arial",10))
tb_obs.place(x=30, y=210)
tb_obs = tkinter.Text(app, width=53, height=10)
tb_obs.place(x=30, y=230)

vbotao = tkinter.Button(app, text="Salvar ", command=sal_pag, width=20, height=2)
vbotao.place(x=30, y=420)

vbotao_limpar = tkinter.Button(app, text="Limpar", command=limpar, width=20, height=2)
vbotao_limpar.place(x=300, y=420)

    



app.mainloop()
