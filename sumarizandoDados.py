#Data Wrangling
#Limpeza e estruturação de dados

import pandas as pd
import numpy as np

datas = pd.date_range('20200101', periods = 6)
#print(datas)

df = pd.DataFrame(np.random.randn(6, 4), index = datas, columns = ['Var_A', 'Var_B', 'Var_C', 'Var_D'])
#print(df)
#print(df.shape)
#print(df.dtypes)

df2 = pd.DataFrame({'A': 1., #caso não seja determinado o tamanho, será o padro float64, diferente do 'c' onde foi determinado float32
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index = list(range(4)), dtype = 'float32'),
                    'D': np.array([3] * 4, dtype = 'int32'), #se não fosse determinado, o tamanho seria dtype = int64
                    'E': pd.Categorical(["test", "train", "test", "train"]), #tipo de dados: categoria
                    'F': 'Python'})
#print(df2)
#print(df2.shape)
#print(df2.dtypes)


#Fazendo a sumarização(resumo dos dados)
#print(df2.describe())
#describe serve apenas para dados numéricos.

#Outro exemplo (Reindex)
df1 = df.reindex(index = datas[0:4], columns = list(df.columns) + ['Var_E'])
print(df1)
#reindex = mudança de indexação do 'df'
#pegando apenas as 3 primeiras linhas do index 'data' [0:4]
#guardando numa coluna 'list'
#adicionando uma coluna a mais 'Var_E'


#Adicionando valores na coluna Var_E
df1.loc[datas[0] : datas[1], 'Var_E'] = 77
print(df1)
print(df1.dtypes)
print(df1.describe())
#da linha (data) 0 até a 1, adiciona o valor 77 à 'Var_E'
#ou seja, linhas de 0 a 1, coluna E, mude o valor para 77


#LEMBRANDO QUE O QUE VEM ANTES DA VÍRGULA SÃO LINHAS E O QUE VEM DEPOIS, SÃO COLUNAS!!!
























