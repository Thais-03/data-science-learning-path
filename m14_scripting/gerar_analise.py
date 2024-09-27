# Importar biblioteca padrão
import os
import sys

# Importar bibliotecas de terceiros
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()

# Declarar função pra a plotagem dos gráficos
def plota_grafico(df, value, index, func, ylabel, xlabel, opcao='nada'):
    if opcao == 'nada':
        pd.pivot_table(df, values=value, index=index,
                       aggfunc=func).plot(figsize=[15, 5])
    elif opcao == 'sort':
        pd.pivot_table(df, values=value, index=index,
                       aggfunc=func).sort_values(value).plot(figsize=[15, 5])
    elif opcao == 'unstack':
        pd.pivot_table(df, values=value, index=index,
                       aggfunc=func).unstack().plot(figsize=[15, 5])
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)

# Capturar os argumentos passados em uma lista
meses = sys.argv[1:]

# Abrir lista para armazenar arquivos
sinasc_2019 = []

# Iterar a lista de meses para gerar arquivos
for mes in meses: 
    arquivo = './Support_Exercise_M14/input/SINASC_RO_2019_'+mes+'.csv'
    sinasc_2019.append(arquivo)


# Iterar sobre cada arquivo CSV
for sinasc_mes in sinasc_2019:
    sinasc = pd.read_csv(sinasc_mes)
    print(sinasc.DTNASC.min(), sinasc.DTNASC.max())

    # Extrair o ano e mês mais recente da coluna DTNASC
    max_data = sinasc.DTNASC.max()[:7]
    print(max_data)
    
    # Criar diretório de saída para salvar as figuras
    output_dir = f'./Support_Exercise_M14/output/figs/{max_data}'
    os.makedirs(output_dir, exist_ok=True)

    # Gerar e salvar as figuras
    plota_grafico(sinasc, 'IDADEMAE', 'DTNASC', 'count', 'quantidade de nascimento', 'data de nascimento')
    plt.savefig(f'{output_dir}/quantidade_de_nascimento.png')

    plota_grafico(sinasc, 'IDADEMAE', ['DTNASC', 'SEXO'], 'mean', 'media idade mae', 'data de nascimento', 'unstack')
    plt.savefig(f'{output_dir}/media_idade_mae_por_sexo.png')

    plota_grafico(sinasc, 'PESO', ['DTNASC', 'SEXO'], 'mean', 'media peso bebe', 'data de nascimento', 'unstack')
    plt.savefig(f'{output_dir}/media_peso_bebe_por_sexo.png')

    plota_grafico(sinasc, 'PESO', 'ESCMAE', 'median', 'peso medio', 'escolaridade mae', 'sort')
    plt.savefig(f'{output_dir}/media_peso_por_escolaridade_mae.png')

    plota_grafico(sinasc, 'APGAR1', 'GESTACAO', 'mean', 'apgar1 medio', 'gestacao', 'sort')
    plt.savefig(f'{output_dir}/media_apgar1_por_gestacao.png')

    plota_grafico(sinasc, 'APGAR5', 'GESTACAO', 'mean', 'apgar5 medio', 'gestacao', 'sort')
    plt.savefig(f'{output_dir}/media_apgar5_por_gestacao.png')

    # Fechar as figuras
    plt.close('all')