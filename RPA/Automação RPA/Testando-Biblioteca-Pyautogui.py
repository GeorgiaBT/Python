import pyautogui as posicaomouse
import pyautogui as tempoespera

tempoespera.sleep(5)

posicaomouse.moveTo(772, 1055)

tempoespera.sleep(2)

posicaomouse.click(772, 1055)

tempoespera.sleep(2)

posicaomouse.typewrite('calc')

tempoespera.sleep(5)

posicaomouse.click(242, 377)

tempoespera.sleep(2)

print(posicaomouse.position())