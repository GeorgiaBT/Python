from selenium import webdriver as opcoesselenium
from selenium.webdriver.common.by import By
import pyautogui as tempoespera
from selenium.webdriver.support.select import Select

navegador = opcoesselenium.Chrome()

navegador.get("https://pt.surveymonkey.com/r/7GX9XRZ")

tempoespera.sleep(5)

navegador.find_element(By.NAME, "72542598").send_keys("Geórgia Borges Teixeira")

tempoespera.sleep(2)

navegador.find_element(By.NAME, "72542821").send_keys("georgiaborges_12@yahoo.com")

tempoespera.sleep(3)

sexo = "Feminino"

if sexo == "Masculino":
    navegador.find_element(By.ID, "72542994_583517054_label").click()

else:
    navegador.find_element(By.ID, "72542994_583517055_label").click()

tempoespera.sleep(3)

pegadropdown = navegador.find_element(By.ID, "72543178").click()
itemselecionado = Select(pegadropdown)
itemselecionado.select_by_index(2)

tempoespera.sleep(2)

navegador.find_element(By.XPATH, '//*[@id="patas"]/main/article/section/form/div[2]/button').click()

tempoespera.sleep(3)