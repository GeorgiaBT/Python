def funcaodivisao(numero1, numero2):
    return  numero1/numero2

resultado = funcaodivisao(10,2)
print(resultado )

def funcaomedia(nota1, nota2, nota3, nota4):
    return (nota1 + nota2 + nota3 + nota4) / 4

media = funcaomedia(10, 9, 7, 3)
print(media)

#funcao com argumentos arbitrarios, *args
def frutapreferida(*fruta):
    print("Eu gosto de ", fruta[0])
    print("Eu gosto de ", fruta[1])
    print("Eu gosto de ", fruta[2])
    print("Eu gosto de ", fruta[3])

frutapreferida("Banana", "Goiaba", "Laranja", "Kiwi")

print("\n")

def unirlistas(*listas):
    print(listas)

lista1 = [1, 2, 3, 4]
lista2 = [6, 7, 8, 9, 10]

unirlistas(*lista1, *lista2)

print("\n")

#se o numero de argumentos da palavra chave for desconhecido adicionamos ** antes do nome do parametro
def funcaokwargs (**parametro):
    print("Eu moro em ", parametro["cidade1"])
    print("Eu moro em ", parametro["cidade2"])

funcaokwargs(cidade1 = "SP", cidade2 = "RJ")
