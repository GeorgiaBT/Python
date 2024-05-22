"""
A diferenca das listas para as tuplas é que não podemos editar os elementos da tupla

"""

tuplaletras = ("A", "B", "C", "D")

print(tuplaletras)
print(type(tuplaletras))
print(len(tuplaletras))
print(tuplaletras[0])
print(tuplaletras[1])
print(tuplaletras[-1])

#precisa ter mais de um item ou , pra ser tupla
novatupla = ("E",)
print(novatupla)
print(type(novatupla))

tuplaletras += novatupla

print("\n")
print(tuplaletras)

print("\n")
#removendo elemento
tuplanumeros = (1, 2, 3, 4, 5 , 6, 7)
listanumeros = list(tuplanumeros) #converte tupla em lista
listanumeros.remove(4)
tuplanumeros = tuple(listanumeros)
print(tuplanumeros)

print("\n")

tuplafrutas = ("Banana", "Abacaxi", "Laranja", "Maçã")

for item in tuplafrutas:
    print(item)