dicionario = {
    "Ana": 21,
    "Marcela": 34,
    "Pedro" : 42
}
print("Exemplo dicionario 1: ",dicionario)
print(len(dicionario))
print(type(dicionario))
print("\n")

dicionario2 = dicionario.copy()
print("Exemplo dicionario 2: ",dicionario2)

dicionario3 = dict(dicionario)
print("Exemplo dicionario 3: ", dicionario3)

print("\n\n")

pessoas = {
    "Ana": 21,
    "Marcela": 34,
    "Pedro": 42,
    "Pedro": 53

}

print(pessoas)

#retornar apenas idade marcela
dados = pessoas["Marcela"]
dados2 = pessoas.get("Pedro")
print(dados)
print(dados2)

nomes = pessoas.keys()
print(nomes)

idades = pessoas.values()
print(idades)

print("\n\n")

alimentos = {
    "arroz": 35,
    "macarrão": 21.90,
    "feijão": 29
}

print(alimentos)

#alterando valores
alimentos["macarrão"] = 39.90
print(alimentos)

alimentos.update({"feijão": 10.50})
print(alimentos)

#adicionando item
alimentos["salsicha"] = 23
print(alimentos)

#remove item do dicionario
alimentos.pop("salsicha")
print(alimentos)

#remove ultimo item do dicionario
alimentos.popitem()
print(alimentos)

#remover todos os itens
alimentos.clear()
print(alimentos)



alimentos ["arroz"]= 35
alimentos["macarrão"]= 21.90
alimentos["feijão"] = 15.90

print("\n\n")
print(alimentos)

#deletando um item
del alimentos["arroz"]
print(alimentos)

if "macarrão" in alimentos:
    print("Alimento encontrado com sucesso!")
else:
    print("Alimento não foi encontrado na lista!")

print("\n\n")

letras = {
    "Letra 1" : "A",
    "Letra 2": "B",
    "Letra 3": "C",
    "Letra 4": "D",
    "Letra 5": "E",
    "Letra 6": "F"

}

print(letras)

#imprimindo os titulos
for posicao in letras:
    print(posicao)

#imprimindo os valores
for i in letras:
    print(letras[i])

print("\n")

for contador in letras.values():
    print(contador)

print("\n")

for titulo, valor in letras.items():
    print(titulo, " - ", valor)

exemplo1 = {
    "A" : 1,
    "B": 2
}

exemplo2 = {
    "C" : 3,
    "D": 4
}

exemplo3 = {
    "E" : 5,
    "F": 6
}

unirvariosdicionarios = {
    "Dicionário 1 ": exemplo1,
    "Dicionário 2 ": exemplo2,
    "Dicionário 3 ": exemplo3

}

print(unirvariosdicionarios)

print("\n\n")

escola = {
    "Turma 1": {
        "Andre": 10,
        "Amanda": 8
    },
    "Turma 2": {
        "Cleide": 7,
        "Paulo": 5
    },
    "Turma 3": {
        "Roger": 9,
        "Rosiane": 6
    }
}

for tur1, tur2 in escola.items():
    print(tur1)
    for tur1, tur2 in tur2.items():
        print("Aluno: ", tur1, " - Nota: ", tur2)