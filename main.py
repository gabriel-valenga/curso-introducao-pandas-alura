import pandas

dados_csv = pandas.read_csv('./static/aluguel.csv', sep=';')
dados_excel = pandas.read_excel('./static/aluguel.xlsx')
dados_json = pandas.read_json('./static/aluguel.json')
dados_txt = pandas.read_table('./static/aluguel.txt')
dados_html = pandas.read_html('https://www.federalreserve.gov/releases/h3/current/default.htm')

dados = dados_csv
colunas_tipo_dados = dados.dtypes
tamanho_dataframe_dados = dados.shape[0]

tipos_de_imovel = dados['Tipo']
tipos_de_imovel.drop_duplicates(inplace=True)  # inplace para executar o metodo direto na variavel, sem ter que criar uma nova para receber a execucao do metodo. exemplo nova_variavel = variavel()
tamanho_tipos_de_imovel = tipos_de_imovel.shape[0]
tipos_de_imovel.index = range(tamanho_tipos_de_imovel)  # para corrigir os indices ex: 0,1,2,3...
