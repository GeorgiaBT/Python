import  pandas as opcoespandas

vendasdf = opcoespandas.read_excel("C:\\Users\\georg\\Documents\\Python - GitHub\\Python\\Analise e tratamento de dados com Pandas\\Limitando Exibicao de Linhas e Colunas\\Vendas_Jan.xlsx")
print(vendasdf)
print("\n")

#index exibe apenas informacoes sobre as linhas do data frame
print(vendasdf.index)
print("\n")

#columns exibe o nome de todas aas colunas do dataframe
print(vendasdf.columns)
print("\n")

#head exibe apenas as 5 primeiras linhas (padrao).
print(vendasdf.head())
print("\n")

#head(x) exibe apenas as x primeiras linhas (padrao).
print(vendasdf.head(10))
print("\n")

#tail exibe apenas as 5 ultimas linhas.
print(vendasdf.tail())
print("\n")

#tail(x) exibe apenas as x ultimas linhas.
print(vendasdf.tail(7))
print("\n")

#imprimindo somente a coluna vendedor
print(vendasdf["Vendedor"])
print("\n")

#imprimindo mais de uma coluna
print(vendasdf[["Vendedor", "Total Vendas"]])
print("\n")

#limitando linhas
print(vendasdf.loc[0:3])
print("\n")

#limitando por vendedor
vendasleonardoalmeidadf = vendasdf.loc[vendasdf["Vendedor"] == "Leonardo Almeida"]
print(vendasleonardoalmeidadf)
print("\n")

#limitando por vendedor
vendasleonardoA = vendasdf.loc[vendasdf["Vendedor"] == "Leonardo Almeida", ["Vendedor", "Total Vendas"]]
print(vendasleonardoA)
print("\n")

#vendedor do indice 4
print(vendasdf.loc[4, "Vendedor"])
print("\n")

#shape mostra quantas linhas e colunas tem o dataframe
print(vendasdf.shape)
print("\n")

#transforma linhas em colunas
transformalinhaemcoluna = vendasdf.T

print(transformalinhaemcoluna)
print("\n")




