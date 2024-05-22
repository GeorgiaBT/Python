lista1 = ["A", "B", "C"]
lista2 = ["D", "E", "F"]

#extend unimos 2 listas
lista1.extend(lista2)

print(lista1)

lista1.remove("E") #remove elemento
print(lista1)

lista1.pop(2) #remove elemento
print(lista1)

lista1.pop() #remove ultimo elemento
print(lista1)

del lista1[0] #remove primeiro elemento
print(lista1)

lista1.clear() #remove todos elementos da lista
print(lista1)

lista1.append("Maçã")  #adiciona elemento
print(lista1)

lista1.insert(1, "Goiaba") #adiciona elemento
print(lista1)

lista1.insert(1, "Laranja") #adiciona elemento
print(lista1)

if "Laranja" in lista1:
    print("Sim, a fruta laranja existe na lista")
else:
    print("Não encontramos a fruta")

lista2[ "Banana"]

print(lista1)

lista1[1:2] = ["A", "b"]

print(lista1)