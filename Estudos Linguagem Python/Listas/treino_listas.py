frutas = ["maça", "banana", "manga", "abacate", "laranja"]

print(frutas)

frutas.append("kiwi")
print(frutas)

frutas.remove("banana")
print(frutas)

if "abacaxi" in frutas:
    print("Abacaxi esta na lista")
else:
    print("Abacaxi não está na lista")

print(frutas[0])
print(frutas[-1])