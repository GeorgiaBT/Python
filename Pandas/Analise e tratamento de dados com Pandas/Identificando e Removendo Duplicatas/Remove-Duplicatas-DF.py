import pandas as pd

basevendasdf = pd.read_excel("C:\\Users\\georg\\Documents\\Python - GitHub\\Python\\Analise e tratamento de dados com Pandas\\Identificando e Removendo Duplicatas\\Base_Vendas.xlsx")

print("\nImprimindo os dados\n")
print(basevendasdf)
print("\n")

#nunique conta quantos valores unicos tem
resumovaloresunicos = basevendasdf.nunique()

print(resumovaloresunicos)
print("\n")

#subset identifica a coluna que queremos verificar a duplicidade
#keep controla como considerar o valor da duplicidade (first, last, False)
confereduplicidades = basevendasdf.duplicated(subset="Vendedor", keep="first")

print(confereduplicidades)
print("\n")

basevendasdf["Confere duplicidade"] = basevendasdf.duplicated(subset="Vendedor", keep="first")

print(basevendasdf)
print("\n")

removerduplicidade = basevendasdf.drop_duplicates(subset="Vendedor", keep= "first")

print(removerduplicidade)
print("\n")


