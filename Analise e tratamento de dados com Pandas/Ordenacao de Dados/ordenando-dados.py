import pandas as pd

basevendasdf = pd.read_excel("C:\\Users\\georg\\Documents\\Python - GitHub\\Python\\Analise e tratamento de dados com Pandas\\Ordenacao de Dados\\Ordenação.xlsx")

print("\n Imprimindo dados \n")
print(basevendasdf)
print("\n")

#sort ordena as colunas
#by seleciona a coluna
ordenarvendedor = basevendasdf.sort_values(by="Vendedor")
print(ordenarvendedor)
print("\n")

ordenarprodutos = basevendasdf.sort_values(by="Produto")
print(ordenarprodutos)
print("\n")

ordenardata = basevendasdf.sort_values(by="Data Venda")
print(ordenardata)
print("\n")

ordenartotal = basevendasdf.sort_values(by="Total Vendas")
print(ordenartotal)
print("\n")

ordenarduascolunas = basevendasdf.sort_values(by=["Vendedor", "Produto"])
print(ordenarduascolunas)
print("\n")

#ascending ordena de forma crescente (true) ou decrescente (False)
ordenarZaA = basevendasdf.sort_values(by="Vendedor", ascending=False)
print(ordenarZaA)
print("\n")

ordenartotalvendasZaA = basevendasdf.sort_values(by="Total Vendas", ascending=False)
print(ordenartotalvendasZaA)
print("\n")


