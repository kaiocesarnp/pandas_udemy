import numpy as np
import matplotlib.pyplot as plt #para exibir gráficos
import pandas as pd

#print(plt.style.available)#estilos de gráficos disponíveis. Também podem ser encontrados no site matplotlib.org
#print(plt.style.use()) #para utilizar o estilo desejado


#Tamanho do retangulo/caixa da figura:
plt.rcParams['figure.figsize'] = (12, 7) # 20 é a parte X, 7 é Y

d = pd.read_csv('c:/users/inss/desktop/k/titanic_train.csv')
#print(d.head(4))
#print(d.shape)

#plt.plot(d.Age, '*-r') #gráfico com '*' nas pontas e r = red/vermelho
#plt.title('Infos dos passageiros do Titanic')
#plt.xlabel('Passageiro', size = 20)
#plt.ylabel('Idade', size = 25)
#plt.show()

#Utilizando a biblio pandas diretamente:
#d.Age.plot()
#plt.xlabel('Passageiro', size = 20)
#plt.ylabel('Idade', size = 25)
#plt.show()

#Scatter plot. Mostra como os dados estão espalhados no gráfico
#print(d.head(2))
#plt.scatter(d.PassengerId, d.Age, color = 'g', marker = '*') #eixo X é 'passe..' e o Y é 'Age'
#plt.show()

#Histogramas: distribuição de frequência dos dados
print(d.head(3))
print(d.Age.describe())
d.Age.hist()
plt.xlabel('Idade')
plt.ylabel('Freq observada')
plt.show()
