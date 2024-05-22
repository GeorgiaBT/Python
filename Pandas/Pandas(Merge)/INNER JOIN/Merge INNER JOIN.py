import  pandas as pd

loja1df = pd.read_excel("C:\\Users\\georg\\Documents\\Python - GitHub\\Python\\Pandas(Merge)\\INNER JOIN\\Vendas_+INNER_JOIN_Loja1.xlsx")
print("\n Vendas Loja 1 \n")
print(loja1df)
print("\n")

loja2df = pd.read_excel("C:\\Users\\georg\\Documents\\Python - GitHub\\Python\\Pandas(Merge)\\INNER JOIN\\Vendas_+INNER_JOIN_Loja2.xlsx")
print("\n Vendas Loja 2 \n")
print(loja2df)
print("\n")

#inner faz o merge entre as duas tabelas
#on = qual coluna
#how = como
vendedoresambaslojasdf = pd.merge(loja1df, loja2df, on=["Vendedor"], how="inner")

#_x = loja 1
#_y = loja 2
print("\n Vendedores que venderam em ambas as lojas \n")
print(vendedoresambaslojasdf)
print("\n")

#exibiu os nomes das colunas
print(vendedoresambaslojasdf.columns.values.tolist())

#suffixes = nome das colunas
vendedoresresumo = pd.merge(loja1df, loja2df[["Vendedor", "Total Vendas"]], on=["Vendedor"], how="inner", suffixes= (" Loja 1", " Loja 2"))

print("\n Resumo vendedores \n")
print(vendedoresresumo)

resumo = vendedoresresumo[["Vendedor", "Total Vendas Loja 1", "Total Vendas Loja 2"]]

print("\n Resumo \n")
print(resumo)
