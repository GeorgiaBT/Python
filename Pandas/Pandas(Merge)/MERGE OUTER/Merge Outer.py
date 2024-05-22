import pandas as pd

vendasloja1df = pd.read_excel("C:\\Users\\georg\\Documents\\Python - GitHub\\Python\\Pandas(Merge)\\MERGE OUTER\\Outer_Vendas_Loja1.xlsx")

print("\n Vendas loja 1 \n")
print(vendasloja1df)
print("\n")

vendasloja2df = pd.read_excel("C:\\Users\\georg\\Documents\\Python - GitHub\\Python\\Pandas(Merge)\\MERGE OUTER\\Outer_Vendas_Loja2.xlsx")

print("\n Vendas loja 2 \n")
print(vendasloja2df)
print("\n")

verificandovendasdf = pd.merge(vendasloja1df, vendasloja2df, on=["Id Vendedor"], how="outer", suffixes=(" Loja 1", " Loja 2"))

print("\n Juntando dados com o outer e verificando os vendedores que venderam em ambas as lojas \n")
print(verificandovendasdf)
print("\n")

tratandodadosdf = verificandovendasdf.dropna()

print("\n Removendo linhas com NaN \n")
print(tratandodadosdf)
print("\n")

del tratandodadosdf["Vendedor Loja 2"]

print("\n Removendo Vendedor Loja 2 \n")
print(tratandodadosdf)
print("\n")


