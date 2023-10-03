import pandas as pd
import numpy as np

datas = pd.date_range('20180101', periods = 600, freq = "D")
df = pd.DataFrame(np.random.randn(600, 5), index = datas, columns = list("ABCDE"))

#print(datas)
#print(df)
#print(df.head(2)) #pegando só duas linhas de resultado

#Obtendo todos os dados da coluna D:
#print(df['D'].head(5)) #com o head(5) obtem-se apenas as cinco primeiras

#Obtendo dados de uma linha até outra, especificamente:
#print(df[1:5])

#-------------

#Obtendo dados das colunas B, C e D:
#print(df.loc[:, ['B', 'C', 'D']])
#o dois pontos (:) antes da vírgula busca todas linhas das colunas

#-------------

#Buscando dados a partir das datas:
#print(df.loc['20180301' : '20180917', ['A', 'E']].head(4))


#-------------

#Saber quantos dias há entre as datas:
f =df.loc['20180301' : '20180917', ['A', 'E']]
#print(len(f))


#Coletando linhas específicas:
#print(df.iloc[15])


#Coletando linhas e colunas específicas:
#print(df.iloc[2 : 4, 0 : 2]) #linha 2 a 4, coluna de indice 0 a 2


#Coletando conjuntos de linhas/posições específicas:
#print(df.iloc[[1,5,6], [0,3]])


#Coletando dados de outra forma:
print(df.iloc[1:3, :]) #da linha 1 a 3 e todas (:) as colunas





















