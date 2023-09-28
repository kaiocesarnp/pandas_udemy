import pandas as pd

arrays = [[1, 1, 2, 2], ['red', 'blue', 'red', 'blue']]
#print(pd.MultiIndex.from_arrays(arrays, names = ('number', 'color')))


#Função multiIndex From product

numbers = [0, 1, 2]
colors = ['green', 'purple']

print(pd.MultiIndex.from_product([numbers, colors],
                           names = ['number', 'color']))
