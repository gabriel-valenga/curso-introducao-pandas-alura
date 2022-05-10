import os.path

import pandas

dados_imoveis_csv = pandas.read_csv('./static/aluguel.csv', sep=';')
dados_imoveis_excel = pandas.read_excel('./static/aluguel.xlsx')
dados_imoveis_json = pandas.read_json('./static/aluguel.json')
dados_imoveis_txt = pandas.read_table('./static/aluguel.txt')
dados_imoveis_html = pandas.read_html('https://www.federalreserve.gov/releases/h3/current/default.htm')

dados_imoveis = dados_imoveis_json
colunas_tipo_dados_imoveis = dados_imoveis.dtypes
tamanho_dataframe_dados_imoveis = dados_imoveis.shape[0]

tipos_de_imovel = dados_imoveis['Tipo']
tipos_de_imovel.drop_duplicates(inplace=True)  # inplace para executar o metodo direto na variavel, sem ter que criar uma nova para receber a execucao do metodo. exemplo nova_variavel = variavel()
tamanho_tipos_de_imovel = tipos_de_imovel.shape[0]
tipos_de_imovel.index = range(tamanho_tipos_de_imovel)  # para corrigir os indices ex: 0,1,2,3...

apenas_apartamentos = dados_imoveis['Tipo'] == 'Apartamento'
apenas_casas = (dados_imoveis['Tipo'] == 'Casa') \
               | (dados_imoveis['Tipo'] == 'Casa de Condomínio') \
               | (dados_imoveis['Tipo'] == 'Casa de Vila')
dados_imoveis_apartamentos = dados_imoveis[apenas_apartamentos]
dados_imoveis_casas = dados_imoveis[apenas_casas]

dados_imoveis_filtrar_colunas = dados_imoveis.iloc[[0, 1], [0, 1]]

# dados_imoveis.to_csv('dados_imoveis/dados_imoveis_exercicio_pandas.csv', sep=';', index=False)  # salvando o arquivo em csv

nomes = [['João', 'Maria', 'Ana'], ['Amanda', 'Carol', 'Viviane'], ['Letícia', 'Daniele', 'Carla']]

nomes_dataframe = pandas.DataFrame(nomes, list('321'), list('ZYX'))
nomes_dataframe.sort_index(inplace=True)
nomes_dataframe.sort_values(by='X', inplace=True)
nomes_dataframe.sort_values(by='3', axis=1, inplace=True)

alunos = pandas.DataFrame({'Nome': ['Ary', 'Cátia', 'Denis', 'Beto', 'Bruna', 'Dara', 'Carlos', 'Alice'],
                           'Sexo': ['M', 'F', 'M', 'M', 'F', 'F', 'M', 'F'],
                           'Idade': [15, 27, 56, 32, 42, 21, 19, 35],
                           'Notas': [7.5, 2.5, 5.0, 10, 8.2, 7, 6, 5.6],
                           'Aprovado': [True, False, False, True, True, True, False, False]},
                          columns=['Nome', 'Idade', 'Sexo', 'Notas', 'Aprovado'])

selecao_alunos_aprovados = alunos['Aprovado'] == True
selecao_alunas_aprovadas = (alunos['Aprovado'] == True) & (alunos['Sexo'] == 'F')
selecao_alunos_dez_a_vinte_ou_maior_40 = ((alunos['Idade'] >= 10)\
                                         & (alunos['Idade'] <= 20))\
                                         | (alunos['Idade'] > 40)
alunos_aprovados = alunos[selecao_alunos_aprovados]
alunas_aprovadas = alunos[selecao_alunas_aprovadas]
alunos_dez_a_vinte_ou_maior_quarenta = alunos[selecao_alunos_dez_a_vinte_ou_maior_40]

teste_loc = [['João', 'Maria', 'Ana'], ['Amanda', 'Carol', 'Viviane'], ['Letícia', 'Daniele', 'Carla']]

teste_loc_dataframe = pandas.DataFrame(nomes, list('321'), list('ZYX'))

find_teste_loc_dataframe = teste_loc_dataframe.loc[['2']]
find_teste_iloc_dataframe = teste_loc_dataframe.iloc[[1,2]]

apenas_alunos_reprovados = alunos['Aprovado'] == False
apenas_alunos_reprovados = alunos[apenas_alunos_reprovados]['Nome', 'Sexo', 'Idade']