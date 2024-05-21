import pandas as opcoespandas

vendasjaneirodf = opcoespandas.read_excel("C:\\Users\\georg\\Documents\\Python - GitHub\\Python\\Analise e tratamento de dados com Pandas\\Mesclando DataFrame\\Vendas_Jan.xlsx")

print("DataFrame vendas Janeiro")
print(vendasjaneirodf)
print("\n")

vendasfevereirodf = opcoespandas.read_excel("C:\\Users\\georg\\Documents\\Python - GitHub\\Python\\Analise e tratamento de dados com Pandas\\Mesclando DataFrame\\Vendas_Fev.xlsx")

print("DataFrame vendas Fevereiro")
print(vendasfevereirodf)
print("\n")

#append unindo os dois arquivos
# append / concat
vendasjaneirodf = vendasjaneirodf._append(vendasfevereirodf)

print("DataFrame Jan e Fev")
print(vendasjaneirodf)
print("\n")

vendasmarcodf = opcoespandas.read_excel("C:\\Users\\georg\\Documents\\Python - GitHub\\Python\\Analise e tratamento de dados com Pandas\\Mesclando DataFrame\\Vendas_Mar.xlsx")

print("DataFrame vendas Março")
print(vendasmarcodf)
print("\n")

vendasgeraldf = opcoespandas.concat(([vendasjaneirodf, vendasfevereirodf, vendasmarcodf]))
print("DataFrame vendas Jan, Fev e Mar")
print(vendasgeraldf)
print("\n")

resumindodfgeral = vendasjaneirodf[["Vendedor", "Data Venda", "Total Vendas"]]
print("Imprimindo 3 colunas do DF geral")
print(resumindodfgeral)
print("\n")

vendasgeralcomgrupos = opcoespandas.concat([vendasjaneirodf, vendasfevereirodf, vendasmarcodf], keys=["Janeiro", "Fevereiro", "Março"])
print("DF geral com grupos")
print(vendasgeralcomgrupos)
print("\n")

extraindofev = vendasgeralcomgrupos.loc["Fevereiro"]
print("Imprimindo fevereiro")
print(extraindofev)
print("\n")