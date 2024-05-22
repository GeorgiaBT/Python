from  tkinter import Tk
from tkinter import *
from tkinter import ttk
#Tk - janela
janela = Tk()

janela.geometry("400x400")

janela.title("Comboboc exemplo 1")

Label(janela, text="Selecione um mês:",
      font=("Arial 18")).grid(row=0, column=0)

messelecionado = ttk.Combobox(janela,
                              font="Arial 20")

messelecionado["values"] = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")

messelecionado.grid(row=0, column=1 )

messelecionado.current(10)

def itemselecionado():

      print(str(messelecionado.get()))

botaopegaitemselecionado = Button(janela,
                                  text="Item Selecionado",
                                  font="Arial 20",
                                  command=itemselecionado)

botaopegaitemselecionado.grid(row=1, column=0, columnspan=2, sticky="NSEW")
#mainloop - no tkinter uma janela funciona como um loop infinito
janela.mainloop()