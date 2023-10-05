#Dados faltantes

import pandas as pd
import numpy as np

datas = pd.date_range('20190101', periods = 60, freq = "D")
#print(datas)

df = pd.DataFrame(np.random.randn(60, 5), index = datas, columns = list("ABCDE"))
#print(df.head(3))

#Gerando uma coluna nova com valores da coluna 'A' que são maiores que 0
df['F'] = df.A[df.A > 0]
#print(df.head(3))


#Substituindo os valores "NaN" por um valor qualquer:
df2 = df.copy()
#print(df2.dropna()) #dropna = remover, tirar valores NaN. E também a linha inteira, mesmo outra coluna(B por ex) tendo valor

#Substituindo os valore "NaN" da coluna 'F' pela média dos valores de outra coluna (A por ex):
df3 = df.copy()
#print(df3.F.fillna(np.mean(df3.A))) #fillna = preencher, na = NaN, ou seja, preencha os valores NaN

#Substituindo os valores "NaN" por um nº específico (777)
df4 = df.copy()
print(df4.fillna(value = 777))
