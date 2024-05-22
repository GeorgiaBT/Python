from  tkinter import Tk
from tkinter import *
from tkinter import messagebox

#Tk - janela
janela = Tk()

janela.geometry("400x400")

janela.title("Messagebox")

def mensageminformacao():
    messagebox.showinfo("Informação", "Bem-vindo(a) ao curso de Tkiner!")

def mensagemaviso():
    messagebox.showwarning("Aviso", "Você está usando Tkinter.")

def mensagemerro():
    messagebox.showerror("Erro", "Erro ao carregar o sistema")

def mensagemquestao():

   resultado= messagebox.askquestion("Deletar", "Tem certeza que deseja deletar?")

   if resultado == "yes":
       print("Deletado com sucesso!")
   else:
       print("Cancelado com sucesso!")

def mensagemcancel():

    resultado = messagebox.askokcancel("Ok ou Cancelar", "Deseja continuar?")

    if resultado:
        print("Continuando...")
    else:
        print("Cancelado com sucesso!")
def mensagemsimnao():

    resultado = messagebox.askyesno("Sim ou Não", "Quer procurar o valor?")

    if resultado:
        print("Procurando...")
    else:
        print("Cancelado com sucesso!")
def mensagemretry():

    resultado = messagebox.askretrycancel("Repetir ou Cancelar", "Quer tentar novamente?")

    if resultado:
        print("Repetindo...")
    else:
        print("Cancelado com sucesso!")

botaoinformacao = Button(janela,
                         text="Informação",
                         font="Arial 20",
                         command=mensageminformacao).pack()

botaoaviso = Button(janela,
                         text="Aviso",
                         font="Arial 20",
                         command=mensagemaviso).pack()


botaoerro = Button(janela,
                         text="Erro",
                         font="Arial 20",
                         command=mensagemerro).pack()

botaoquestao = Button(janela,
                         text="Questão",
                         font="Arial 20",
                         command=mensagemquestao).pack()

botaocancel = Button(janela,
                         text="Ok ou Cancelar",
                         font="Arial 20",
                         command=mensagemcancel).pack()

botaosimnao = Button(janela,
                         text="SIm ou Não",
                         font="Arial 20",
                         command=mensagemsimnao).pack()

botaoretry = Button(janela,
                         text="Repetir ou Cancelar",
                         font="Arial 20",
                         command=mensagemretry).pack()



#mainloop - no tkinter uma janela funciona como um loop infinito
janela.mainloop()