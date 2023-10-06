#Salvando dados do csv para xlsx

import pandas as pd

d1 = pd.read_csv('c:/users/inss/desktop/k/iris/iris.data')


#Transformando csv em xlsx
print(d1.to_excel('c:/users/inss/desktop/k/teste.xlsx', index = False))

#'index = False' evita que o índice seja salvo como uma coluna adicional no Excel


#Foi necessário instalar a biblioteca 'openpyxl' que é um biblio utilizada
    #pelo pandas para escrever arquivos excel
