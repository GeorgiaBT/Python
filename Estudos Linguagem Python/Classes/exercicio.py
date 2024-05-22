class carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.km = 0

    def drive(self, numero):
        self.km += numero

    def descricao(self):
        print(self.marca, self.modelo, "(" ,self.ano, ")", "Quilometragem", self.km)


carro1 = carro("Honda", "Civic", 2017)
carro.descricao(carro1)
carro1.drive(100)
carro.descricao(carro1)
