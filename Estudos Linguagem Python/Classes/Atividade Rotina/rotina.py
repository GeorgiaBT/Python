class Rotina:
    def __init__(self, nome, dormindo=False, dirigindo=False):
        self.nome = nome
        self.dormindo = dormindo
        self.dirigindo = dirigindo

    def dormir(self):

        if self.dirigindo:
            print(self.nome, "não pode dormir enquanto dirige")
            return

        if self.dormindo:
            print(self.nome, "já está dormindo")
            return

        print("O " + self.nome + " esta dormindo")
        self.dormindo = True

    def acordar(self):

        if not self.dormindo:
            print("O", self.nome, "já está acordado")
            return

        print("O " + self.nome + " acordou")
        self.dormindo = False

    def dirigir(self):

        if self.dormindo:
            print(self.nome, "não pode dirigir enquanto está dormindo")
            return

        if self.dirigindo:
            print(self.nome, "já está dirigindo")
            return

        print("O " + self.nome + " esta dirigindo")
        self.dirigindo = True

    def parardirigir(self):

        if not self.dirigindo:
            print(self.nome, "já parou de dirigir")
            return

        print("O " + self.nome + " parou de dirigir")
        self.dirigindo = False
