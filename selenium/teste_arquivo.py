import pandas as pd
import re

# Lendo o arquivo CSV com o pandas
#df = pd.read_csv('/home/araujoroa2/Downloads/gerar_csv_94.csv')
df = pd.read_csv('/home/araujoroa2/Downloads/gerar_csv.csv', header=None)


# Verificando se o DataFrame foi criado corretamente
if not df.empty:
    print("O arquivo CSV foi lido com sucesso.")
    print("Número de linhas:", len(df))
    print("Colunas:", df.columns)
else:
    print("O arquivo CSV não pôde ser encontrado ou está vazio.")


# Inicializando o navegador Selenium
#coluna_b = df['Coluna B']
# Acessar a segunda coluna (índice 1) diretamente sem usar o nome da coluna
coluna_b = df.iloc[:, 1]

for valor in coluna_b:
    print(valor)

# Acessar o valor da posição 6 da coluna B
valor_posicao_6 = coluna_b.iloc[7]
print("Valor na posição 6 da coluna B:", valor_posicao_6)

# Exemplo de string no formato "R$ 5.656,00"
valor_com_mascara = coluna_b.iloc[7]

# Removendo a máscara e trocando a vírgula por ponto
valor_sem_mascara = re.sub(r'[^\d,]', '', valor_com_mascara).replace(',', '.')

print("Valor com máscara:", valor_com_mascara)
print("Valor sem máscara:", valor_sem_mascara)