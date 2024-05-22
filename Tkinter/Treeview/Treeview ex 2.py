#cadastrar itens
from  tkinter import Tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#Tk - janela
janela = Tk()

janela.geometry("900x400")

janela.title("Treeview exemplo 2")

id = Label(text="ID: ",
           font="Arial 12").grid(row=1, column=0, sticky="E")

exibirid = Entry(font="Arial 12")
exibirid.grid(row=1, column=1, sticky="W")

nome = Label(text="Nome: ",
           font="Arial 12").grid(row=1, column=2, sticky="E")

exibirnome = Entry(font="Arial 12")
exibirnome.grid(row=1, column=3, sticky="W")

idade = Label(text="Idade: ",
           font="Arial 12").grid(row=1, column=4, sticky="E")

exibiridade = Entry(font="Arial 12")
exibiridade.grid(row=1, column=5, sticky="W")

sexo = Label(text="Sexo: ",
           font="Arial 12").grid(row=1, column=6, sticky="E")

exibirsexo = Entry(font="Arial 12")
exibirsexo.grid(row=1, column=7, sticky="W")
def additemtreeview():

    if exibirid.get() == "":
        messagebox.showinfo("Atenção!", "Digite um ID")
    elif exibirnome.get() == "":
        messagebox.showinfo("Atenção!", "Digite o Nome")
    elif exibiridade.get() == "":
        messagebox.showinfo("Atenção!", "Digite a Idade")
    elif exibirsexo.get() == "":
        messagebox.showinfo("Atenção!", "Digite o Sexo")
    else:
        treeviewdados.insert("", "end",
                             values=(str(exibirid.get()),
                                     str(exibirnome.get()),
                                     str(exibiridade.get()),
                                     str(exibirsexo.get())))
        exibirid.delete(0, "end")
        exibirnome.delete(0, "end")
        exibiridade.delete(0, "end")
        exibirsexo.delete(0, "end")


botaoadicionar = Button(text="Cadastrar",
                        font="Arial 20",
                        command= additemtreeview)

botaoadicionar.grid(row=2, column=0, columnspan=8, sticky="NSEW")

stilo = ttk.Style()
#clam, alt, default, classic
stilo.theme_use("alt")
stilo.configure(".")

treeviewdados = ttk.Treeview(janela, columns=(1,2,3,4), show="headings")

treeviewdados.column("1", anchor=CENTER)
treeviewdados.heading("1", text="ID")

treeviewdados.column("2", anchor=CENTER)
treeviewdados.heading("2", text="Nome")

treeviewdados.column("3", anchor=CENTER)
treeviewdados.heading("3", text="Idade")

treeviewdados.column("4", anchor=CENTER)
treeviewdados.heading("4", text="Sexo")

treeviewdados.insert("", "end", text="1", values=("1", "Allan", 29, "Masculino"))
treeviewdados.insert("", "end", text="2", values=("2", "Ana", 41, "Feminino"))
treeviewdados.insert("", "end", text="3", values=("3", "Berenice", 50, "Feminino"))
treeviewdados.insert("", "end", text="4", values=("4", "Roger", 21, "Masculino"))
treeviewdados.insert("", "end", text="5", values=("5", "Pedro", 45, "Masculino"))


treeviewdados.grid(row=3, column=0, columnspan=8, sticky="NSEW")

janela.mainloop()