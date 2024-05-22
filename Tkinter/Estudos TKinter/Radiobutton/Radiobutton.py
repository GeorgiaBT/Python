from  tkinter import Tk
from tkinter import *

#Tk - janela
janela = Tk()

janela.geometry("400x400")

def imprimiritemselecionado():
    print("Você selecionou a letra: " + variavelopcaoselecionada.get())

variavelopcaoselecionada = StringVar(janela, "0")

radiobutton1 = Radiobutton(janela,
                           text="Letra A",
                           font="Arial 26",
                           value= "A",
                           variable=variavelopcaoselecionada,
                           command= imprimiritemselecionado).pack()

radiobutton2 = Radiobutton(janela,
                           text="Letra B",
                           font="Arial 26",
                           value= "B",
                           variable=variavelopcaoselecionada,
                           command= imprimiritemselecionado).pack()


radiobutton3 = Radiobutton(janela,
                           text="Letra C",
                           font="Arial 26",
                           value= "C",
                           variable=variavelopcaoselecionada,
                           command= imprimiritemselecionado).pack()

janela.title("Radiobutton exemplo 1")

#mainloop - no tkinter uma janela funciona como um loop infinito
janela.mainloop()