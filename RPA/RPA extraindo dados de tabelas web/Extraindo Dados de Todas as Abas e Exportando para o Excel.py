from selenium import webdriver as opcoesselenium
from selenium.webdriver.common.by import By

import pyautogui as tempoespera

import pandas as pd

navegador = opcoesselenium.Chrome()

navegador.get("https://rpachallengeocr.azurewebsites.net/")

listadataframe = []

linha =  1

i = 1

while i < 4:

    elementotabela = navegador.find_element(By.XPATH, '//*[@id="tableSandbox"]')

    linhas = elementotabela.find_elements(By.TAG_NAME, "tr")
    colunas = elementotabela.find_elements(By.TAG_NAME, "td")

    for linhaatual in linhas:
        print(linhaatual.text)
        listadataframe.append(linhaatual.text)

        linha = linha + 1

    i += 1

    tempoespera.sleep(2)

    navegador.find_element(By.XPATH, '//*[@id="tableSandbox_next"]').click()

    tempoespera.sleep(2)

else:
    print("Dados extraídos com sucesso!")

arquivoexcel = pd.ExcelWriter('DadosAbasSite.xlsx', engine='xlsxwriter')
arquivoexcel._save()

dataFrame = pd.DataFrame(listadataframe, columns=['#;ID;Due Date'])

arquivoexcel = pd.ExcelWriter('Dados_Abas_Site.xlsx', engine='xlsxwriter')

dataFrame.to_excel(arquivoexcel, sheet_name='Dados', index=False)

arquivoexcel._save()