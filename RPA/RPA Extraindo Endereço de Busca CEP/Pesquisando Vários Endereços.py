from selenium import webdriver as opcoesselenium
from selenium.webdriver.common.by import By
import pyautogui as tempoespera
import pandas as pd

navegador = opcoesselenium.Chrome()
navegador.get("https://buscacepinter.correios.com.br/app/endereco/index.php")

tempoespera.sleep(4)

#dicionario
dicionariocep ={
    "CEP 1": "80730001",
    "CEP 2": "80320210",
    "CEP 3": "82560260"
}

listadataframe = []

#inserindo o cep
navegador.find_element(By.NAME, "endereco").send_keys("80730001")

tempoespera.sleep(2)

#clica no botao buscar
navegador.find_element(By.NAME, "btn_pesquisar").click()

tempoespera.sleep(4)

for contador in dicionariocep.values():

    tempoespera.sleep(4)
    #voltando para pagina inicial para pesquisar um novo cep
    navegador.get('https://buscacepinter.correios.com.br/app/endereco/index.php')

    tempoespera.sleep(3)

    navegador.find_element(By.NAME, "endereco").send_keys(contador)

    tempoespera.sleep(3)

    # clica no botao buscar
    navegador.find_element(By.NAME, "btn_pesquisar").click()

    tempoespera.sleep(4)

    elementotabela = navegador.find_element(By.XPATH, '//*[@id="resultado-DNEC"]')

    endereco = ""
    for linhatabela in elementotabela.find_elements(By.TAG_NAME, "tr"):

        for colunastabela in linhatabela.find_elements(By.TAG_NAME, "td"):

            endereco = endereco + ";" + colunastabela.text

    listadataframe.append(endereco)

arquivoexcel = pd.ExcelWriter('enderecobuscacep.xlsx', engine='xlsxwriter')
arquivoexcel._save()

dataFrame = pd.DataFrame(listadataframe, columns=[';Rua;Bairro;Cidade;CEP'])

#preparando o arquivo usando o mecanismo xlsx writer
arquivoexcel = pd.ExcelWriter('enderecobuscacep.xlsx', engine='xlsxwriter')

#convertendo o dataframe em um objeo excel
dataFrame.to_excel(arquivoexcel, sheet_name='Dados', index=False)

#salvando o arquivo com as alterações
arquivoexcel._save()