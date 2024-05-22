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

rua = navegador.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[1]').text
print("Rua:", rua)

bairro = navegador.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[2]').text
print("Bairro:", bairro)

cidade = navegador.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[3]').text
print("Cidade:", cidade)

cep = navegador.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[4]').text
print("CEP:", cep)

