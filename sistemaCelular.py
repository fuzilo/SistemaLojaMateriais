
from tkinter import *
from tkinter import ttk
import tkinter as tk
import pymongo



tela = Tk()
tela.title("Sistema de Vendas - Loja de Materiais")
tela.geometry("360x800")
tela.resizable(True,True)
tela.configure(background="#ffffff")

exemplo = pymongo.MongoClient("mongodb://localhost:27017/")
db=exemplo["exemplo"]
collection = db["clientes"]

#Cadastro de Clientes
lbl_titulo = Label(tela, text="Contatos", font=("Arial", 30, "bold"), bg="#ffffff")
lbl_titulo.place(x=20, y=50)

txt_codigo = Entry(tela, width=20, borderwidth=2, fg="black", bg="white")
txt_codigo.place(x=40, y=160)
lbl_codigo = Label(tela, text="Código:", bg="#ffffff")
lbl_codigo.place(x=40, y=182)

txt_nome = Entry(tela, width=40, borderwidth=2, fg="black", bg="white")
txt_nome.place(x=40, y=220)
txt_nome.insert(0, "")
lbl_nome = Label(tela, text="Nome:", bg="#ffffff")
lbl_nome.place(x=40, y=242)

txt_numero1 = Entry(tela, width=20, borderwidth=2, fg="black", bg="white")
txt_numero1.place(x=40, y=280)
txt_numero1.insert(0, "")
lbl_numero1 = Label(tela, text="Celular:", bg="#ffffff")
lbl_numero1.place(x=40, y=302)

txt_numero2 = Entry(tela, width=25, borderwidth=2, fg="black", bg="white")
txt_numero2.place(x=40, y=340)
txt_numero2.insert(0, "")
lbl_numero2 = Label(tela, text="Residencial:", bg="#ffffff")
lbl_numero2.place(x=40, y=362)

txt_email = Entry(tela, width=20, borderwidth=2, fg="black", bg="white")
txt_email.place(x=40, y=400)
txt_email.insert(0, "")
lbl_email = Label(tela, text="E-mail:", bg="#ffffff")
lbl_email.place(x=40, y=422)

txt_pais = Entry(tela, width=20, borderwidth=2, fg="black", bg="white")
txt_pais.place(x=40, y=460)
txt_pais.insert(0, "")
lbl_pais = Label(tela, text="País:", bg="#ffffff")
lbl_pais.place(x=40, y=482)

comboestado = ttk.Combobox(tela, values=["São Paulo", "Rio de Janeiro", "Minas Gerais", "Espírito Santo"])
comboestado.place(x=40, y=520)
lbl_estado = Label(tela, text="Estado:", bg="#ffffff")
lbl_estado.place(x=40, y=542)


txt_cidade = Entry(tela, width=20, borderwidth=2, fg="black", bg="white")
txt_cidade.place(x=40, y=580)
txt_cidade.insert(0, "")
lbl_cidade = Label(tela, text="Cidade:", bg="#ffffff")
lbl_cidade.place(x=40, y=602)

def salvar():
    codigo=txt_codigo.get()
    nome = txt_nome.get()
    numero1 = int(txt_numero1.get())
    numero2 = int(txt_numero2.get())
    email = txt_email.get()
    pais = txt_pais.get()
    cidade = txt_cidade.get()
    estado = comboestado.get()

    #Apagar os dados nas caixas
    txt_codigo.delete(0, tk.END)
    txt_nome.delete(0, tk.END)
    txt_numero1.delete(0, tk.END)
    txt_numero2.delete(0, tk.END)
    txt_email.delete(0, tk.END)
    txt_pais.delete(0, tk.END)
    txt_cidade.delete(0, tk.END)
    comboestado.set("")
    

    contato = {"código":codigo, "nome":nome, "celular":numero1, "residencial": numero2, "país":pais, "email":email, "cidade":cidade, "estado":estado}
    collection.insert_one(contato)

def atualizar():
    codigo=txt_codigo.get()
    nome = txt_nome.get()
    numero1 = int(txt_numero1.get())
    numero2 = int(txt_numero2.get())
    email = txt_email.get()
    pais = txt_pais.get()
    cidade = txt_cidade.get()
    estado = comboestado.get()

    collection.update_one({"código":codigo}, {"$set":{
                                        "código":codigo, "nome":nome,"celular":numero1, "residencial":numero2, "email":email, "país":pais, "estado":estado,
                                        "cidade":cidade}})
    
def apagar():
    codigo = txt_codigo.get()
    collection.delete_one({"código":codigo})

def consultar():
    codigo= txt_codigo.get()
    resultado = collection.find_one({"código":codigo})
    if resultado:
        txt_nome.insert(END, f"{resultado['nome']}\n")
        txt_numero1.insert(END, f"{resultado['celular']}\n")
        txt_numero2.insert(END, f"{resultado['residencial']}\n")
        txt_email.insert(END, f"{resultado['email']}\n")
        txt_pais.insert(END, f"{resultado['país']}\n")
        txt_cidade.insert(END, f"{resultado['cidade']}\n")
        comboestado.insert(END, f"{resultado['estado']}\n")
    else:
        lbl_resultado.config(text="Nenhum resultado encontrado")    

#Importação de icones
foto_salvar = PhotoImage(file=r"icon\salvar.png")
foto_excluir = PhotoImage(file=r"icon\excluir.png")
foto_alterar = PhotoImage(file=r"icon\alterar.png")
foto_consultar = PhotoImage(file=r"icon\consultar.png")
foto_sair = PhotoImage(file=r"icon\sair.png")


btn_salvar = Button (tela, text="Salvar", image = foto_salvar, width=60,height=60,  compound =TOP,command=salvar).place(x=280,y=680)
btn_consultar = Button(tela, text="Consultar",image=foto_consultar,width=60,height=60,compound =TOP,command=consultar).place(x=156,y=680)
btn_excluir = Button (tela, text="Excluir",image=foto_excluir,width=60,height=60, compound =TOP,command=apagar).place(x=200,y=70)
btn_atualizar = Button (tela, text="Atualizar",image=foto_alterar, width=60,height=60, compound =TOP,command=atualizar).place(x=280,y=70)


tela.mainloop()