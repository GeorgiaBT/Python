from  tkinter import Tk
from tkinter import *

#Tk - janela
janela = Tk()

janela.geometry("400x400")

def imprimiritemselecionado():
    print("Você selecionou a letra: " + variavelopcaoselecionada.get())

variavelopcaoselecionada = StringVar(janela, "0")

opcoes = {"Letra A": "A",
        "Letra B": "B",
        "Letra C": "C",
        "Letra D": "D",
        "Letra E": "E",
        "Letra F": "F",
        "Letra G": "G",
        "Letra H": "H",
        "Letra I": "I",
        "Letra J": "J",
        "Letra K": "K"
}

for (textocoluna0, textocoluna1) in opcoes.items():
    Radiobutton(janela,
                text=textocoluna0,
                font="Arial 26",
                value=textocoluna1,
                variable=variavelopcaoselecionada,
                command=imprimiritemselecionado).pack()

janela.title("Radiobutton exemplo 2")

#mainloop - no tkinter uma janela funciona como um loop infinito
janela.mainloop()