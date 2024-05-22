import pandas as pd

dadosdf = pd.read_excel("C:\\Users\\georg\\Documents\\Python - GitHub\\Python\\Analise e tratamento de dados com Pandas\\Tratamento de dados\\Tratamento_Dados.xlsx")
print(dadosdf)
print("\n")

#ffilna preenche os valores vazios com a média

#substitui vazio por media
#dadosdf["Total Vendas"] = dadosdf["Total Vendas"].fillna(dadosdf["Total Vendas"].mean())

#substitui vazio por 5
#dadosdf["Total Vendas"] = dadosdf["Total Vendas"].fillna(5)

#ffil preenche com o ultimo registro valido encontrado
dadosdf["Total Vendas"] = dadosdf["Total Vendas"].ffill()

print(dadosdf)
print("\n")

#value_counts conta quantas linhas/vendas foram feitas
qtdvendas = dadosdf["Vendedor"].value_counts()

print(qtdvendas)
print("\n")

vendavendedor = dadosdf.groupby("Vendedor").sum
print(vendavendedor)
print("\n")