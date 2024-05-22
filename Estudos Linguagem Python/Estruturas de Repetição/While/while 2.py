linha = 0

while linha < 3:
    coluna = 0
    while coluna < 3:
        print("Linha: ", linha, "Coluna: ", coluna)
        coluna += 1
    linha += 1

numeroinicial = 1
numerofinal = int(input("Digite um número maior que 1: "))

while numeroinicial <= numerofinal:
    print("Escolhi: ", numeroinicial)
    numeroinicial += 1

print("\n")

numero = 1
npar = int(input("Digite um numero maior que 1: "))

while numero <= npar:
    if numero % 2 == 0:
        print(numero, " ")
    numero += 1
