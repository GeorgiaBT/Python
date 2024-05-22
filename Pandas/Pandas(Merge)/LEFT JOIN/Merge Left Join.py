import pandas as pd

#PROCV - puchar uma informação de outra tabela

vendasdf = pd.read_excel("C:\\Users\\georg\\Documents\\Python - GitHub\\Python\\Pandas(Merge)\\LEFT JOIN\\Vendas_LEFT_JOIN.xlsx")

print("\n Vendas loja \n")
print(vendasdf)
print("\n")

vendedoresdf = pd.read_excel("C:\\Users\\georg\\Documents\\Python - GitHub\\Python\\Pandas(Merge)\\LEFT JOIN\\Vendedores_LEFT_JOIN.xlsx")

print("\n Vendedores loja \n")
print(vendedoresdf)
print("\n")

#left = trazer os dados pela esquerda
verificandovendasdf = pd.merge(vendasdf, vendedoresdf, on="Id Vendedor", how="left")

print("\n  Merge Left Join \n")
print(verificandovendasdf)
print("\n")

verificandovendasdf2 = pd.merge(vendasdf, vendedoresdf, on="Id Vendedor", how="left", suffixes=(" Vendas", " Checagem"))

print("\n  Merge Left Join \n")
print(verificandovendasdf2)
print("\n")

tratamentodadosdf = pd.merge(vendasdf, vendedoresdf, on="Id Vendedor", how="left", suffixes=(" Vendas", " Checagem"))

tratamentodadosdf = tratamentodadosdf.dropna()

print("\n  Removendo linhas com NaN \n")
print(tratamentodadosdf)
print("\n")

del tratamentodadosdf["Vendedor Checagem"]

print("\n  Removendo coluna Vendedor Checagem \n")
print(tratamentodadosdf)
print("\n")