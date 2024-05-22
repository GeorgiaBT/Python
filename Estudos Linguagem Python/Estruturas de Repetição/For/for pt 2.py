listanomes = ["Bia", "Paulo", "Andre", "Amanda"]

for posicao in listanomes:
    if posicao == "Paulo":
        continue
    print(posicao)

print("\n")

for i in range(11):
    print(i)

print("\n")
#range(start, stop e step)
#range start = 1, stop = 10, step = 1

for posicao in range(1, 11, 2):
    print("Número: ", posicao)

print("\n")

for i in range(20, 9, -1):
    print("Número: ", i)