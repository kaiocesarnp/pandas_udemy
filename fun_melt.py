#Função Melt
#Fundir, juntar, unir, agrupar, combinar

import pandas as pd

df = pd.DataFrame({'A': {0: 'a', 1: 'b', 2: 'c'},
                    'B': {0: 1, 1: 3, 2: 5},
                   'C': {0: 2, 1: 4, 2: 6}})

#print(df)

#Melt
mlt = pd.melt(df, id_vars = ['A'], value_vars = ['B'])
#print(mlt)

#id_vars = Refernciação de 'id' = variável(vars) A;
#value_vars = valores da variável B

#Melt 2
mlt2 = pd.melt(df, id_vars = ['A'], value_vars = ['B', 'C'], var_name = 'VarTeste', value_name = 'Nome do Valor')
print(mlt2)
