#variavel global, acessa de qualquer funçao
nome = "Silvana"

def funcao1():
    print(nome)

def funcao2():
    print(nome)

funcao1()
funcao2()

nomesobrenome = "Georgia Borges"

def funcaonomesobrenome():
    print(nomesobrenome)

def funcaonomesobrenome2():
    #variavel local, dentro da funcao, nao estamos mudando o valor e sim criando uma nova variavel, por isso a variavel global não é afetada
    nomesobrenome = "Bill Gates"
    print(nomesobrenome)

funcaonomesobrenome()
funcaonomesobrenome2()
print(nomesobrenome)

print("\n")

idade = 32

def funcaoidade1():
    print(idade)

def funcaoidade2():
    #mudou a variavel global dentro da função
    global idade
    idade = 34
    print(idade)

funcaoidade1()
funcaoidade2()
print(idade)
