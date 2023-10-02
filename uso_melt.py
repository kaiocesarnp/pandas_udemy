import pandas as pd

data = {
    "localização": ['CidadeA', 'CidadeB'],
    "Temperatura": ["Prevista", "Atual"],
    "Set-2019": [30, 32],
    "Out-2019": [45, 43],
    "Nov-2019": [24, 22]
    }
#print(data)

#Transformando o dicionário acima num Data Frame:
df = pd.DataFrame(data, columns = ['localização', 'Temperatura', 'Set-2019', 'Out-2019', 'Nov-2019'])
#print(df)

#Reshape utilizando Melt
df2 = pd.melt(df, id_vars = ["localização", "Temperatura"], var_name = "Data", value_name = "Valor")
print(df2)
#id_vars = id das variáveis são 'localização' e 'temperatura'
#var_name e value_name alteram os nomes das datas (set-2019, por ex) e adiciona o nome 'valor'


#Outra forma (não interessante):
df3 = pd.melt(df, id_vars = ["localização"], var_name = "Date", value_name = "Value")
print(df3)
