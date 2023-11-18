from tkinter import *
from tkinter import ttk
import tkinter as tk
import pymongo


tela = Tk()
tela.title("Sistema de Vendas - Loja de Materiais")
tela.geometry("800x600")
tela.resizable(True,True)
tela.configura(background="#ffffff")

exemplo = pymongo.MongoClient("mongodb://localhost:27017/")
db=exemplo["exemplo"]
collection = db["clientes"]

#Cadastro de Clientes
lbl_titulo = Label(tela, text="Cadastro de Clientes", font=("Arial", 30,"bold"),bg="#ffffff").place(x=200,y=50)

lbl_codigo = Label(tela, text="Código:", bg="#ffffff").place(x=130,y=140)
txt_codigo=Entry(tela, width=20,borderwidth=2,fg="black",bg="white")
txt_codigo.place(x=190, y=140)

lbl_nome = Label(tela, text="Nome:", bg="#ffffff").place(x=130,y=170)
txt_nome=Entry(tela, width=40,borderwidth=2,fg="black",bg="white")
txt_nome.place(x=190, y=170)
txt_nome.insert(0,"")

lbl_cpf = Label(tela, text="CPF:", bg="#ffffff").place(x=450,y=170)
txt_cpf=Entry(tela, width=20,borderwidth=2,fg="black",bg="white")
txt_cpf.place(x=480, y=170)
txt_cpf.insert(0,"")

lbl_idade = Label(tela, text="Idade:", bg="#ffffff").place(x=130,y=200)
txt_idade=Entry(tela, width=20,borderwidth=2,fg="black",bg="white")
txt_idade.place(x=190, y=200)
txt_idade.insert(0,"")

lbl_end = Label(tela, text="Rua:", bg="#ffffff").place(x=130,y=200)
txt_end=Entry(tela, width=25,borderwidth=2,fg="black",bg="white")
txt_end.place(x=480, y=200)
txt_end.insert(0,"")

lbl_bairro = Label(tela, text="Bairro:", bg="#ffffff").place(x=130,y=230)
txt_bairro=Entry(tela, width=20,borderwidth=2,fg="black",bg="white")
txt_bairro.place(x=190, y=230)
txt_bairro.insert(0,"")

lbl_estado = Label(tela, text="Estado:", bg="#ffffff").place(x=330,y=230)
comboestado = ttk.Combobox(tela,
                        values=[
                            "São Paulo",
                            "Rio de Janeiro",
                            "Minas Gerais",
                            "Espírito Santo"],)
comboestado.grid(column=0, row=1)
comboestado.place(x=370, y=230)

lbl_cidade = Label(tela, text="Cidade:", bg="#ffffff").place(x=520,y=230)
txt_cidade=Entry(tela, width=20,borderwidth=2,fg="black",bg="white")
txt_cidade.place(x=570, y=230)
txt_cidade.insert(0,"")

def salvar():
    codigo=txt_codigo.get()
    nome = txt_nome.get()
    idade = int(txt_idade.get())
    end = txt_end.get()
    cpf = txt_cpf.get()
    bairro = txt_bairro.get()
    cidade = txt_cidade.get()
    estado = comboestado.get()

    #Apagar os dados nas caixas
    txt_codigo.delete(0, tk.END)
    txt_nome.delete(0, tk.END)
    txt_idade.delete(0, tk.END)
    txt_end.delete(0, tk.END)
    txt_bairro.delete(0, tk.END)
    txt_cidade.delete(0, tk.END)
    comboestado.set("")
    txt_cpf.delete(0, tk.END)

    cliente = {"código":codigo, "nome":nome, "idade":idade, "endereço": end, "cpf":cpf, "bairro":bairro, "cidade":cidade, "estado":estado}
    collection.insert_one(cliente)

def atualizar():
    codigo=txt_codigo.get()
    nome = txt_nome.get()
    idade = int(txt_idade.get())
    end = txt_end.get()
    cpf = txt_cpf.get()
    bairro = txt_bairro.get()
    cidade = txt_cidade.get()
    estado = comboestado.get()

    collection.update_one({"código":codigo}, {"$set":{
                                        "código":codigo, "nome":nome,"idade":idade, "endereço":end, "cpf":cpf, "bairro":bairro, "estado":estado}})
    
def apagar():
    codigo = txt_codigo.get()
    collection.delete_one({"código":codigo})

btn_salvar = Button    