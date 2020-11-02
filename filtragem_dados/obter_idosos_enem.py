import pandas as pd

# Informando a localização do arquivo com os microdados do ENEM 2019
arq_microdados = 'MICRODADOS_ENEM_2019.csv'

# Fazendo a leitura dos dados
dados = pd.read_csv(arq_microdados, sep=";", encoding="ISO-8859-1")


# Fazendo uma filtragem para pegar apenas os inscritos que são idosos
idosos_enem = dados.query('NU_IDADE >= 60')
# print(len(idosos_enem))

# Criando um arquivo .csv apenas com os dados dos idosos
destino = 'MICRODADOS_ENEM_2019_IDOSOS.csv'
idosos_enem.to_csv(destino, index=False)