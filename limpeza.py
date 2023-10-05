#Verificando se há dados repetidos no DF


import pandas as pd
import numpy as np

df2 = pd.DataFrame({'A': 1., #caso não seja determinado o tamanho, será o padro float64, diferente do 'c' onde foi determinado float32
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index = list(range(4)), dtype = 'float32'),
                    'D': np.array([3] * 4, dtype = 'int32'), #se não fosse determinado, o tamanho seria dtype = int64
                    'E': pd.Categorical(["test", "train", "test", "train"]), #tipo de dados: categoria
                    'F': 'Python',
                    'G': [2, 2, 4, 4],
                    'H': [np.nan, 2, 4, np.nan]})
print(df2)


#Verificando se há dados repetidos:
print(df2.nunique(dropna = False))
#como padrão, o 'nunique' vem com 'dropna = true', o que exclui elementos "NaN".
    #sendo possível modificar para 'false' e assim contabilizar "NaN" como um valor também

#axis=0: A contagem de valores únicos é realizada ao longo das colunas.
#axis=1: A contagem de valores únicos é realizada ao longo das linhas.
