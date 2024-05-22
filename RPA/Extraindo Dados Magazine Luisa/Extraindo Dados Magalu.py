from selenium import webdriver as opcoesselenium
from selenium.webdriver.common.by import By

import pyautogui as tempoespera
import pyautogui as funcoesteclado

navegador = opcoesselenium.Chrome()

navegador.get('https://www.magazineluiza.com.br/')

#procura pelo campo ID e digita o nome do produto
navegador.find_element(By.ID, 'input-search').send_keys("geladeira")

tempoespera.sleep(2)

funcoesteclado.press("enter")

tempoespera.sleep(10)

listaprodutos = navegador.find_elements(By.CLASS_NAME, "ciMFyT")

for item in listaprodutos:

    nomeproduto = ""
    precoproduto = ""
    urlproduto = ""

    if nomeproduto == "":

        try:
            nomeproduto = item.find_element(By.CLASS_NAME, "fbccdO").text
        except Exception:
            pass

    elif nomeproduto == "":

        try:
            nomeproduto = item.find_element(By.CLASS_NAME, "sc-fvwjDU").text
        except Exception:
            pass

    if precoproduto == "":

        try:
            precoproduto = item.find_element(By.CLASS_NAME, "dOwMgM").text
        except Exception:
            pass

    elif precoproduto == "":

        try:
            precoproduto = item.find_element(By.CLASS_NAME, "sc-bOhtcR").text
        except Exception:
            pass

    elif precoproduto == "":

        try:
            precoproduto = item.find_element(By.CLASS_NAME, "eCPtRw").text
        except Exception:
            pass

    elif precoproduto == "":

        try:
            precoproduto = item.find_element(By.CLASS_NAME, "sc-kpDqfm").text
        except Exception:
            pass

    else:

        precoproduto = "0"

    if urlproduto == "":

        try:
            urlproduto = item.find_element(By.TAG_NAME, "a").get_attribute("href")
        except Exception:
            pass

    else:

        urlproduto = "-"

    print(nomeproduto, "-", precoproduto)
    print(urlproduto)