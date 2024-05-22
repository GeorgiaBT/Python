from tkinter import *
from tkinter import messagebox
from tkinter import ttk

janela = Tk()

janela.title("Cotação")

Label(janela, text="Moeda: ",
      font=("Arial 20")).grid(row=0, column=0)

moedaselecionado = ttk.Combobox(janela, font=("Arial 20"))

moedaselecionado["values"] = ("Dolar",
                            "Euro",
                            "Peso")

moedaselecionado.grid(row=0, column=1)

moedaselecionado.current(0)

def pesquisaritem():

    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.select import Select

    import pyautogui as tempoespera

    # Service verifica a versao do chrome e informa ao selenium para que o chromedrivermanager baixe o arquivo correspondente
    servico = Service(ChromeDriverManager().install())
    meunavegador = webdriver.Chrome(service=servico)

    meunavegador.get("https://www.google.com.br/")

    tempoespera.sleep(3)

    meunavegador.find_element(By.NAME, "q").send_keys("Dólar hoje")

    tempoespera.sleep(2)

    #faz a busca
    meunavegador.find_element(By.NAME, "q").send_keys(Keys.RETURN)

    tempoespera.sleep(4)

    valordolargoogle = meunavegador.find_elements(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')[0].text

    tempoespera.sleep(2)

    print(valordolargoogle)

    tempoespera.sleep(2)

    if str(moedaselecionado.get()) == "Euro":

        tempoespera.sleep(2)

        selecionacombobox = Select(meunavegador.find_element(By.CLASS_NAME, "l84FKc")) #zuzy3c

        linha = 0

        for opcao in selecionacombobox.options:

            print(opcao.text)

            if opcao.text == "Euro":

                tempoespera.sleep(2)

                pegadropdrown = meunavegador.find_element(By.CLASS_NAME, "l84FKc") #zuzy3c

                tempoespera.sleep(2)

                itemselecionado = Select(pegadropdrown)

                itemselecionado.select_by_index(linha)

                tempoespera.sleep(3)

                valordolargoogle = meunavegador.find_elements(By.XPATH,'//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')[0].text

                tempoespera.sleep(1)

                break

            linha = linha + 1

        tempoespera.sleep(2)

        valorMoeda.config(text=str(moedaselecionado.get()) + ":" + valordolargoogle)


    else:

        valorMoeda.config(text=str(moedaselecionado.get()) + ":" + valordolargoogle)


botaopesquisar = Button(text="Pesquisar",
                        font=("Arial 20"),
                        command=pesquisaritem)
botaopesquisar.grid(row=1, column=0, columnspan=2,sticky="NSEW")

valorMoeda = Label(janela, text="Valor: 0",
                         font=("Arial 20"))
valorMoeda.grid(row=2, column=0, columnspan=2,sticky="W")

janela.mainloop()