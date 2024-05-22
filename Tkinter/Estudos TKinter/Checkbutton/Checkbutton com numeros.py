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

    total += int(varnumero.get())
    print(valorantigo, "+", varnumero.get(), "=", total)


varnumero = IntVar()

checknumero5 = Checkbutton(janela, text="5",
                        font="Arial 20",
                        variable=varnumero,
                        onvalue=5,
                        offvalue=0,
                        command=funcaosomar).pack()

checknumero10= Checkbutton(janela, text="10",
                        font="Arial 20",
                        variable=varnumero,
                        onvalue=10,
                        offvalue=0,
                        command=funcaosomar).pack()


checknumero15 = Checkbutton(janela, text="15",
                        font="Arial 20",
                        variable=varnumero,
                        onvalue=15,
                        offvalue=0,
                        command=funcaosomar).pack()




#mainloop - no tkinter uma janela funciona como um loop infinito
janela.mainloop()