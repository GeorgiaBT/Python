"""
Classes são as especificacoes de um conjunto de objetos/regras
objetos - um item da classe
"""

class minhaprimeiraclasse:
    idade = 30
    nome = "João"

pegaidade = minhaprimeiraclasse()
print("Nome:",pegaidade.nome, "- Idade:", pegaidade.idade)

print("\n\n")

class aluno:
    nome = ""
    idade = 0
    altura = 0

dados = aluno()
dados.nome = "Cintia"
dados.idade = 21
dados.altura = 1.79

print("Estudante:", dados.nome)
print("Idade:", dados.idade)
print("Altura:", dados.altura)
print("\n\n")

class turma:
    #def é um metodo construtor
    #o metodo construtor em python é o __int__
    #self é um parametro da propria
    def __init__(self, nomealuno, idadealuno, alturaaluno):
        self.nome = nomealuno
        self.idade = idadealuno
        self.altura = alturaaluno

    def imprimir(self):
        print("Estudante:", self.nome)
        print("Idade:", self.idade)
        print("Altura:", self.altura)


aluno1 = turma("Paula", 17, 1.65)
aluno2 = turma("Rafael", 21, 1.78)
aluno3 = turma("Rodrigo", 16, 1.71)

aluno1.imprimir()
aluno2.imprimir()
aluno3.imprimir()
