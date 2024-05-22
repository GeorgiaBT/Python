palavracomespaco = "                     Curso de Python"

print(palavracomespaco)
print(palavracomespaco.strip())

print("------------------------------")

gostoporfrutas = "Eu gosto de Laranja"
print("Maçã" in gostoporfrutas )

resultado = gostoporfrutas.find("o")
print(resultado)

print("------------------------------")
copa = "Brasil vai ganhar a copa do mundo"

campeao = "Alemanha" not in copa

print(campeao)

print("------------------------------")
aluno = "Rebecca Martins"
nota1= 9
nota2 = 6
media = (nota1 + nota2)/2

print("Aluna: " + aluno + " - Média: " + str(media))

print(f"Aluna: {aluno} - Media: {media}")

ajustetexto = "Aluna: {} - Media: {}"
print(ajustetexto.format(aluno, media))