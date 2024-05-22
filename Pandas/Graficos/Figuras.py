import pandas as pd
import matplotlib.pyplot as grafico

frutasdf = pd.read_excel("C:\\Users\\georg\\Documents\\Python - GitHub\\Python\\Graficos\\Base_Grafico.xlsx")

print("\n Data Frame fruta \n")
print(frutasdf)
print("\n")

#tamanho da figura
figura = grafico.figure(figsize=(100, 10))

frutas = frutasdf["Frutas"]
total = frutasdf["Total Vendas"]

def graficoConfig(k):

    grafico.legend()
    grafico.title("Grafico "+str(k))
    grafico.annotate(frutas[0], (frutas[0], total[0]))
    grafico.annotate(frutas[1], (frutas[1], total[1]))
    grafico.annotate(frutas[2], (frutas[2], total[2]))
    grafico.annotate(frutas[3], (frutas[3], total[3]))
    grafico.annotate(frutas[4], (frutas[4], total[4]))
    grafico.xticks([])
    return k

#1 - linha  3- colunas  1-posicao do grafico
#add_subplot adiciona um grafico na parte de uma figura
figura.add_subplot(231)
grafico.plot(frutas, total, label="plot")
graficoConfig(1)

figura.add_subplot(232)
grafico.bar(frutas, total, label="plot")
graficoConfig(2)

figura.add_subplot(233)
grafico.pie(total, labels= frutas)
#nao aceita legenda
grafico.title("Grafico 3")

figura.add_subplot(235)
grafico.stem(frutas, total, label="plot")
graficoConfig(4)

grafico.savefig("figuragrafico.png")

grafico.show()