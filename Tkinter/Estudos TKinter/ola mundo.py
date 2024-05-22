from  tkinter import Tk
from tkinter import *

#Tk - janela
janela = Tk()

janela.geometry("400x400")

#Label - é onde escrevemos os textos que serão exibidos na tela
instrucao = Label(text="\nBem vindos a minha primeira interface com Tkinter!\n", font="Arial 40")
#pack  coloca os objetos dentro da tela. Cria e centraliza e deixa um em baixo do outro
instrucao.pack()

janela.title("Interface Gráfica")

#mainloop - no tkinter uma janela funciona como um loop infinito
janela.mainloop()