from  tkinter import Tk
from tkinter import *
from tkinter import messagebox

#Tk - janela
janela = Tk()

janela.geometry("400x400")

janela.title("Messagebox")

messagebox.showinfo("Informação", "Bem-vindo(a) ao curso de Tkiner!")
messagebox.showwarning("Aviso", "Você está usando Tkinter.")
messagebox.showerror("Erro", "Erro ao carregar o sistema")
messagebox.askquestion("Questão", "Tkinter é com python?")
messagebox.askokcancel("Ok ou Cancelar", "Deseja continuar?")
messagebox.askyesno("Sim ou Não", "Quer procurar o valor?")
messagebox.askretrycancel("Repetir ou Cancelar", "QUer tentar novamente?")

#mainloop - no tkinter uma janela funciona como um loop infinito
janela.mainloop()