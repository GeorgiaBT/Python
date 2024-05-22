nome = "Beatriz Yumi Coelho Prates"

print(nome)
print("Total de caracteres: " + str(len(nome)))

print(nome[0])
print(nome[0:8])
print(nome[8:12])
print(nome[8:])

frase = "CUrSo de LoGica DE PROgramaçÃO PYthOn"

#upper retorna todas as letras em maiusculas
print(frase.upper())
#lower retorna todas as letras em mainusculas
print(frase.lower())

notaprova = "Tirei nota cinco na prova"

#replace substitui um dado
print(notaprova.replace("cinco","dez"))

cpf = "123.456.789-10"

cpfpartes = cpf.split(".")
print(cpfpartes)

print(cpfpartes)
print(cpfpartes[0])
print(cpfpartes[1])
print(cpfpartes[2])

cpfpartes2 = cpfpartes[2].split("-")
print(cpfpartes2[0])
print(cpfpartes2[1])

print("CPF: " + cpfpartes[0] + cpfpartes[1] + cpfpartes2[0] + cpfpartes2[1])