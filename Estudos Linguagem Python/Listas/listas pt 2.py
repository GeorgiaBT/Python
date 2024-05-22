listaminmax = [5, 10, 20, 100, 50]

print(min(listaminmax))
print(max(listaminmax))

listanumeros1a10 = [posicao for posicao in range(101) if posicao <= 10]

print(listanumeros1a10)

print("\n\n")

listadoisemdois = list(range(0, 100, 2))
print(listadoisemdois)

print("\n\n")

listaoriginal = ["Carro", "moto", "bicicleta", "lancha"]
listacopiada = listaoriginal.copy()

print(listacopiada)

print("\n\n")

lista1letras = ["A", "B", "C"]
lista2numeros = [1, 2, 3]

#Join unindo listas
listaJoin = lista1letras + lista2numeros
print(listaJoin)

print("\n\n")

l1 = ["a1", "b1", "c1"]
l2 = [11, 12, 13]

for item in l2:
    l1.append(item)

print(l1)
