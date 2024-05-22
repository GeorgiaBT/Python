from  tkinter import Tk
from tkinter import *

#Tk - janela
#lambda permite enviar varios dados em uma funcao
#sticky estica/preenche as laterais
#grid divide a tela em partes/grades
#columnspam colocamos para dizer quantas colunas do grid o item vai ocupar
janela = Tk()

janela.title("Calculadora")

janela.geometry("345x340")

def enviarnumeropara(char):

    global calculooperacoes
    calculooperacoes += str(char)
    textodeentrada.set(calculooperacoes)

def deletarnumero():

    global calculooperacoes

    textosemultimodigito = calculooperacoes[:-1] #exclui o ultimo digito
    calculooperacoes = textosemultimodigito

    textodeentrada.set(calculooperacoes)

def limpartudo():

    global calculooperacoes

    calculooperacoes = ""
    textodeentrada.set((calculooperacoes))

def funcaoresultado():

    global calculooperacoes

    resultadocalculo = str(eval(calculooperacoes))
    #eval avalia se é um calculo valido e efetua o calculo
    textodeentrada.set(resultadocalculo)

    calculooperacoes = resultadocalculo


calculooperacoes = ""
textodeentrada = StringVar()

exibiroperacoesresult = Entry(janela, font="Arial 20 bold",
                              textvariable= textodeentrada,
                              border= 5,
                              bg = "#BBB",
                              fg= "black"
                              ).grid(row=1, columns=5, padx=10, pady=15)

botao7 = Button(janela,
                text=7,
                border=5,
                fg="white",
                bg="pink",
                font=("Arial 20 bold"),
                command= lambda: enviarnumeropara("7")).grid(row=2, column=0, sticky="NSEW")

botao8 = Button(janela,
                text=8,
                border=5,
                fg="white",
                bg="pink",
                font=("Arial 20 bold"),
                command= lambda: enviarnumeropara("8")).grid(row=2, column=1, sticky="NSEW")

botao9 = Button(janela,
                text=9,
                border=5,
                fg="white",
                bg="pink",
                font=("Arial 20 bold"),
                command= lambda: enviarnumeropara("9")).grid(row=2, column=2, sticky="NSEW")

botaodel = Button(janela,
                text="DEL",
                border=5,
                fg="white",
                bg="#C08B9C",
                font=("Arial 20 bold"),
                command= deletarnumero).grid(row=2, column=3, sticky="NSEW")

botaoac = Button(janela,
                text="AC",
                border=5,
                fg="white",
                bg="#C08B9C",
                font=("Arial 20 bold"),
                command= limpartudo).grid(row=2, column=4, sticky="NSEW")

botao4 = Button(janela,
                text=4,
                border=5,
                fg="white",
                bg="pink",
                font=("Arial 20 bold"),
                command= lambda: enviarnumeropara("4")).grid(row=3, column=0, sticky="NSEW")

botao5 = Button(janela,
                text=5,
                border=5,
                fg="white",
                bg="pink",
                font=("Arial 20 bold"),
                command= lambda: enviarnumeropara("5")).grid(row=3, column=1, sticky="NSEW")

botao6 = Button(janela,
                text=6,
                border=5,
                fg="white",
                bg="pink",
                font=("Arial 20 bold"),
                command= lambda: enviarnumeropara("6")).grid(row=3, column=2, sticky="NSEW")


botaosoma = Button(janela,
                text="+",
                border=5,
                fg="white",
                bg="pink",
                font=("Arial 20 bold"),
                command= lambda: enviarnumeropara("+")).grid(row=4, column=3, sticky="NSEW")

botaosubtrai = Button(janela,
                text="-",
                border=5,
                fg="white",
                bg="pink",
                font=("Arial 20 bold"),
                command= lambda: enviarnumeropara("-")).grid(row=4, column=4, sticky="NSEW")

botaomultiplica = Button(janela,
                text="*",
                border=5,
                fg="white",
                bg="pink",
                font=("Arial 20 bold"),
                command= lambda: enviarnumeropara("*")).grid(row=3, column=3, sticky="NSEW")

botaodivide = Button(janela,
                text="/",
                border=5,
                fg="white",
                bg="pink",
                font=("Arial 20 bold"),
                command= lambda: enviarnumeropara("/")).grid(row=3, column=4, sticky="NSEW")

botaoresultado = Button(janela,
                text="=",
                border=5,
                fg="white",
                bg="pink",
                font=("Arial 20 bold"),
                command=funcaoresultado).grid(row=5, column=2 ,columnspan=3, sticky="NSEW")



botao3 = Button(janela,
                text=3,
                border=5,
                fg="white",
                bg="pink",
                font=("Arial 20 bold"),
                command= lambda: enviarnumeropara("3")).grid(row=4, column=0, sticky="NSEW")

botao2 = Button(janela,
                text=2,
                border=5,
                fg="white",
                bg="pink",
                font=("Arial 20 bold"),
                command= lambda: enviarnumeropara("2")).grid(row=4, column=1, sticky="NSEW")

botao1 = Button(janela,
                text=1,
                border=5,
                fg="white",
                bg="pink",
                font=("Arial 20 bold"),
                command= lambda: enviarnumeropara("1")).grid(row=4, column=2, sticky="NSEW")

botao0 = Button(janela,
                text=0,
                border=5,
                fg="white",
                bg="pink",
                font=("Arial 20 bold"),
                command= lambda: enviarnumeropara("0")).grid(row=5, column=0, sticky="NSEW")

botaoponto = Button(janela,
                text=".",
                border=5,
                fg="white",
                bg="pink",
                font=("Arial 20 bold"),
                command= lambda: enviarnumeropara(".")).grid(row=5, column=1, sticky="NSEW")








#mainloop - no tkinter uma janela funciona como um loop infinito
janela.mainloop()