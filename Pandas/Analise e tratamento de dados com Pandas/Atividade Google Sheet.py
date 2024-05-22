import pandas as pd


#https://docs.google.com/spreadsheets/d/1uxYa8NKhoPQVAO_LNqNWxyn30qn5S_qD/edit?usp=sharing&ouid=103286032416998039927&rtpof=true&sd=true


planilhaid = "1uxYa8NKhoPQVAO_LNqNWxyn30qn5S_qD"

dadosdf = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{planilhaid}/export?format=csv")

print("\n DataFrame google sheets \n")
print(dadosdf)
print("\n")

deletandocolunas = dadosdf.drop(columns=["Produto", "Data Venda"])
print("\n Excluindo colunas \n")
print(deletandocolunas)
print("\n")

deletandocolunas["Total Vendas"] = deletandocolunas["Total Vendas"].str.replace(",", ".")
deletandocolunas["Total Vendas"] = deletandocolunas["Total Vendas"].astype(float)

resumindocolunas = deletandocolunas.groupby(["Vendedor"]).sum()
print(resumindocolunas)

resumindocolunas.to_csv("Exercicio pandas.csv")