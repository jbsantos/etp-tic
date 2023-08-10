from decimal import Decimal
import pandas as pd
import re
from num2words import num2words


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

# Exemplo de string no formato "R$ 5.656,10"
valor_com_mascara = coluna_b.iloc[7]

# Removendo a máscara e trocando a vírgula por ponto
valor_sem_mascara = float(re.sub(r'[^\d,]', '', valor_com_mascara).replace(',', '.'))

# Convertendo para um número inteiro
valor_inteiro = int(valor_sem_mascara)

print("Valor com máscara:", valor_com_mascara)
print("Valor sem máscara:", valor_sem_mascara)
print("Valor inteiro:", valor_inteiro)

# Separando a parte inteira dos centavos
valor_centavos = valor_sem_mascara - float(valor_inteiro) 

print("Valor centavos:", f"{valor_centavos:02}")  # Exibe os centavos com dois dígitos, adicionando zero à esquerda se necessário

valor_arredondado = round(valor_centavos, 2)
print(valor_arredondado) 


def valor_por_extenso(valor):
    partes = valor.split(".")
    
    if len(partes) >= 2:
        reais = partes[0].replace(".", "")
        centavos = partes[1]
    else:
        reais = valor.replace(".", "")
        centavos = "00"
    
    extenso_reais = num2words(int(reais), lang='pt_BR').replace("-", " ")
    extenso_centavos = num2words(int(centavos), lang='pt_BR').replace("-", " ")
    
    if extenso_reais == "um":
        extenso_reais = "um real"
    else:
        extenso_reais += " reais"
    
    if extenso_centavos == "um":
        extenso_centavos = "um centavo"
    else:
        extenso_centavos += " centavos"
    
    valor_extenso = extenso_reais + " e " + extenso_centavos
    return valor_extenso.title()

valor = valor_sem_mascara
valor_extenso = valor_por_extenso(str(valor))
print(valor_extenso)

    

