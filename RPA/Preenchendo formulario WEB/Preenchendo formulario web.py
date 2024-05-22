from selenium import webdriver as opcoesselenium
from selenium.webdriver.common.by import By
import pyautogui as tempoeespera

from selenium.webdriver.support.select import Select

navegador = opcoesselenium.Chrome()

navegador.get("https://form.jotform.com/221436066464051")

tempoeespera.sleep(5)

#preenche o campo nome
navegador.find_element(By.NAME, "q3_nome[first]").send_keys("Geórgia ")

tempoeespera.sleep(1)

navegador.find_element(By.NAME, "q3_nome[last]").send_keys("Borges Teixeira")

tempoeespera.sleep(1)

navegador.find_element(By.NAME, "q4_email").send_keys("georgiaborges_12@yahoo.com")

tempoeespera.sleep(3)

pegadropdown = navegador.find_element(By.ID, "input_5")
itemselecionado = Select(pegadropdown)
itemselecionado.select_by_index(2)

tempoeespera.sleep(2)

filho = "Não"

if filho == "Sim":
    navegador.find_element(By.ID, "label_input_6_0").click()

else:
    navegador.find_element(By.ID, "label_input_6_1").click()

tempoeespera.sleep(2)

navegador.find_element(By.ID, "label_input_7_2").click()

tempoeespera.sleep(2)

navegador.find_element(By.ID, "label_input_7_4").click()

tempoeespera.sleep(2)

navegador.find_element(By.XPATH, '//*[@id="input_8"]/div[4]').click()

tempoeespera.sleep(2)

navegador.find_element(By.ID, "input_9_0_2").click()

tempoeespera.sleep(2)

navegador.find_element(By.ID, "input_9_1_3").click()

tempoeespera.sleep(2)

#navegador.find_element(By.ID, "input_2")


