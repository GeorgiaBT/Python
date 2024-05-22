numero = 1
while numero < 11:
    print(numero)
    numero += 1

print("\n")

num = 1
while num <= 1000:
    print("Numero: ", num)

    if num == 5:
        break
    num += 1

print("\n")

n = 0
while n < 10:
    n += 1

    if n == 6:
        continue
    print(n)

print("\n")

contador = 0

while contador < 11:
    contador += 1
    print("Número: "), contador
else:
    print("Números impressos com sucesso!")