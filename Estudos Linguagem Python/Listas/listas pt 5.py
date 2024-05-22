listaletras = ["A","C","F","B","E", "D"]
print(listaletras)
#ordena as letras
listaletras.sort()
print(listaletras)

listaletras.sort(reverse = True)
print(listaletras)

listanumeros = [1,6, 3, 17, 43, 24, 12, 7]
print(listanumeros)
listanumeros.sort()
print(listanumeros)

listanumeros.sort(reverse=True)
print(listanumeros)

listamaimin = [ "Sofa", "TV", "carro", "Casa", "armario"]
print(listamaimin)
listamaimin.sort()
print(listamaimin)

listamaimin.sort(key=str.lower)
print(listamaimin)