import pandas as pd

vendasdf = pd.read_excel("C:\\Users\\georg\\Documents\\Python - GitHub\\Python\\Pandas(Merge)\\GROUPBY\\Groupby.xlsx")

print("\n DataFrame Vendas \n")
print(vendasdf)
print("\n")

mediavendedor = vendasdf.groupby(["Vendedor"]).mean(numeric_only=True)
print("\n Média \n")
print(mediavendedor)
print("\n")

somavendedor = vendasdf.groupby(["Vendedor"]).sum(numeric_only=True)
print("\n Soma \n")
print(somavendedor)
print("\n")

deixandovaloresembranco = vendasdf.groupby(by=["Vendedor"], dropna=False).sum(numeric_only = True)
print("\n Deixando valores em branco \n")
print(deixandovaloresembranco)
print("\n")

removevaloresembranco = vendasdf.groupby(by=["Vendedor"], dropna=True).sum(numeric_only = True)
print("\n Remove valores em branco \n")
print(removevaloresembranco)
print("\n")

agrupaduascolunas = vendasdf.groupby(["Vendedor", "Produto"]).sum(numeric_only= True)
print("\n Agrupa duas colunas \n")
print(agrupaduascolunas)
print("\n")

agrupafrutasvendedor = vendasdf.groupby(["Produto", "Vendedor"]).sum(numeric_only= True)
print("\n Agrupa frutas e vendedor \n")
print(agrupafrutasvendedor)
print("\n")

agrupadatavendedor = vendasdf.groupby(["Data Venda", "Vendedor"]).sum(numeric_only= True)
print("\n Agrupa data e vendedor \n")
print(agrupadatavendedor)
print("\n")
