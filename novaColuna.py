import pandas as pd
import numpy as np

datas = pd.date_range('20190101', periods = 60, freq = "D")
df = pd.DataFrame(np.random.randn(60, 5), index = datas, columns = list("ABCDE"))
#print(df)
#print(df.shape) #fornece a dimensão do DF
print(df.head(3)) #Visualiza os 3 primeiros da lista
print(df.tail(3)) #Visualiza os 3 ultimos da lista

#df['F'] = range(60) #adiciona nova coluna com valores de 0 a 59
#print(df)

#Multiplicando valores de colunas e adicionando numa nova
#df['Produto']  = df['A'] * df['B']
#print(df.head(3))

#print(df.index)#busca os indices
#print(df.columns) #busca as colunas
#print(df.to_numpy()) #busca somente os valores
print(df.T) #transforma linha em coluna e coluna em linha




