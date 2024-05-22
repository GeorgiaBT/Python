"""
add - adiciona itens
union - unir sets
intersetion - retorna itens existentes em ambos conjuntos

symmetric_difference_update - mantem apenas os itens que não estao presentes em ambos conjuntos

symmetric_difference - retorna apenas os itens que não estao presentes em ambos conjuntos

"""

setexemplonumeros = set()
setexemplonumeros.add(1)
setexemplonumeros.add(2)
setexemplonumeros.add(3)
setexemplonumeros.add(4)
setexemplonumeros.add(5)
setexemplonumeros.add("Amanda")

print(setexemplonumeros)
print("\n")

#add
setletras = {"A", "B", "C"}
print(setletras)
print("\n")
#union

set1 = {"Alla,", "Berenice", "Roger"}
set2 = {39, 21, 45}

uniaosets = set1.union(set2)
print(uniaosets)
print("\n")

#intersetion

listaset1 = {"Python", "C++", "Java"}
listaset2 = {"VisualG", "Logica", "Python"}

imprimindoosdoisparaconferir = listaset1.union(listaset2)
print(imprimindoosdoisparaconferir)

valorqueestaemabosossets = listaset1.intersection(listaset2)
print(valorqueestaemabosossets)

#symmetric_difference_update
listaset1.symmetric_difference_update(listaset2)
print(listaset1)

#symmetric_difference
listas1 = {"Python", "C++", "Java"}
listas2 = {"VisualG", "Logica", "Python"}

naoestaoemambos = listas1.symmetric_difference(listas2)
print(naoestaoemambos)

print("\n")

setnumero = {1, 2, 3, 4, 5, 6, 6, 7, 8}
print(setnumero)
#sets não aceitam valores repetidos
print(len(setnumero))
#não conta  os valores repetidos

setex1 = { "A", "B", "C"} #set string
setex2 = {1, 2, 3} # set numeros
setex3 = {True, False, False} #set boleano
setex4 = {"Maçã", 2, True} #set misturado
setex2.update(setex1) #unindo os sets

print("\n\n")
print(setex1)
print(setex2)
print(setex3)
print(setex4)
print("\n")

listaobjetos = {"Casa", "moto", "Bicicleta", "lancha"}

for item in listaobjetos:
    print(item)

listaobjetos.add("Carro")
print(listaobjetos) #add item no set

listaobjetos.remove("moto")
print(listaobjetos) #remove item no set

listaobjetos.pop()
print(listaobjetos) #remove ultimo item da lista

print("Carro" in listaobjetos) #verifica se esta no set