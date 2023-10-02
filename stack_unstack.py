#Funlçao StacK (pilha)
#Empilhar os dados, um abaixo do outro

import pandas as pd

df = pd.read_csv("https://cdncontribute.geeksforgeeks.org/wp-content/uploads/nba.csv")
#print(df.head(4)) #pega somente as 4 primeiras linhas de dados
#print(df.shape) #tamanho
#read_csv = leitura de csv


#Empilhando dados com stack
stack_df = df.stack()
print(stack_df)


#Retornando os dados originais
udf = stack_df.unstack()
print(udf.head(3))
