from  tkinter import Tk
from tkinter import *
from tkinter import messagebox

#Tk - janela
janela = Tk()

janela.geometry("400x400")

#Label - é onde escrevemos os textos que serão exibidos na tela
instrucao = Label(text="\nBem vindos ao curso de Tkinter!\n", font="Arial 40")
#pack  coloca os objetos dentro da tela. Cria e centraliza e deixa um em baixo do outro
instrucao.pack()

janela.title("Interface Gráfica - Button")

botao = Button(janela, text="Enviar", font="Arial 40")
botao.pack()
 #def metodo para exibir a mensagem
def exibirmensagem():
    messagebox.showinfo("Mensagem",
                        "Olá, mundo")

botaoolamundo = Button(janela, text="Mensagem",
                       font="Arial 40",
                       command= exibirmensagem)
botaoolamundo.pack()

botaosair = Button(janela, text="Sair",
                       font="Arial 40",
                       command= janela.destroy) #fechar a tela do tkinter
botaosair.pack()

botaoverde = Button(janela, text="VERDE",
                    font="Arial 40",
                    fg= "white",
                    bg= "green")
botaoverde.pack()

botaoamarelo = Button(janela, text="AMARELO",
                    font="Arial 40",
                    fg= "black",
                    bg= "yellow")
botaoamarelo.pack()


#mainloop - no tkinter uma janela funciona como um loop infinito
janela.mainloop()