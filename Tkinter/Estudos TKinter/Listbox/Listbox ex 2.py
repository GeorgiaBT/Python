from  tkinter import Tk
from tkinter import *
from tkinter import messagebox
#Tk - janela
janela = Tk()

janela.geometry("400x400")

janela.title("Listbox")

labelinstrucao = Label(janela,
                       text="Dia da Semana",
                       font="Arial 26").pack()

listanomes = ("Ana", "Amanda", "Cesar", "Pedro", "Allan", "Carlos", "Marcos", "Roger", "Emile")

variavelnomes = Variable(value=listanomes)
#cira listbox
listbox = Listbox(janela,
                  font="Arial 20",
                  listvariable= variavelnomes,
                  selectmode=MULTIPLE) #selectmode - SINGLE permite uma simples selecao
#selectmode=SINGLE, BROWSE, MULTIPLE, EXTENDED

listbox.pack(expand=True, fill=BOTH) #expandir a listbox para ocupar toda a tela

def itemselecionado(evento):

    #retornar todos os indices/posicoes selecionadas
    indiceselecionado = listbox.curselection()

    #join junta todos os itens que estão selecionados
    item = ",".join([listbox.get(posicao) for posicao in indiceselecionado])
    mensagem = "Você selecionou: " + item
    messagebox.showinfo(title="Atenção!", message=mensagem)
    print(mensagem)

#criando um evento de clique para pegar a posicao do item selecionado
listbox.bind("<<ListboxSelect>>", itemselecionado)

textoparaadicionar = Entry(font="Arial 26")
textoparaadicionar.pack()

def addItem():

    listbox.insert(END, str(textoparaadicionar.get()))

botaoadicionar = Button(text="Adicionar texto",
                        font="Arial 30",
                        command=addItem).pack()

#mainloop - no tkinter uma janela funciona como um loop infinito
janela.mainloop()