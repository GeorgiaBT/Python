import  pyautogui as escolhaopcao


opcao = escolhaopcao.confirm('Clique no botão desejado',
            buttons=['excel', 'word', 'notepad'])

if opcao == "excel":

    escolhaopcao.hotkey('win', 'r')

    escolhaopcao.sleep(2)

    escolhaopcao.typewrite('excel')

    escolhaopcao.sleep(2)

    escolhaopcao.press('enter')

    escolhaopcao.sleep(5)

    escolhaopcao.click(x=334, y=254)

    escolhaopcao.sleep(3)

    escolhaopcao.typewrite("Digitando no excel")

    print("Você escolheu abrir o excel")

elif opcao == "word":

    escolhaopcao.hotkey('win', 'r')

    escolhaopcao.sleep(2)

    escolhaopcao.typewrite('winword')

    escolhaopcao.sleep(2)

    escolhaopcao.press('enter')

    escolhaopcao.sleep(5)

    escolhaopcao.click(x=392, y=250)

    escolhaopcao.sleep(3)

    escolhaopcao.typewrite("Digitando no word")

    print("Você escolheu abrir o word")

else:

    escolhaopcao.hotkey('win', 'r')

    escolhaopcao.sleep(2)

    escolhaopcao.typewrite('notepad')

    escolhaopcao.sleep(2)

    escolhaopcao.press('enter')

    escolhaopcao.sleep(5)

    escolhaopcao.typewrite("Digitando no notas")

    print("Você escolheu abrir o bloco de notas")
