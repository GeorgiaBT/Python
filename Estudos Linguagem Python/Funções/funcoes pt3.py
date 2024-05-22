#Argumentos com chaves
def provaaluno(nota1, nota2, nota3):
    print("O aluno tirou", nota3)

provaaluno(nota1= 9, nota2=7, nota3= 6)

print("\n\n")

#Funcao com parametro padrao
def funcaonome(nome = "Python"):
    print("Meu nome é", nome)

funcaonome("Alice")
funcaonome("Pedro")
funcaonome()  #pega o nome padrao
funcaonome("Carolina")

print("\n\n")

#Passando uma lista como um argumento
def funcaolistanumeros(numero):
    print(numero)
    for item in numero:
        print(item)

listanumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

funcaolistanumeros(listanumeros)

print("\n\n")

#funcao multiplicar
def multiplicacaodoisnumeros (numerorecebido):
    return 10 * numerorecebido

print(multiplicacaodoisnumeros(5))
print(10, "x", 10, "=", multiplicacaodoisnumeros(10))