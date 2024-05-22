import pandas as pd
import matplotlib.pyplot as grafico

frutasdf = pd.read_excel("C:\\Users\\georg\\Documents\\Python - GitHub\\Python\\Graficos\\Base_Grafico.xlsx")

print("\n Data Frame fruta \n")
print(frutasdf)
print("\n")

frutas = frutasdf["Frutas"]
total = frutasdf["Total Vendas"]

#plot = grafico de linhas
#label = legenda
#linestyle = : pontilhada
#lw = largura linha
grafico.plot(frutasdf["Frutas"], frutasdf["Total Vendas"], label="Total Vendas", linestyle="--", lw="2", color="b")
grafico.legend() #legend exibe a legenda
grafico.title("Vendas Frutas") #title cria um titulo
grafico.xlabel("Nome das frutas") #xlabel = descricao eixo x
grafico.ylabel("Total de vendas") #ylabel = descricao eixo y
grafico.xticks(([0,1,2,3,4])) #escala de numeros eixo x
grafico.yticks(([0,10,20,30,40, 50, 60, 70, 80, 90, 100])) #escala de numeros eixo y
grafico.axis(xmin=0, xmax=4, ymin=0, ymax=80) #Define maximo e minimo para o eixo x e y
grafico.axis("auto") #ajusta eixo x e y de forma automatica
#grafico.annotate("Abacate",(0,10)) #anotação
#grafico.annotate("Banana",(1,52)) #anotação

for k in range(4):

    grafico.annotate(total[k], (frutas[k], total[k]))
    k+1

grafico.savefig("imagemGrafico.png")



#cria e apresenta o grafico
grafico.show()