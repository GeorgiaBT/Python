class funcaoinformacoes:
    def __init__(mysillyobject, nomealuno, idadealuno, mediaaluno):
        mysillyobject.nome = nomealuno
        mysillyobject.idade = idadealuno
        mysillyobject.media = mediaaluno

    def funcaoimprimirdados (mysillyobject):
        print("Nome:", mysillyobject.nome)
        print("Idade:", mysillyobject.idade)
        print("Media:", mysillyobject.media)

pegainformacoes = funcaoinformacoes("Ricardo", 17, 8)
pegainformacoes.funcaoimprimirdados()

print("\n\n")

class notasaluno:
    def __init__(self, nota1, nota2, nota3, nota4):
        self.n1 = nota1
        self.n2 = nota2
        self.n3 = nota3
        self.n4 = nota4

notas = notasaluno(9, 4, 8, 10)

print("Nota 3:", notas.n3)

notas.n3 = 10

print("Nota 3:", notas.n3)
