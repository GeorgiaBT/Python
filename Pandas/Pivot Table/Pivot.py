import pandas as pd

baselanchonetedf = pd.read_excel("C:\\Users\\georg\\Documents\\Python - GitHub\\Python\\Pivot Table\\Vendas_Lanchonete_Pivot.xlsx")

print("\n Imprimindo Dados \n")
print(baselanchonetedf)
print("\n")

pivotexemplo1 = baselanchonetedf.pivot(index="Data Venda", columns="Cliente", values="Preço com Desconto")
print("\n Imprimindo clientes/ preço com desconto \n")
print(pivotexemplo1)
print("\n")

#pivot não aceita valores repetidos
pivotexemplo2 = baselanchonetedf.pivot(index="Cliente", columns="Data Venda", values="Preço com Desconto")
print("\n Imprimindo clientes/ preço com desconto \n")
print(pivotexemplo2)
print("\n")