#Reshaping
#Reformular, organizar os dados. Transformar os dados em um formato para outro

import pandas as pd
import numpy as np

datas = pd.date_range('20200101', periods = 6)
df = pd.DataFrame(np.random.randn(6, 4), #6 linhas por 4 colunas
                index = datas, columns = ['Var_A', 'Var_B', 'Var_C', 'Var_D'])
#print(df)

#Transformar nomes das colunas nas datas, ao invés dos 'Vars'
dft = df.T #T = transpor
#print(dft)

#Descobrir o formato de um conjunto de dados
#shape é um atributo do DF e não um método, por isso não é necessário '()'
dfs = df.shape
#print(dfs)

#Nesse caso - pegando o modelo dft - o que é coluna vira linha e vice-versa:
#print(dft.shape)

#Reshaping em cima dos valores numéricos:
#print(dft.values)

#Descobrir tamanho:
#print(np.size(dft.values)) # 4 vezes 6

#Reogarnizando de outra forma:
v = dft.values
print(v.reshape(2, 12)) #2 linhas por 12 colunas, ou seja, 24 o tamanho, referenciando 4 vezes 6
