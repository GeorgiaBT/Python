import pandas as pd

vendasdf = pd.read_excel("C:\\Users\\georg\\Documents\\Python - GitHub\\Python\\Pandas(Merge)\\MERGE\\Vendas_Merge.xlsx")
print("\n DataFrame vendas \n")
print(vendasdf)
print("\n")

vendedoresdf = pd.read_excel("C:\\Users\\georg\\Documents\\Python - GitHub\\Python\\Pandas(Merge)\\MERGE\\Vendedores_Merge.xlsx")
print("\n DataFrame vendedores \n")
print(vendedoresdf)
print("\n")

produtosdf = pd.read_excel("C:\\Users\\georg\\Documents\\Python - GitHub\\Python\\Pandas(Merge)\\MERGE\\Produtos_Merge.xlsx")
print("\n DataFrame produtos \n")
print(produtosdf)
print("\n")

#merge tras informacao de outros df para o df atual
vendasdf = vendasdf.merge(vendedoresdf)

print("\n merge DataFrame vendas X vendedores\n")
print(vendasdf)
print("\n")


vendasdf = vendasdf.merge(produtosdf)

print("\n merge DataFrame vendas X produtos\n")
print(vendasdf)
print("\n")

print(vendasdf.columns)
print("\n")

resumodf = vendasdf[["Vendedor", "Produto", "Total Vendas"]]

print("\n merge DataFrame resumo\n")
print(resumodf)
print("\n")
