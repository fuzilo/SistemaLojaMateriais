from tkinter import *
from tkinter import messagebox
import subprocess

tela=Tk()
tela.title("Acesso ao Sistema")
tela.geometry("360x800")
tela.resizable(False,False)
largura =360
altura = 800


foto_acesso = PhotoImage(file=r"icon\acessar.png")
foto_sair = PhotoImage(file=r"icon\sair.png")
def sair():
    resposta = messagebox.askquestion("Sair do Sistema?", "Você tem certeza que deseja sair?")
    if resposta =='yes':
        tela.destroy()


def validar_acesso(usuario, senha):
    if usuario == 'admin' and senha =='123':
        abrir_app()
        
    else:
        messagebox.showerror("Erro de Login", "Usuário ou senha incorretos.")    
        
def abrir_app():
    tela.destroy()
    subprocess.run(["python","sistemaCelular.py"])   
            
def click_botao():
    usuario = txt_usuario.get()
    senha = txt_senha.get()
    validar_acesso(usuario, senha)




lbl_usuario= Label(tela, text="Usuário").place (x=50, y=340)
lbl_senha = Label(tela, text="Senha").place(x=50, y= 400)


txt_usuario = Entry(tela, width=20)
txt_usuario.place(x=100, y=340)
txt_senha = Entry(tela,width=20, show="*")
txt_senha.place(x=100, y=400)

btn_usuario = Button(tela, text="Acessar", image=foto_acesso, compound =TOP, command=click_botao)
btn_usuario.place(x=250, y=650)

btn_sair = Button(tela, text="Sair", image = foto_sair, compound=TOP, command=sair)
btn_sair.place(x=50, y= 650)

largura_screen = tela.winfo_screenwidth()
altura_screen= tela.winfo_screenheight()
posx= largura_screen /2 - largura / 2
posy= altura_screen /2 - altura /2
tela.geometry("%dx%d+%d+%d" % (largura,altura,posx,posy))

tela.mainloop()





