import pandas as opcoespandas

notasalunosdf = opcoespandas.DataFrame({
    "Nome": ["Ana", "Pedro", "Jõao"],
    "Nota 1": [9, 8, 10],
    "Nota 2": [8, 7, 6],
    "Nota 3": [8, 9, 3],
    "Nota 4": [4, 6, 7]
})

print("Dicionario notas aluno")
print(notasalunosdf)
print("\n")

notasalunosdf["Média"] = (notasalunosdf["Nota 1"] + notasalunosdf["Nota 2"] + notasalunosdf["Nota 3"] + notasalunosdf["Nota 4"])/4
print("\n DataFrame com média")
print(notasalunosdf)

notasalunosdf["Faltas"]= 5
print("\n Faltas com valor padrao")
print(notasalunosdf)

novasfaltas = [2, 5, 3]
print(type(novasfaltas))

notasalunosdf["Faltas"] = novasfaltas
print("\n Substituindo valores na coluna de faltas atraves de uma lista")
print(notasalunosdf)

notasalunosdf.loc[1, "Nota 2"] = 12
print("\n Alterando a nota 2 do aluno pedro")
print(notasalunosdf)

notasalunosdf["Média"] =  (notasalunosdf["Nota 1"] + notasalunosdf["Nota 2"] + notasalunosdf["Nota 3"] + notasalunosdf["Nota 4"])/4
print("\n Recalculando a média")
print(notasalunosdf)
