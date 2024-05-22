import pandas as pd
from datetime import date
import numpy as np

arquivoaniversario = pd.read_excel("C:\\Users\\georg\\Downloads\\Aniversario.xlsx")

arquivoaniversario["Nascimento"] = arquivoaniversario["Nascimento"].astype(str)

#criando a coluna ano
arquivoaniversario["Ano"] = arquivoaniversario["Nascimento"].str[:4]

arquivoaniversario["Mês"] = arquivoaniversario["Nascimento"].str[5:7]

arquivoaniversario["Dia"] = arquivoaniversario["Nascimento"].str[-2:]

arquivoaniversario["Data Atual"] = date.today()

arquivoaniversario["Data Atual"] = arquivoaniversario["Data Atual"].astype(str)

arquivoaniversario["Ano Atual"] = arquivoaniversario["Data Atual"].str[:4]

arquivoaniversario["Mês Atual"] = arquivoaniversario["Data Atual"].str[5:7]

arquivoaniversario["Dia Atual"] = arquivoaniversario["Data Atual"].str[-2:]

arquivoaniversario["Aniversário"] = np.where((arquivoaniversario["Mês"] == arquivoaniversario["Mês Atual"]) &
                                              (arquivoaniversario["Dia"] == arquivoaniversario["Dia Atual"]), "Sim", "")

#filtra somente os aniversariantes do dia
arquivoaniversario = arquivoaniversario.loc[arquivoaniversario["Aniversário"] != "", ["Nome", "Nascimento", "Email"]]

print(arquivoaniversario)

for linha in range(len(arquivoaniversario)):

    print(arquivoaniversario.iloc[linha,2])