from tkinter import *
from tkinter import messagebox
import subprocess

tela=Tk()
tela.title("Acesso ao Sistema")
tela.geometry("360x800")
tela.resizable(False,False)
largura =360
altura = 800

barra_menus = Menu(tela)

opcoes_menus_arquivos = Menu(barra_menus)
opcoes_menus_gestao = Menu(barra_menus)
opcoes_novo=Menu(opcoes_menus_arquivos)

def sair():
    resposta = messagebox.askquestion("Sair do Sistema?", "Você tem certeza que deseja sair?")
    if resposta =="yes":
        tela.destroy()

def gerenciar_contatos():
    tela.destroy()
    subprocess.run(["python","sistemaCelular.py"])           

barra_menus.add_cascade(label="Arquivo", menu=opcoes_menus_arquivos)
barra_menus.add_cascade(label="Gestão", menu=opcoes_menus_gestao)

opcoes_menus_arquivos.add_cascade(label="Novo", menu=opcoes_novo)

opcoes_menus_arquivos.add_command(label="Abrir")
opcoes_menus_arquivos.add_command(label="Salvar")
opcoes_menus_arquivos.add_command(label="Salvar como...")
opcoes_menus_arquivos.add_separator()
opcoes_menus_arquivos.add_command(label="Sair", command=tela.quit)

barra_menus.add_cascade(label="Gestão", menu=opcoes_menus_gestao)
opcoes_novo.add_command(label="Salvar Imagens")
opcoes_novo.add_command(label="Carregar Imagens")

foto_logo = PhotoImage(file = r"icon\logo.png")
foto_usuarios = PhotoImage(file = r"icon\contatos.png")
foto_logout = PhotoImage(file = r"icon\sair.png")

btn_contatos = Button(tela, text="Contatos", image=foto_usuarios, compound=TOP,command=gerenciar_contatos).place(x=145, y=266)
btn_logout = Button(tela, text="Sair", image=foto_logout, compound=TOP, command=sair).place(x=145, y=366)

lbl_logo = Label(tela, text="SmartPhone", compound=TOP, image=foto_logo).place(x=145, y=680)
                       
                       






tela.config(menu=barra_menus)

tela.mainloop()
