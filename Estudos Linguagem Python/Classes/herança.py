class alunoescolapai:
    # construtor
    def __init__(self, nome, sexo, media, situacao):
        self.nome = nome
        self.sexo = sexo
        self.media = media
        self.situacao = situacao

    def imprimirdados(self):
        print("Aluno:", self.nome)
        print("Sexo:", self.sexo)
        print("Media:", self.media)
        print("Situação:", self.situacao)

#heranca basta colocar o nome da classe que quer herdar entre os parenteses
class alunoescolafilho(alunoescolapai):
    #quando cria-se um construtor na classe filho ele sobrescreve a classe pai

    def __init__(self, nome, sexo, n1, n2, n3, n4):
        self.media = (n1 + n2 + n3 + n4) / 4

        if self.media >= 6:
            self.situacao = "Aprovado(a)!"
        else:
            self.situacao = "Reprovado(a)!";

#com a função super chamamos o construtor da classe pai
#init é o construtor da classe pai
        super().__init__(nome, sexo, self.media, self.situacao)

aluno1 = alunoescolafilho("Rodrigo", "M", 9, 8, 7 , 4)

aluno1.imprimirdados()