print("Exemplo 1 de função")

#uma função
def minhaprimeirafuncao():
    print("Essa é minha primeira função criada com Python!")

minhaprimeirafuncao()

def funcaotexto(nome):
    print(nome, "Santos")

funcaotexto("Ana")
funcaotexto("Roger")
funcaotexto("Marcos")

def funcaosaudacao(saudacao, nome):
    print(saudacao, nome)

funcaosaudacao("Boa noite", "Ana")
funcaosaudacao("Boa tarde", "Luis")
funcaosaudacao("Bom dia", "Roger")

print("\n\n")


#funcao com 2 parametros/argumentos
def funcaocomargumentos(nome, sobrenome):
    print("Nome completo:", nome, sobrenome)

nomeinput = input("Digite seu nome: ")
sobrenomeinput = input("Digite seu sobrenome: ")

funcaocomargumentos(nomeinput, sobrenomeinput)
