#Data Wrangling
#Limpeza e estruturação de dados

import pandas as pd
import numpy as np

datas = pd.date_range('20200101', periods = 6)
#print(datas)

df = pd.DataFrame(np.random.randn(6, 4), index = datas, columns = ['Var_A', 'Var_B', 'Var_C', 'Var_D'])
print(df)
print(df.shape)
print(df.dtypes)

df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index = list(range(4)), dtype = 'float32'),
                    'D': np.array([3] * 4, dtype = 'int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'Python'})
print(df2)
print(df2.shape)
print(df2.dtypes)

