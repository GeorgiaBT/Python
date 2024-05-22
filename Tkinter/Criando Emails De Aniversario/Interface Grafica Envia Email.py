from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import win32com.client as win32

outlook = win32.Dispatch("outlook.application")


janela = Tk()

janela.geometry("910x350")

#clam, alt, default, classic
stilo = ttk.Style()
stilo.theme_use("alt")
stilo.configure(".", font=("Arial 20"), rowheight=30)

treeviewdados = ttk.Treeview(janela, columns=(1,2,3), show="headings")

treeviewdados.column("1", anchor=CENTER)
treeviewdados.heading("1", text="Nome")

treeviewdados.column("2", anchor=CENTER)
treeviewdados.heading("2", text="Nascimento")

treeviewdados.column("3", anchor=CENTER)
treeviewdados.heading("3", text="Email")

treeviewdados.grid(row=2, column=0, columnspan=8, sticky="NSEW")

import pandas as pd
from datetime import date
import numpy as np

arquivoaniversario = pd.read_excel("C:\\Users\\georg\\Downloads\\Aniversario.xlsx")

arquivoaniversario["Nascimento"] = arquivoaniversario["Nascimento"].astype(str)

#criando a coluna ano
arquivoaniversario["Ano"] = arquivoaniversario["Nascimento"].str[:4]

arquivoaniversario["Mês"] = arquivoaniversario["Nascimento"].str[5:7]

arquivoaniversario["Dia"] = arquivoaniversario["Nascimento"].str[-2:]

arquivoaniversario["Data Atual"] = date.today()

arquivoaniversario["Data Atual"] = arquivoaniversario["Data Atual"].astype(str)

arquivoaniversario["Ano Atual"] = arquivoaniversario["Data Atual"].str[:4]

arquivoaniversario["Mês Atual"] = arquivoaniversario["Data Atual"].str[5:7]

arquivoaniversario["Dia Atual"] = arquivoaniversario["Data Atual"].str[-2:]

arquivoaniversario["Aniversário"] = np.where((arquivoaniversario["Mês"] == arquivoaniversario["Mês Atual"]) &
                                              (arquivoaniversario["Dia"] == arquivoaniversario["Dia Atual"]), "Sim", "")

#filtra somente os aniversariantes do dia
arquivoaniversario = arquivoaniversario.loc[arquivoaniversario["Aniversário"] != "", ["Nome", "Nascimento", "Email"]]

print(arquivoaniversario)

for linha in range(len(arquivoaniversario)):
    #print(arquivoaniversario.iloc[linha,2])
    treeviewdados.insert("", "end",
                         values=(str(arquivoaniversario.iloc[linha,0]), #nome
                                 str(arquivoaniversario.iloc[linha,1]), #aniversario
                                 str(arquivoaniversario.iloc[linha,2]))) #email

def deletaritemtreeview():

    itens = treeviewdados.selection()

    for item in itens:

        treeviewdados.delete(item)

        messagebox.showinfo(title="Atenção!", message="Nome deletado com sucesso!")

        contarnumerolinhas()


botaodeletar =Button(text="Deletar",
                     font="Arial 20",
                     command=deletaritemtreeview)

botaodeletar.grid(row=1, column=0, columnspan=2, sticky="NSEW")

nome = Label(text="Nome:", font="Arial 12")
nome.grid(row=0, column=0, sticky="W")

exibirnome = Entry(font="Arial 12")
exibirnome.grid(row=0, column=1, sticky="W")

nascimento = Label(text="Nascimento:", font="Arial 12")
nascimento.grid(row=0, column=2, sticky="W")

exibirnascimento = Entry(font="Arial 12")
exibirnascimento.grid(row=0, column=3, sticky="W")

email = Label(text="Email:", font="Arial 12")
email.grid(row=0, column=4, sticky="W")

exibiremail = Entry(font="Arial 12")
exibiremail.grid(row=0, column=5, sticky="W")

def additemtreeview():

    if exibirnome.get() == "":
        messagebox.showinfo(title="Atenção!", message="Por favor digite um nome!")
    elif exibirnascimento.get() == "":
        messagebox.showinfo(title="Atenção!", message="Por favor digite o nascimento!")
    elif exibiremail == "":
        messagebox.showinfo(title="Atenção!", message="Por favor digite um email!")
    else:
        treeviewdados.insert("", "end",
                             values=(str(exibirnome.get()),
                                    str(exibirnascimento.get()),
                                    str(exibiremail.get())))
        messagebox.showinfo(title="Atenção!", message="Nome cadastrado com sucesso!")

        contarnumerolinhas()

        exibirnome.delete(0,"end")
        exibirnascimento.delete(0, "end")
        exibiremail.delete(0, "end")

botaoadd =Button(text="Adicionar",
                     font="Arial 20",
                     command=additemtreeview)

botaoadd.grid(row=1, column=2, columnspan=2, sticky="NSEW")

def alteraritemtreeview():

    if exibirnome.get() == "":
        messagebox.showinfo(title="Atenção!", message="Por favor digite um nome!")
    elif exibirnascimento.get() == "":
        messagebox.showinfo(title="Atenção!", message="Por favor digite o nascimento!")
    elif exibiremail == "":
        messagebox.showinfo(title="Atenção!", message="Por favor digite um email!")
    else:
        itemselecionado = treeviewdados.selection()[0]
        treeviewdados.item(itemselecionado,
                           values=(str(exibirnome.get()),
                                   str(exibirnascimento.get()),
                                   str(exibiremail.get())))

        messagebox.showinfo(title="Atenção!", message="Nome alterado com sucesso!")

        exibirnome.delete(0, "end")
        exibirnascimento.delete(0, "end")
        exibiremail.delete(0, "end")


botaoalterar =Button(text="Alterar",
                     font="Arial 20",
                     command=alteraritemtreeview)

botaoalterar.grid(row=1, column=4, columnspan=2, sticky="NSEW")

def criaremail():

    for numerolinha in treeviewdados.get_children():

        #dadosdalinha = treeviewdados.item(numerolinha)["values"]
        #print(dadosdalinha)

        emailoutlook = outlook.CreateItem(0)

        nome = treeviewdados.item(numerolinha)["values"][0]
        aniversario = treeviewdados.item(numerolinha)["values"][1]
        email = treeviewdados.item(numerolinha)["values"][2]

        #split quebra o nome em colunas de acordo com o criterio
        variavelnome = nome.split(" ")[0]

        emailoutlook.To = email
        emailoutlook.Subject = "Feliz Aniversário!" + str(nome)
        emailoutlook.HTMLBody = f"""
        <p>Parabéns, <b>{variavelnome}</b>!</p>
        <p><font color="yellow">Esse é um dia especial, aproveite seu dia!</font></p>
        <p><a href="https://www.google.com.br/"> Clique aqui para acessar seu presente.</a></p>
        <p>Atenciosamente.</p>
        <p><img src="C:\\Users\\georg\\Downloads\\d75120ea8936aa198cdb98da5d64ffc0.jpg"></p>
        """
        #<b> negrito
        #<a href> = para colocar um hyperlinlk
        emailoutlook.save()

    messagebox.showinfo(title="Atenção!", message="Emails criados com sucesso!")

botaoemail =Button(text="Criar Email",
                     font="Arial 20",
                     command=criaremail)

botaoemail.grid(row=1, column=6, columnspan=2, sticky="NSEW")


labelnumerolinhas = Label(text="Linhas:", font="Arial 20")
labelnumerolinhas.grid(row=4, column=0, columnspan=8, sticky="W")

def contarnumerolinhas(item=""):

    numero = 0

    linhas = treeviewdados.get_children(item)

    for linha in linhas:

        numero += 1

    labelnumerolinhas.config(text="Aniversariantes:" + str(numero))

contarnumerolinhas()

def passadadosparaentry(Event):

    item = treeviewdados.selection()

    for linha in item:

        exibirnome.delete(0, END)
        exibirnascimento.delete(0, END)
        exibiremail.delete(0, END)

        exibirnome.insert(0, treeviewdados.item(linha, "values")[0])
        exibirnascimento.insert(0, treeviewdados.item(linha, "values")[1])
        exibiremail.insert(0, treeviewdados.item(linha, "values")[2])


treeviewdados.bind("<Double-1>", passadadosparaentry)

janela.mainloop()

