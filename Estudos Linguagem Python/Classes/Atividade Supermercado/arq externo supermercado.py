import supermercado as sp

sp.supermercadodef()

print(sp.produtos["Arroz"])

from supermercado import produtos

print(produtos["Feijão"])

#imprimindo o titulo
for posicao in produtos:
    print(posicao)

print("\n")

#imprimindo os precos
for i in produtos:
    print(produtos[i])

#imprimindo produto e preco
for prod, prec in produtos.items():
    print(prod, "-", prec)

from supermercado import departamento

for produto, preco in departamento.items():
    print(produto)
    for produto, preco in preco.items():
        print("Produto:", produto, "R$", preco)