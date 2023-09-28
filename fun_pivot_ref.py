#Função Pivor
#Utilizada para manipular DF, tabelas, fazer reshaping nos dados

import pandas as pd
import numpy as np

dias = pd.date_range(start = '20190101', periods = 12)
#print(dias)


Pessoa = ['George', 'Victor', 'Lucas']
#print(np.random.choice(Pessoa)) #Nome é escolhido aleatoriamente

Nome = []
Gasto = []
for i in range(12):
    Nome.append(np.random.choice(Pessoa)) #append armazena o nome sorteado no Nome
    Gasto.append(np.round(np.random.rand()*100, 2)) #np.random.rand gera um numero aleatório entre 0 e 1 e multiplica por 100. Ou seja, o gasto será entre 0 e 100
#print(Nome)                                     #np.round(2) significa o tanto de casas decimais que o gasto terá
#print(Gasto)

df = pd.DataFrame({'Dia': dias, 'Nome': Nome, 'Gasto': Gasto})
#print(df)

#------------

#Agrupando todas as variáveis num único DF:
df = pd.DataFrame({'Dias': dias, 'Nome': Nome, 'Gasto': Gasto}) #dicionário
#print(df)


#-----------

#Visual mais agradável:
new_column = df.pivot(index = 'Dias', columns = 'Nome', values = 'Gasto')
print(new_column)
