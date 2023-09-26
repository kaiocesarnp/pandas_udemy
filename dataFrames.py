import pandas as pd
import numpy as np

"""
series = pd.Series([7, 4, 2, np.nan, 6, 9])
print(series)
print(type(series))

#a funçao 'range' permite gerar/obter datas no decorrer periodos
#a função 'periods' está relacionada a quantos periodos serão mostrados
datas = pd.date_range('20180101', periods = 6, freq = "D")
#print(datas)
#print(type(datas))

#no resultado (print), a frequencia(representada por 'freq') indica que é por dias
#freq = 'D', sendo possível mudá-la, por ex: freq = 'M', de mês/month
#utilize o help para obter outras formas
#help(pd.date_range)

df = pd.DataFrame(np.random.randn(6, 4), index = datas, columns = list("ABCD"))
#print(np.random.randn(6, 4)) #seis linhas, quatro colunas
print(df)
print(type(df))

#---------------------

"""

#Criando um novo DataFrame

df2 = pd.DataFrame({
    "A":7,
    "B": pd.Timestamp('20190101'),
    "C": pd.Series(1, index = list(range(4)), dtype = 'float32'),
    "D": np.array([3] * 4, dtype = 'int32'),
    "E": pd.Categorical(["test", "train", "test", "train"]),
    "F": 'Python'
    })
#cada uma das chaves a, b, c.. representa um coluna
#B = Timestamp em Python é um número que representa um momento específico no tempo.
#C = cria uma coluna com valores 1.0, indexada por uma lista de inteiros de 0 a 3 e com o tipo de dados float32.
#D = np.arraycom valores inteiros 3 usando a biblioteca NumPy e define o tipo de dados como int32. 3 * 4 repete o numero 3 quatro vezes
#E = cria uma coluna com dados categóricos contendo as categorias 'test' e 'train'.

print(df2)
print(df2.dtypes)
