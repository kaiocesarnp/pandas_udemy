import pandas as pd
import numpy as np

df = pd.DataFrame({'A': ['verdadeiro', 'falso', 'verdadeiro', 'falso',
                         'verdadeiro', 'falso', 'verdadeiro', 'falso'],
                   'B': ['um', 'um', 'dois', 'tres',
                         'dois', 'dois', 'um', 'tres'],
                   'C': np.random.randn(8), #gera numeros aleatórios
                   'D': np.random.randn(8)})
#print(df)

#Fazendo a estatistica descritiva por grupos, no caso a coluna A, depois a B, soma(sum)
print(df.groupby(['A']).sum())
print(df.groupby(['B']).sum())

#Agrupamento de duas ou mais colunas:
print(df.groupby(['A', 'B']).max())
