import pandas as pd

loja1df = pd.read_excel("C:\\Users\\georg\\Documents\\Python - GitHub\\Python\\Pandas(Merge)\\JOIN FULL\\Vendedores_Join_Full_Loja1.xlsx")

print("\n Vendedores loja 1 \n")
print(loja1df)
print("\n")

loja2df = pd.read_excel("C:\\Users\\georg\\Documents\\Python - GitHub\\Python\\Pandas(Merge)\\JOIN FULL\\Vendedores_Join_Full_Loja2.xlsx")

print("\n Vendedores loja 2 \n")
print(loja2df)
print("\n")

#concat une os arquivos
vendasloja1e2df = pd.concat([loja1df, loja2df])
print("\n Junção Lojas \n")
print(vendasloja1e2df)
print("\n")

semvendedoresduplicados = vendasloja1e2df.drop_duplicates(subset="Id Vendedor")

print("\n Junção Lojas sem itens duplicados \n")
print(semvendedoresduplicados)
print("\n")


