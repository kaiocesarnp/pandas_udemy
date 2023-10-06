#Abrindo/importando arquivos de dados externos

import pandas as pd

d = pd.read_csv('c:/users/inss/desktop/k/iris/iris.data')
print(d.head(3))
print(d.dtypes)
print(d.shape)
print(d.describe())
