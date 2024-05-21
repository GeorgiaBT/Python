import pyautogui as posicaomouse

#mesma coisa que pressionar as teclas do teclado windows + r
posicaomouse.hotkey('win', 'r')

posicaomouse.sleep(2)

posicaomouse.typewrite('notepad')

posicaomouse.sleep(2)

posicaomouse.press('enter')

posicaomouse.sleep(3)

posicaomouse.typewrite('Abri o bloco de notas com o python!')

posicaomouse.sleep(3)

fecharblocodenotas = posicaomouse.getActiveWindow()

posicaomouse.sleep(2)

fecharblocodenotas.close()

posicaomouse.sleep(2)

posicaomouse.press('tab')

posicaomouse.sleep(2)

posicaomouse.press('tab')

print("Automação executada com sucesso!")
