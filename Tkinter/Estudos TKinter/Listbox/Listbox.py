from  tkinter import Tk
from tkinter import *

#Tk - janela
janela = Tk()

janela.geometry("400x400")

janela.title("Listbox")

labelinstrucao = Label(janela,
                       text="Dia da Semana",
                       font="Arial 26").pack()
#cira listbox
listbox = Listbox(janela, font="Arial 20")

#popula as informacoes na listbox
listbox.insert(1, "Domingo")
listbox.insert(2, "Segunda-feira")
listbox.insert(3, "Terça-feira")
listbox.insert(4, "Quarta-feira")
listbox.insert(5, "Quinta-feira")
listbox.insert(6, "Sexta-feira")
listbox.insert(7, "Sábado")

listbox.pack()

#mainloop - no tkinter uma janela funciona como um loop infinito
janela.mainloop()