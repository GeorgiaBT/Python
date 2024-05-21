from re import M

import  pandas as opcoespandas
import numpy as opcoesnumpy

#daterange = lista
#202212201 = ano/mes/dia
#periods = qnts dias
dataFrameDatas = opcoespandas.date_range("20221201", periods=31)
print(dataFrameDatas)

print("\n")
dataframemeses = opcoespandas.date_range("20221231", periods=12, freq="ME")
print(dataframemeses)

print("\n")
numerosaleatorios = opcoespandas.DataFrame(opcoesnumpy.random.rand(5, 1))
print(numerosaleatorios)

print("\n")
numerosaleatorios = opcoespandas.DataFrame(opcoesnumpy.random.rand(15, 10)*100)
print(numerosaleatorios)

#colocar titulo nas colunas
print("\n")
numerosaleatorios = opcoespandas.DataFrame(opcoesnumpy.random.rand(15, 10)*100, columns=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"])
print(numerosaleatorios)

print(numerosaleatorios.columns)

#criando um dataframe a partir de um dicionario
notasalunosdataframe = opcoespandas.DataFrame({
                                            "Nome": ["Ana", "Pedro", "João"],
                                            "Média": [9, 7, 10]
                                                })

print("\n")
print(notasalunosdataframe)