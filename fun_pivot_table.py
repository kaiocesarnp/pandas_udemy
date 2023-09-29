#Função Pivot Table

#Diferença entre Pivot e Pivot Table:
#A pivot não pode usar de referência o index com dados repetidos (iguais valores)
#A pivot pode

import pandas as pd

Carros = [7, 4, 3, 2, 8]
dias = pd.date_range('20190101', '20190101', periods = 5)
vendedor = ['George', 'Vagner', 'Pedro', 'Vagner', 'George']

df = pd.DataFrame({'Vendas': Carros, 'Data': dias, 'Vendedor': vendedor})
print(df)

#Usando a função pivot table com o index repetido
pivot = pd.pivot_table(df, index = 'Data', columns = 'Vendedor', values = 'Vendas')
print(pivot)

#O numero de vendas é dividido pelo tanto de vezes que o nome do vendedor aparece
    #no DF, por isso são numeros 'quebrados' (floats)
