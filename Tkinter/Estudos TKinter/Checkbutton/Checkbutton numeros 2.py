from  tkinter import Tk
from tkinter import *
from tkinter import messagebox

#Tk - janela
janela = Tk()

janela.geometry("400x400")


janela.title("Checkbutton com numeros")

labelinformacao = Label(janela, text="Selecione a opção desejada",
                        fg= "Blue",
                        font="Arial 20").pack()

total = 0
valorantigo = 0
def funcaosomar():

    global total
    global valorantigo

    valorantigo = total

    total += int(varnumero5.get()) + int(varnumero10.get()) + int(varnumero15.get())

    print(valorantigo, ":", total)


varnumero5 = IntVar()
varnumero10 = IntVar()
varnumero15 = IntVar()

checknumero5 = Checkbutton(janela, text="Numero 5",
                        font="Arial 20",
                        variable=varnumero5,
                        onvalue=5,
                        offvalue=0,
                        command=funcaosomar).pack()

checknumero10 = Checkbutton(janela, text="Numero 10",
                        font="Arial 20",
                        variable=varnumero10,
                        onvalue=10,
                        offvalue=0,
                        command=funcaosomar).pack()

checknumero15 = Checkbutton(janela, text="Numero 15",
                        font="Arial 20",
                        variable=varnumero15,
                        onvalue=15,
                        offvalue=0,
                        command=funcaosomar).pack()

#mainloop - no tkinter uma janela funciona como um loop infinito
janela.mainloop()