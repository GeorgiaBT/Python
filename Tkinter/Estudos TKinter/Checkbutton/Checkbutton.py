from  tkinter import Tk
from tkinter import *
from tkinter import messagebox

#Tk - janela
janela = Tk()

janela.geometry("400x400")


janela.title("Checkbutton")

labelinformacao = Label(janela, text="Selecione a opção desejada",
                        fg= "Blue",
                        font="Arial 20").pack()

def funcaoazulclica():

    messagebox.showinfo("Mensagem", varazul.get())

varazul = StringVar()
varamarelo = StringVar()
varverde = StringVar()

checkazul = Checkbutton(janela, text="Azul",
                        font="Arial 20",
                        variable=varazul,
                        onvalue="Clicou na cor azul",
                        offvalue="",
                        command=funcaoazulclica).pack()

def funcaoamareloclica():

    messagebox.showinfo("Mensagem", varamarelo.get())

checkamarelo = Checkbutton(janela, text="Amarelo",
                        font="Arial 20",
                        variable=varamarelo,
                        onvalue="Clicou na cor amarela",
                        offvalue="",
                        command=funcaoamareloclica).pack()


def funcaoverdeclica():
    messagebox.showinfo("Mensagem", varverde.get())

checkverde = Checkbutton(janela, text="Verde",
                        font="Arial 20",
                        variable=varverde,
                        onvalue="Clicou na cor verde",
                        offvalue="",
                        command=funcaoverdeclica).pack()




#mainloop - no tkinter uma janela funciona como um loop infinito
janela.mainloop()