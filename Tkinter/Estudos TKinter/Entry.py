from  tkinter import Tk
from tkinter import *

#Tk - janela
janela = Tk()

janela.geometry("900x600")

janela.title("Interface Gráfica")

#grid divide a tela em partes
#sticky usamos para preencher o item na tela toda, para não ficar espaços em branco nas laterais. è o NSEW(norte sul leste oeste)
#entry - campo de entrada de dados
nome = Label(text="Nome:",
             font="Arial 40")
nome.grid(row=1, column=0, sticky="W")

exibirnome = Entry(font="Arial 40")
exibirnome.grid(row=1, column=1, sticky="W")

sobrenome = Label(text="Sobrenome:",
             font="Arial 40")
sobrenome.grid(row=2, column=0, sticky="W")

exibirsobrenome = Entry(font="Arial 40")
exibirsobrenome.grid(row=2, column=1, sticky="W")


#mainloop - no tkinter uma janela funciona como um loop infinito
janela.mainloop()

