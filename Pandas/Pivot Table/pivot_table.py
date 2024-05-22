import pandas as pd

baselanchonetedf = pd.read_excel("C:\\Users\\georg\\Documents\\Python - GitHub\\Python\\Pivot Table\\Vendas_Lanchonete_Pivot_Table.xlsx")

print("\n Imprimindo dados \n")
print(baselanchonetedf)
print("\n")

#index = linhas
#columns = colunas
#values = soma/media
#aggfunc = tipo de calculo , sum = soma
pivotex1 = baselanchonetedf.pivot_table(index="Data Venda", columns="Cliente", values="Preço com Desconto", aggfunc="sum")
print("\n Imprimindo data/cliente/preco com desconto \n")
print(pivotex1)
print("\n")

pivotex2 = baselanchonetedf.pivot_table(index="Cliente", columns="Data Venda", values="Preço com Desconto", aggfunc="sum")
print("\n Imprimindo cliente/data/preco com desconto \n")
print(pivotex2)
print("\n")

pivotex3 = baselanchonetedf.pivot_table(index="Data Venda", columns="Cliente", values=["Preço Total", "Preço com Desconto"], aggfunc="sum")
print("\n Imprimindo cliente/preco total/preco com desconto \n")
print(pivotex3)
print("\n")

pivotex4 = baselanchonetedf.pivot_table(index="Data Venda", columns=["Cliente", "Produto"], values=["Preço Total", "Preço com Desconto"], aggfunc="sum")
print("\n Imprimindo cliente/preco total/preco com desconto \n")
print(pivotex4)
print("\n")

pivotex4["Preço com Desconto"] = pivotex4["Preço com Desconto"].fillna(0)
pivotex4["Preço Total"] = pivotex4["Preço Total"].fillna(0)

print("\n Troca NaN por 0 \n")
print(pivotex4)
print("\n")



