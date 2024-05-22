from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import pyautogui as tempoespera

#Service verifica a versao do chrome e informa ao selenium para que o chromedrivermanager baixe o arquivo correspondente
servico = Service(ChromeDriverManager().install())
meunavegador = webdriver.Chrome(service=servico)
meunavegador.get("https://www.google.com.br/")

tempoespera.sleep(10)

