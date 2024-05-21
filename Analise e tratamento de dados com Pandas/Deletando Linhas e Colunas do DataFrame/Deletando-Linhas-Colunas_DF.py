import pandas as pd

dataframedados = pd.read_excel("C:\\Users\\georg\\Documents\\Python - GitHub\\Python\\Analise e tratamento de dados com Pandas\\Deletando Linhas e Colunas do DataFrame\\Deletar_Linhas_Colunas.xlsx")
print(dataframedados)
print("\n")
print(type(dataframedados))
print("\n")

#dropna deleta linhas que tenham pelo menos um valor em branco
deletandolinhasembranco = dataframedados.dropna()

print("\n")
print(deletandolinhasembranco)
print("\n")

#del deleta a coluna
del deletandolinhasembranco["Produto"]

print("\n")
print(deletandolinhasembranco)
print("\n")

deletarduascolunas =deletandolinhasembranco.drop(columns=["Data Venda", "Total Vendas"])

print("\n")
print(deletarduascolunas)
print("\n")

excluilinha3 = deletarduascolunas.drop(2, axis=0)

print("\n")
print(excluilinha3)
print("\n")

excluirmaislinhas= excluilinha3.drop([0, 1])

print("\n")
print(excluirmaislinhas)
print("\n")


