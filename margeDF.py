#Método/Função Merge

import pandas as pd

#Cadastro da loja A
cadastro_a = {'Id': ['AA2930', 'BB4563', 'CC2139', 'DE2521', 'GT3462', 'HH1158'],
              'Nome': ['Victor', 'Amanda', 'Bruna', 'Carlos', 'Ricardo', 'Maria'],
              'Idade': [20, 35, 40, 54, 30, 27],
              'CEP': ['00092-029', '11111-111', '22222-888', '00000-999', '88888-111', '77777-666']
    }
cadastro_a = pd.DataFrame(cadastro_a, columns = ['Id', 'Nome', 'Idade', 'CEP'])
#print(cadastro_a)

#Cadastro da loja B
cadastro_b = {'Id': ['CC9999', 'EF4488', 'DD9999', 'GT3462', 'HH1158'],
              'Nome': ['Marcos', 'Patricia', 'Ericka', 'Ricardos', 'Maria'],
              'Idade': [19, 30, 22, 30, 27],
              'CEP': ['00092-029', '11111-111', '11111-888', '88888-111', '77777-666']
    }
cadastro_b = pd.DataFrame(cadastro_b, columns = ['Id', 'Nome', 'Idade', 'CEP'])
#print(cadastro_b)

#Registro de compras de todas as unidades
compras = {'Id':['AA2930', 'EF4488', 'CC2139', 'EF4488', 'CC9999', 'AA2930', 'HH1158', 'HH1158'],
           'Data': ['2019-01-01', '2019-01-30', '2019-01-30', '2019-02-01', '2019-02-20', '2019-03-15', '2019-04-01', '2019-04-10'],
           'Valor': [200, 100, 40, 150, 300, 25, 50, 500]
           }
compras = pd.DataFrame(compras, columns = ['Id', 'Data', 'Valor'])
#print(compras)

#-------------

#Tipos de merge feitos em pandas:
#Inner Join = interseção de ambos os lados
#Full Join = Junta os lados completamente
#Left Join = Apenas as informações do lado esquerdo
#Right Join = Apenas as informações do lado direito


##Inner Join:
#Identicando clientes da loja A que também vão na loja B (Interseção de clientes):
#print(pd.merge(cadastro_a, cadastro_b, on = ["Id"], how = "inner"))

#O 'Id (on = ["Id"])' no caso é a coluna de rastreio, baseada no 'how'
#O how indica como será feito o merge, no caso com o 'inner' (interseção dos clientes de ambas as lojas)
#O 'x' e 'y' (sufixos) que aparecem ao lado de nome, idade, cep referem-se às tabelas da esquerda e direita, respectivamente
    #é possivel muda-los utilizando o comando suffixes = ('_A', '_B') por exemplo

#Coletando infos especificas do B :
#print(pd.merge(cadastro_a, cadastro_b [['Id', 'CEP']], on = ["Id"], how = "inner", suffixes = ('_A', '_B') ))

#-------------

#Full Join:
unicos = pd.concat([cadastro_a, cadastro_b], ignore_index = True)

#Removendo duplicatas:
#print(unicos.drop_duplicates(subset = "Id")) #subset é subconjunto, nesse caso baseado no 'id' de cada cliente

#-------------

#Left Join
#Identificando clientes que fizeram compras e estão cadastrados na loja A:

esquerda = pd.merge(cadastro_a, compras, how = "left", on = ["Id"])
#print(esquerda)

#Os que aparecem NaN no resultado é porque não fizeram compras

#Filtrando por pessoa os gastos que tiveram:
#print(esquerda.groupby(['Id', "Nome"])['Valor'].sum()) #sum = soma

#-------------

#Outer
#outer junta todos os dados atribuindo a um unico DF
print(pd.merge(cadastro_a, cadastro_b, how = "outer", on = ["Id"], indicator = True))

#Indicator mostra em qual tabela está cada cliente
