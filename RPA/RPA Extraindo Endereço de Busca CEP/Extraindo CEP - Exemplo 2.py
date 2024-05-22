from selenium import webdriver as opcoesselenium
from selenium.webdriver.common.by import By
import pyautogui as tempoespera

navegador = opcoesselenium.Chrome()
navegador.get("https://buscacepinter.correios.com.br/app/endereco/index.php")

tempoespera.sleep(4)

#inserindo o cep
navegador.find_element(By.NAME, "endereco").send_keys("80320210")

tempoespera.sleep(2)

#clica no botao buscar
navegador.find_element(By.NAME, "btn_pesquisar").click()

tempoespera.sleep(4)

elementotabela = navegador.find_element(By.XPATH, '//*[@id="resultado-DNEC"]')

for linhatabela in elementotabela.find_elements(By.TAG_NAME, "tr"):
    endereco = ""
    for colunastabela in linhatabela.find_elements(By.TAG_NAME, "td"):

        endereco = endereco + ";" + colunastabela.text

print(endereco)