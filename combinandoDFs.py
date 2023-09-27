import pandas as pd

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                    index = [0, 1, 2, 3]) #especifica a posição de cada linha (A0, A1, A2..)

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                    index = [4, 5, 6, 7])

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']},
                    index = [8, 9, 10, 11])

#print(df1)
#print(df2)
#print(df3)

#Combinando DFs
#frames = [df1, df2, df3]
#framesCombinados = pd.concat(frames)
#print(framesCombinados)

#Outra forma:
#framesCombinados2 = pd.concat([df1, df2, df3])
#print(framesCombinados2)

#Forma errada e usada por iniciantes:
#framesCombinados = pd.concat(df1, df2, df3)

#------------------

#Adicionando chave de especificação para determinado df
#grupo = pd.concat([df1, df2, df3], keys = ['f1', 'f2', 'f3']) #cada um dos df agora possui um subgrupo
#print(grupo)

#Coletar valores de cada key
#print(grupo.loc['f2'])

#------------------

#Outra maneira de concatenar
g2 = df1._append(df2)._append(df3)
print(g2)




















