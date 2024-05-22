from selenium import webdriver as opcoesselenium
from selenium.webdriver.common.by import By

import pandas as pd

navegador = opcoesselenium.Chrome()

navegador.get("https://rpachallengeocr.azurewebsites.net/")

elementotabela = navegador.find_element(By.XPATH, '//*[@id="tableSandbox"]')

linhas = elementotabela.find_elements(By.TAG_NAME, "tr")
colunas = elementotabela.find_elements(By.TAG_NAME, "td")

dataframelista = []

linha =  1

for linhaatual in linhas:

    print(linhaatual.text)
    dataframelista.append(linhaatual.text)

    linha +=1

arquivoexcel = pd.ExcelWriter('dadossite.xlsx', engine='xlsxwriter')
arquivoexcel._save()

dataFrame = pd.DataFrame(dataframelista, columns=['Nome_Coluna_D0ados'])

arquivoexcel = pd.ExcelWriter('Dados_Site.xlsx', engine='xlsxwriter')

dataFrame.to_excel(arquivoexcel, sheet_name= 'Sheet1', index=False)

arquivoexcel._save()

