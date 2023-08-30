import pandas as pd
import time, re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException

# Lendo o arquivo CSV com o pandas
df = pd.read_csv('/home/araujoroa2/Downloads/gerar_csv_94.csv', header=None)

# Verificando se o DataFrame foi criado corretamente
if not df.empty:
    print("O arquivo CSV foi lido com sucesso.")
    print("Número de linhas:", len(df))
    print("Colunas:", df.columns)
else:
    print("O arquivo CSV não pôde ser encontrado ou está vazio.")

try:
    # Inicializando o navegador Selenium
    path = '/static/driver/chromedriver'
    driver = webdriver.Chrome()  
    print("O driver do Selenium foi localizado com sucesso.")
    coluna_b = df.iloc[:, 1] 

    driver.get('http://www.comprasnet.gov.br/seguro/loginPortalUASG.asp')
    driver.current_window_handle  # id da janela atual
    driver.set_window_size(width=1022, height=683)

    ## Pagina de Login

    # Localize o campo desejado usando o seletor CSS
    campo = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#card2 .content')))

    # Localize o campo de login dentro do elemento com a classe .content e clique nele
    campo_login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'txtLogin')))
    campo_login.click()

    # Agora, preencha o campo de login com o valor desejado
    campo_login.send_keys('79260144515')

    # Localize o campo de senha dentro do elemento com a classe .content e clique nele
    campo_senha = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'txtSenha')))
    campo_senha.click()

    # Agora, preencha o campo de senha com o valor desejado
    campo_senha.send_keys('SATIC20232')

    # Aguarde até que o botão esteja clicável antes de clicar nele
    botao_entrar = WebDriverWait(campo, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.br-button.is-primary')))
    botao_entrar.click()
    
    ## Pagina Inicial
    botao_criar = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.div-menu-acesso-rapido-interno button.br-button.is-primary')))
    botao_criar.click()

    campo_etp = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'ETP')))
    campo_etp.click()

    time.sleep(5)

    # Obtenha todas as guias abertas pelo driver
    guias = driver.window_handles

    # Alterne para a nova aba (guia) que foi aberta
    driver.switch_to.window(guias[1])  # O índice 0 é a guia original, o índice 1 é a nova guia

    ## Pagina ETP
    botao_criar_etp = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.br-button.primary.ng-star-inserted')))
    botao_criar_etp.click()

    opcao_etp_tic = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'p-slidemenusub ul li.ui-menuitem:nth-child(1) a span')))
    opcao_etp_tic.click()

    ## Passando informações ETP - TIC

    ## Informações Básicas

    # Aguarde até que o botão "Próximo campo" esteja clicável antes de clicar nele
    botao_proximo = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@ptooltip, "Próximo campo")]')))
    botao_proximo.click()

    ##  Descrição da necessidade

    # Localize o iframe pelo seletor CSS ou por qualquer outro meio disponível
    iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe.cke_wysiwyg_frame')))

    # Alterne para o iframe
    driver.switch_to.frame(iframe)

    campo_necessidade_2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body.document-editor')))
    campo_necessidade_2.click()

    #Agora, preencha o campo de login com o valor desejado
    campo_necessidade_2.send_keys(coluna_b.iloc[1])

    # Após preencher o campo, retorne ao conteúdo principal
    driver.switch_to.default_content()

    # Aguarde até que o botão "Próximo campo" esteja clicável antes de clicar nele
    botao_proximo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[ptooltip="Próximo campo"]')))
    botao_proximo.click()

    ## Área requisitante

    # Aguarde até que o botão "Próximo campo" esteja clicável antes de clicar nele
    botao_proximo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[ptooltip="Próximo campo"]')))
    botao_proximo.click()

    ## Necessidades de Negócio

    # Localize o iframe pelo seletor CSS ou por qualquer outro meio disponível
    iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe.cke_wysiwyg_frame')))

    # Alterne para o iframe
    driver.switch_to.frame(iframe)

    campo_necessidade_4 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body.document-editor')))
    campo_necessidade_4.click()

    #Agora, preencha o campo de login com o valor desejado
    campo_necessidade_4.send_keys(coluna_b.iloc[3])

    # Após preencher o campo, retorne ao conteúdo principal
    driver.switch_to.default_content()

    # Aguarde até que o botão "Próximo campo" esteja clicável antes de clicar nele
    botao_proximo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[ptooltip="Próximo campo"]')))
    botao_proximo.click()

    ## Necessidades Tecnológicas

    # Localize o iframe pelo seletor CSS ou por qualquer outro meio disponível
    iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe.cke_wysiwyg_frame')))

    # Alterne para o iframe
    driver.switch_to.frame(iframe)

    campo_necessidade_5 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body.document-editor')))
    campo_necessidade_5.click()

    #Agora, preencha o campo de login com o valor desejado
    campo_necessidade_5.send_keys(coluna_b.iloc[4])

    # Após preencher o campo, retorne ao conteúdo principal
    driver.switch_to.default_content()

    # Aguarde até que o botão "Próximo campo" esteja clicável antes de clicar nele
    botao_proximo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[ptooltip="Próximo campo"]')))
    botao_proximo.click()

    ## Demais requisitos necessários e suficientes à escolha da solução de TIC

    # Localize o iframe pelo seletor CSS ou por qualquer outro meio disponível
    iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe.cke_wysiwyg_frame')))

    # Alterne para o iframe
    driver.switch_to.frame(iframe)

    campo_necessidade_6 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body.document-editor')))
    campo_necessidade_6.click()

    #Agora, preencha o campo de login com o valor desejado
    campo_necessidade_6.send_keys(coluna_b.iloc[5])

    # Após preencher o campo, retorne ao conteúdo principal
    driver.switch_to.default_content()

    # Aguarde até que o botão "Próximo campo" esteja clicável antes de clicar nele
    botao_proximo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[ptooltip="Próximo campo"]')))
    botao_proximo.click()

    ## Estimativa da demanda - quantidade de bens e serviços

    # Localize o iframe pelo seletor CSS ou por qualquer outro meio disponível
    iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe.cke_wysiwyg_frame')))

    # Alterne para o iframe
    driver.switch_to.frame(iframe)

    campo_necessidade_7 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body.document-editor')))
    campo_necessidade_7.click()

    #Agora, preencha o campo de login com o valor desejado
    campo_necessidade_7.send_keys(coluna_b.iloc[6])

    # Após preencher o campo, retorne ao conteúdo principal
    driver.switch_to.default_content()

    # Aguarde até que o botão "Próximo campo" esteja clicável antes de clicar nele
    botao_proximo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[ptooltip="Próximo campo"]')))
    botao_proximo.click()

    ## Demais Requisitos Necessários e Suficientes à Escolha da Solução de TIC

    # Localize o iframe pelo seletor CSS ou por qualquer outro meio disponível
    iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe.cke_wysiwyg_frame')))

    # Alterne para o iframe
    driver.switch_to.frame(iframe)

    campo_solucao_8 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body.document-editor')))
    campo_solucao_8.click()

    #Agora, preencha o campo de login com o valor desejado
    campo_solucao_8.send_keys(coluna_b.iloc[7])

    # Após preencher o campo, retorne ao conteúdo principal
    driver.switch_to.default_content()

    # Aguarde até que o botão "Próximo campo" esteja clicável antes de clicar nele
    botao_proximo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[ptooltip="Próximo campo"]')))
    botao_proximo.click()

    ## Análise comparativa de soluções

    # Localize o iframe pelo seletor CSS ou por qualquer outro meio disponível
    iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe.cke_wysiwyg_frame')))

    # Alterne para o iframe
    driver.switch_to.frame(iframe)

    campo_solucao_9 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body.document-editor')))
    campo_solucao_9.click()

    #Agora, preencha o campo de login com o valor desejado
    campo_solucao_9.send_keys(coluna_b.iloc[8])

    # Após preencher o campo, retorne ao conteúdo principal
    driver.switch_to.default_content()

    # Aguarde até que o botão "Próximo campo" esteja clicável antes de clicar nele
    botao_proximo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[ptooltip="Próximo campo"]')))
    botao_proximo.click()

    ## Registro de soluções consideradas inviáveis

    # Localize o iframe pelo seletor CSS ou por qualquer outro meio disponível
    iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe.cke_wysiwyg_frame')))

    # Alterne para o iframe
    driver.switch_to.frame(iframe)

    campo_solucao_10 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body.document-editor')))
    campo_solucao_10.click()

    #Agora, preencha o campo de login com o valor desejado
    campo_solucao_10.send_keys(coluna_b.iloc[9])

    # Após preencher o campo, retorne ao conteúdo principal
    driver.switch_to.default_content()

    # Aguarde até que o botão "Próximo campo" esteja clicável antes de clicar nele
    botao_proximo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[ptooltip="Próximo campo"]')))
    botao_proximo.click()

    ## Análise comparativa de custos (TCO)

    # Localize o iframe pelo seletor CSS ou por qualquer outro meio disponível
    iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe.cke_wysiwyg_frame')))

    # Alterne para o iframe
    driver.switch_to.frame(iframe)

    campo_solucao_11 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body.document-editor')))
    campo_solucao_11.click()

    #Agora, preencha o campo de login com o valor desejado
    campo_solucao_11.send_keys(coluna_b.iloc[10])

    # Após preencher o campo, retorne ao conteúdo principal
    driver.switch_to.default_content()

    # Aguarde até que o botão "Próximo campo" esteja clicável antes de clicar nele
    botao_proximo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[ptooltip="Próximo campo"]')))
    botao_proximo.click()

    ## Descrição da solução de TIC a ser contratada

    # Localize o iframe pelo seletor CSS ou por qualquer outro meio disponível
    iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe.cke_wysiwyg_frame')))

    # Alterne para o iframe
    driver.switch_to.frame(iframe)

    campo_solucao_12 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body.document-editor')))
    campo_solucao_12.click()

    #Agora, preencha o campo de login com o valor desejado
    campo_solucao_12.send_keys(coluna_b.iloc[11])

    # Após preencher o campo, retorne ao conteúdo principal
    driver.switch_to.default_content()

    # Aguarde até que o botão "Próximo campo" esteja clicável antes de clicar nele
    botao_proximo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[ptooltip="Próximo campo"]')))
    botao_proximo.click()

    ## Estimativa de custo total da contratação

    # Remove os pontos e troca a vírgula por ponto decimal
    valor_sem_mascara = float(re.sub(r'[^\d,]', '', coluna_b.iloc[13]).replace(',', '.'))

    # Convertendo para um número inteiro
    valor_inteiro = int(valor_sem_mascara)

    # Separando casas decimais
    valor_decimais = int ((valor_sem_mascara - valor_inteiro)* 100)

    # Localize novamente o campo de input
    campo_solucao_13_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[formcontrolname="valorNumerico"]')))

    #Agora, preencha o campo com o valor desejado
    campo_solucao_13_input.send_keys(valor_inteiro)

    # Obtém o valor atual do campo de input
    valor_com_mascara = campo_solucao_13_input.get_attribute("value")

    # Encontre a posição da vírgula no valor atual
    posicao_virgula = valor_com_mascara.find(',')

    # Posicione o cursor após a vírgula, movendo para a direita
    for _ in range(len(valor_com_mascara) - posicao_virgula + 1):
        campo_solucao_13_input.send_keys(Keys.RIGHT)
        time.sleep(1)
        campo_solucao_13_input.send_keys(valor_decimais)

    time.sleep(1)

    # Localize o iframe pelo seletor CSS ou por qualquer outro meio disponível
    iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe.cke_wysiwyg_frame')))

    # Alterne para o iframe
    driver.switch_to.frame(iframe)

    campo_solucao_13 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body.document-editor')))
    campo_solucao_13.click()

    #Agora, preencha o campo de login com o valor desejado
    campo_solucao_13.send_keys(coluna_b.iloc[12])

    # Após preencher o campo, retorne ao conteúdo principal
    driver.switch_to.default_content()

    # Role para cima
    driver.execute_script("window.scrollTo(0, 0);")

    # Aguarde até que o botão "Próximo campo" esteja clicável antes de clicar nele
    botao_proximo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[ptooltip="Próximo campo"]')))
    botao_proximo.click()

    ## Justificativa técnica da escolha da solução

    # Localize o iframe pelo seletor CSS ou por qualquer outro meio disponível
    iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe.cke_wysiwyg_frame')))

    # Alterne para o iframe
    driver.switch_to.frame(iframe)

    campo_solucao_14 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body.document-editor')))
    campo_solucao_14.click()

    #Agora, preencha o campo de login com o valor desejado
    campo_solucao_14.send_keys(coluna_b.iloc[13])

    # Após preencher o campo, retorne ao conteúdo principal
    driver.switch_to.default_content()

    # Aguarde até que o botão "Próximo campo" esteja clicável antes de clicar nele
    botao_proximo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[ptooltip="Próximo campo"]')))
    botao_proximo.click()

    ## Justificativa econômica da escolha da solução

    # Localize o iframe pelo seletor CSS ou por qualquer outro meio disponível
    iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe.cke_wysiwyg_frame')))

    # Alterne para o iframe
    driver.switch_to.frame(iframe)

    campo_solucao_15 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body.document-editor')))
    campo_solucao_15.click()

    #Agora, preencha o campo de login com o valor desejado
    campo_solucao_15.send_keys(coluna_b.iloc[14])

    # Após preencher o campo, retorne ao conteúdo principal
    driver.switch_to.default_content()

    # Aguarde até que o botão "Próximo campo" esteja clicável antes de clicar nele
    botao_proximo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[ptooltip="Próximo campo"]')))
    botao_proximo.click()

    ## Benefícios a serem alcançados com a contratação

    # Localize o iframe pelo seletor CSS ou por qualquer outro meio disponível
    iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe.cke_wysiwyg_frame')))

    # Alterne para o iframe
    driver.switch_to.frame(iframe)

    campo_planejamento_16 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body.document-editor')))
    campo_planejamento_16.click()

    #Agora, preencha o campo de login com o valor desejado
    campo_planejamento_16.send_keys(coluna_b.iloc[15])

    # Após preencher o campo, retorne ao conteúdo principal
    driver.switch_to.default_content()

    # Aguarde até que o botão "Próximo campo" esteja clicável antes de clicar nele
    botao_proximo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[ptooltip="Próximo campo"]')))
    botao_proximo.click()

    ## Providências a serem Adotadas

    # Localize o iframe pelo seletor CSS ou por qualquer outro meio disponível
    iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe.cke_wysiwyg_frame')))

    # Alterne para o iframe
    driver.switch_to.frame(iframe)

    campo_planejamento_17 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body.document-editor')))
    campo_planejamento_17.click()

    #Agora, preencha o campo de login com o valor desejado
    campo_planejamento_17.send_keys(coluna_b.iloc[16])

    # Após preencher o campo, retorne ao conteúdo principal
    driver.switch_to.default_content()

    # Aguarde até que o botão "Próximo campo" esteja clicável antes de clicar nele
    botao_proximo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[ptooltip="Próximo campo"]')))
    botao_proximo.click()

    ## Declaração de Viabilidade

    # Aguarde até que o botão "Próximo campo" esteja clicável antes de clicar nele
    botao_proximo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[ptooltip="Próximo campo"]')))
    botao_proximo.click()

    ## Responsáveis

    # Aguarde até que o botão "Próximo campo" esteja clicável antes de clicar nele
    botao_proximo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[ptooltip="Próximo campo"]')))
    botao_proximo.click()



    time.sleep(10)

except WebDriverException as e:
    print("Ocorreu um erro no WebDriver:", e)
    print("Entre em contato com o desenvolvedor para obter suporte.")
    driver.quit()

except Exception as e:
    print("Ocorreu um erro inesperado:", e)
    print("Entre em contato com o desenvolvedor para obter suporte.")
    driver.quit()



# Pausa a execução do script para aguardar sua interação manual com o alerta
input("Pressione Enter após interagir com o alerta para continuar.")

# Feche o navegador
driver.quit()
