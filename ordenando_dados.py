import pandas as pd
import numpy as np

df = pd.DataFrame({'Col1': ['A', 'A', 'B', np.nan, 'D', 'C'],
                   'Col2': [2, 1, 9, 8, 7, 4],
                   'Col3': [0, 1, 9, 4, 2, 3]})
print(df)

#Ordenando os dados:
print(df.sort_values(by = 'Col2'))
#by = por onde começará, por qual coluna por ex

#Ordenando os dados por várias colunas:
print(df.sort_values(by = ['Col2', 'Col1']))

#Modificando a forma de ascendente para descendente:
print(df.sort_values(by = ['Col3'], ascending = False))
