class dados:
    def __init__(self, nome, idade, estadocivil, salario):
        self.nome = nome
        self.idade = idade
        self.estadocivil = estadocivil
        self.salario = salario

    def imprimirdados(self):
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("Estado Civil:", self.estadocivil)
        print("Salario:", self.salario)
        print("\n")