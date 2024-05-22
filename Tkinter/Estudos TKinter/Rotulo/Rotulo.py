from  tkinter import Tk
from tkinter import *

#Tk - janela
janela = Tk()

janela.geometry("900x900")

#Label - é onde escrevemos os textos que serão exibidos na tela
#foregroud = cor do texto
#background = cor do fundo
#relief = borda decorativa. FLAT, RAISED, SUNKEN, GROOVE, RIDGE
rotulo1 = Label(janela,text="\nPython", relief=FLAT, background="pink", foreground="white", font="Arial 40")
rotulo2 = Label(janela,text="\nPython", relief=RAISED, background="red", foreground="white", font="Arial 40")
rotulo3 = Label(janela,text="\nPython", relief=SUNKEN, background="purple", foreground="white", font="Arial 40")
rotulo4 = Label(janela,text="\nPython", relief=GROOVE, background="blue", foreground="white", font="Arial 40")
rotulo5 = Label(janela,text="\nPython", relief=RIDGE, background="green", foreground="white", font="Arial 40")
#pack  coloca os objetos dentro da tela. Cria e centraliza e deixa um em baixo do outro
rotulo1.pack()
rotulo2.pack()
rotulo3.pack()
rotulo4.pack()
rotulo5.pack()

texto =  """Curso de Tkinter
Aprendendo a criar
Interface gráfica com
Python.
"""

rotulo6 = Label(janela,
                font="Arial 40 bold",
                text= texto
                )

rotulo6.pack()

#Label - é onde escrevemos os textos que serão exibidos na tela
rotulo1 = Label(text="\nCurso de Tkinter\n", font="Arial 40")
#pack  coloca os objetos dentro da tela. Cria e centraliza e deixa um em baixo do outro
rotulo1.pack()

janela.title("Interface Gráfica")

#mainloop - no tkinter uma janela funciona como um loop infinito
janela.mainloop()