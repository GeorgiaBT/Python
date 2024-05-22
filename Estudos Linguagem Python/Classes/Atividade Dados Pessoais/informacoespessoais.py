from dadospessoais import dados

pessoa1 = dados("Celso", 34, "Solteiro", 5000)
pessoa2 = dados("Aline", 24, "Solteira", 3200)

dados.imprimirdados(pessoa1)
dados.imprimirdados(pessoa2)

#altera dados pessoa 1
pessoa1.nome = "Sebastian"
pessoa1.idade = 45
pessoa1.estadocivil = "Casado"
pessoa1.salario = 10000

dados.imprimirdados(pessoa1)

pessoa2.nome = input("Digite o seu nome: ")
pessoa2.idade = int(input("Digite a sua idade: "))
pessoa2.estadocivil = input("Digite o seu estado civil: ")
pessoa2.salario = float(input("Digite o seu salario: "))

dados.imprimirdados(pessoa2)