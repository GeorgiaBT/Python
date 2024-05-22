listanome = ["Bryan","Leticia","Allan", "Bruna", "Simone", "Carla"]

for posicao in listanome:
    print(posicao)

print("\n\n")

[print(item) for item in listanome]

print("\n\n")

i = 0

while i < len(listanome):
    print(listanome[i])
    i = i + 1

print("\n\n")

listanomecomc = []

for item in listanome:
    if "c" in item:
        listanomecomc.append(item)

print(listanomecomc)

print("\n\n")

listamaiuscula = [item.upper() for item in listanome]
print(listanome)
print(listamaiuscula)

listaminuscula = [item.lower() for item in listanome]
print(listanome)
print(listaminuscula)