from  tkinter import Tk
from tkinter import *

#Tk - janela
janela = Tk()

janela.geometry("400x400")

for linha in range(5):
    for coluna in range(3):

        tabela = Frame(
            master= janela,
            relief= RAISED,
            borderwidth= 1
        )
        tabela.grid(row= linha, column= coluna, padx=5, pady= 5)
        crialabel = Label(master= tabela,background="pink", foreground="white", text=f"Linha {linha} \n Coluna {coluna}")
        crialabel.pack()

janela.title("Interface Gráfica")

#mainloop - no tkinter uma janela funciona como um loop infinito
janela.mainloop()