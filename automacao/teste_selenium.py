import time, re
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from num2words import num2words
from config import app_active, app_config
#Controller
from controller.Etp40 import Etp40Controller
from controller.Etp94 import Etp94Controller
from controller.User import UserController

config = app_config[app_active]

class ImportAuto:

    def import_automatic_etp(usuario, senha, id_form, etp):

        #Colocar validação de qual etp usar
        if(etp == 1):
            info_etp = Etp40Controller.retoma_session_etp40(id_form)
        
        elif(etp == 2):
            info_etp = Etp94Controller.retoma_session_etp94(id_form)
        
        ## Instaciar o Drive do Navegador
        def inicializar_drive():
            try:
                # Inicializa o serviço do ChromeDriver
                service = Service(ChromeDriverManager().install())  
                
                # path = 'chromedriver'

                # Define algumas opções
                options = webdriver.ChromeOptions()
                # options.add_argument("--start-maximized")  # Inicia o navegador maximizado
                options.add_argument("--headless=new")  # Inicia o navegador maximiza
                # driver = webdriver.Chrome()
                
                # Inicializa o driver do Chrome com as opções configuradas
                driver = webdriver.Chrome(service=service, options=options)


                # print("O driver do Selenium foi localizado com sucesso.")
                return driver
            except WebDriverException as e:
                error_code = '1000'
                error_message = 'Ocorreu um erro no WebDriver'
                driver.quit()
                
                print(f'Erro ({error_code}): {error_message}')
                return ('error', e)   
        
        ## Acesso ao site do compras net
        def conexao_comprasnet(driver):
            try:
                driver.get('http://www.comprasnet.gov.br/seguro/loginPortalUASG.asp')
                driver.current_window_handle  # id da janela atual
                driver.set_window_size(width=1022, height=683)
                # print ('Conexao Com Site Efetuada')
            except Exception as e:
                error_code = '1001'
                error_message = 'Ocorreu um erro no endereçamento do site'
                driver.quit()

                print(f'Erro ({error_code}): {error_message}')
                return ('error', e)   
        
        ## Procedimento de Logar
        def processo_conexao_login(driver, usuario, senha):
            try:
                # Localize o campo desejado usando o seletor CSS
                campo = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#card2 .content')))

                # Localize o campo de login dentro do elemento com a classe .content e clique nele
                campo_login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'txtLogin')))
                campo_login.click()

                # Agora, preencha o campo de login com o valor desejado
                campo_login.send_keys(usuario)

                # Localize o campo de senha dentro do elemento com a classe .content e clique nele
                campo_senha = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'txtSenha')))
                campo_senha.click()

                # Agora, preencha o campo de senha com o valor desejado
                campo_senha.send_keys(senha)

                # Aguarde até que o botão esteja clicável antes de clicar nele
                botao_entrar = WebDriverWait(campo, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.br-button.is-primary')))
                botao_entrar.click()

                # print('Informação Recebida')
                 
            except Exception as e:
                error_code = '1002'
                error_message = 'Erro de Repasse de Informação'
                driver.quit()

                print(f'Erro ({error_code}): {error_message}')
                return ('error', e)   

        ## Escolha de criacão do etp
        def escolhar_processo_criar_etp(driver):
            try:
                botao_criar = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.div-menu-acesso-rapido-interno button.br-button.is-primary')))
                botao_criar.click()

                criar_etp = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'ETP')))
                criar_etp.click()
                # print('Escolha de Etp Efetuada')
                 
            except Exception as e:
                error_code = '1003'
                error_message = 'Escolha de opção ETP não localizado'
                driver.quit()

                print(f'Erro ({error_code}): {error_message}')
                return ('error', e) # Retorna e para indicar erro

        ## Escolha na criacao do etp
        def escolhar_criar_etp_informado(driver,etp):
            try:
                botao_criar_etp = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.br-button.primary.ng-star-inserted')))
                botao_criar_etp.click()

                time.sleep(5)

                if (etp == 1):
                    opcao_etp_outros = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'p-slidemenusub ul li.ui-menuitem:nth-child(2) a span')))
                    opcao_etp_outros.click()
                    # print('Escolha ETP40')
                     
                elif(etp == 2):
                    opcao_etp_tic = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'p-slidemenusub ul li.ui-menuitem:nth-child(1) a span')))
                    opcao_etp_tic.click()
                    # print('Escolha ETP94')
                     
            except Exception as e:
                error_code = '1004'
                error_message = 'Escolha de opção ETP informada não localizado'
                # driver.quit()

                print(f'Erro ({error_code}): {error_message}')
                return ('error', e) # Retorna e para indicar erro
        
        ## Etapa de Informações Básicas
        def modulo_informacao_basicas(driver):

            time.sleep(5)
            try:
                # Aguarde até que o botão "Próximo campo" esteja clicável antes de clicar nele
                botao_proximo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@ptooltip, "Próximo campo")]')))
                botao_proximo.click()
                # print('mODULO INFORMAÇÃO OK')
            except Exception as e:
                error_code = '1004'
                error_message = 'Erro na Etapa 1 - Informações Básicas'

                # Buscar Numero do Documento Pós Erro do Processo - Rascunho 
                numero = buscar_numero_documento(driver)
                # driver.quit()

                print(f'Erro ({error_code}): {error_message}')
                # return ('error', e) # Retorna e para indicar erro

                return ('warning', numero) # Retorna e para indicar erro

        ## Etapa de Necessidade
        def modulo_necessidade(driver,etp):

            ##  Descrição da necessidade
            try:
                # Localize o iframe pelo seletor CSS ou por qualquer outro meio disponível
                iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe.cke_wysiwyg_frame')))

                # Alterne para o iframe
                driver.switch_to.frame(iframe)

                campo_necessidade_2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body.document-editor')))
                campo_necessidade_2.click()

                # Agora, preencha o campo de login com o valor desejado
                campo_necessidade_2.send_keys(info_etp['2'])

                # Após preencher o campo, retorne ao conteúdo principal
                driver.switch_to.default_content()

                # Aguarde até que o botão "Próximo campo" esteja clicável antes de clicar nele
                botao_proximo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[ptooltip="Próximo campo"]')))
                botao_proximo.click()
            except Exception as e:
                error_code = '1005'
                error_message = 'Erro na Etapa 2 - Descrição da necessidade'
                
                # Buscar Numero do Documento Pós Erro do Processo - Rascunho 
                numero = buscar_numero_documento(driver)

                # print('Rascunho N°-', numero)
                # driver.quit()

                print(f'Erro ({error_code}): {error_message}')
                # return ('error', e) # Retorna e para indicar erro
                return ('warning', numero) # Retorna e para indicar erro

            ## Área requisitante
            try:
                # Aguarde até que o botão "Próximo campo" esteja clicável antes de clicar nele
                botao_proximo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[ptooltip="Próximo campo"]')))
                botao_proximo.click()
            except Exception as e:
                error_code = '1006'
                error_message = 'Erro na Etapa 3 - Área requisitante'
                
                # Buscar Numero do Documento Pós Erro do Processo - Rascunho 
                numero = buscar_numero_documento(driver)
                # driver.quit()

                print(f'Erro ({error_code}): {error_message}')
                # return ('error', e) # Retorna e para indicar erro
                return ('warning', numero) # Retorna e para indicar erro

            # print('Modulo necessidade seguindo')
            time.sleep(5)

            if (etp == 1):
                ## Descrição dos Requisitos da Contratação
                try:
                    # Localize o iframe pelo seletor CSS ou por qualquer outro meio disponível
                    iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe.cke_wysiwyg_frame')))

                    # Alterne para o iframe
                    driver.switch_to.frame(iframe)

                    campo_etp40_necessidade_4 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body.document-editor')))
                    campo_etp40_necessidade_4.click()

                    #Agora, preencha o campo de login com o valor desejado
                    campo_etp40_necessidade_4.send_keys(info_etp['4'])

                    # Após preencher o campo, retorne ao conteúdo principal
                    driver.switch_to.default_content()

                    # Aguarde até que o botão "Próximo campo" esteja clicável antes de clicar nele
                    botao_proximo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[ptooltip="Próximo campo"]')))
                    botao_proximo.click()
                    # print('Escolha ETP40 - Necessidade Concluida')
                except Exception as e:
                    error_code = '1007'
                    error_message = 'Erro na Etapa 4 - Descrição dos Requisitos da Contratação'
                    
                    # Buscar Numero do Documento Pós Erro do Processo - Rascunho 
                    numero = buscar_numero_documento(driver)
                    # driver.quit()

                    print(f'Erro ({error_code}): {error_message}')
                    # return ('error', e) # Retorna e para indicar erro
                    return ('warning', numero) # Retorna e para indicar erro
            
            elif(etp == 2):
                ## Necessidades de Negócio
                try:
                    # Localize o iframe pelo seletor CSS ou por qualquer outro meio disponível
                    iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe.cke_wysiwyg_frame')))

                    # Alterne para o iframe
                    driver.switch_to.frame(iframe)

                    campo_etp94_necessidade_4 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body.document-editor')))
                    campo_etp94_necessidade_4.click()

                    #Agora, preencha o campo de login com o valor desejado
                    campo_etp94_necessidade_4.send_keys(info_etp['4'])

                    # Após preencher o campo, retorne ao conteúdo principal
                    driver.switch_to.default_content()

                    # Aguarde até que o botão "Próximo campo" esteja clicável antes de clicar nele
                    botao_proximo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[ptooltip="Próximo campo"]')))
                    botao_proximo.click()
                except Exception as e:
                    error_code = '1007'
                    error_message = 'Erro na Etapa 4 - Necessidades de Negócio'
                    
                    # Buscar Numero do Documento Pós Erro do Processo - Rascunho 
                    numero = buscar_numero_documento(driver)
                    # driver.quit()

                    print(f'Erro ({error_code}): {error_message}')
                    # return ('error', e) # Retorna e para indicar erro
                    return ('warning', numero) # Retorna e para indicar erro

                ## Necessidades Tecnológicas
                try:
                    # Localize o iframe pelo seletor CSS ou por qualquer outro meio disponível
                    iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe.cke_wysiwyg_frame')))

                    # Alterne para o iframe
                    driver.switch_to.frame(iframe)

                    campo_etp94_necessidade_5 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body.document-editor')))
                    campo_etp94_necessidade_5.click()

                    # Agora, preencha o campo de login com o valor desejado
                    campo_etp94_necessidade_5.send_keys(info_etp['5'])

                    # Após preencher o campo, retorne ao conteúdo principal
                    driver.switch_to.default_content()

                    # Aguarde até que o botão "Próximo campo" esteja clicável antes de clicar nele
                    botao_proximo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[ptooltip="Próximo campo"]')))
                    botao_proximo.click()
                except Exception as e:
                    error_code = '1008'
                    error_message = 'Erro na Etapa 5 - Necessidades Tecnológicas'
                    
                    # Buscar Numero do Documento Pós Erro do Processo - Rascunho 
                    numero = buscar_numero_documento(driver)
                    # driver.quit()

                    print(f'Erro ({error_code}): {error_message}')
                    # return ('error', e) # Retorna e para indicar erro
                    return ('warning', numero) # Retorna e para indicar erro

                ## Demais requisitos necessários e suficientes à escolha da solução de TIC
                try:
                    # Localize o iframe pelo seletor CSS ou por qualquer outro meio disponível
                    iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe.cke_wysiwyg_frame')))

                    # Alterne para o iframe
                    driver.switch_to.frame(iframe)

                    campo_etp94_necessidade_6 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body.document-editor')))
                    campo_etp94_necessidade_6.click()

                    # Agora, preencha o campo de login com o valor desejado
                    campo_etp94_necessidade_6.send_keys(info_etp['6'])

                    # Após preencher o campo, retorne ao conteúdo principal
                    driver.switch_to.default_content()

                    # Aguarde até que o botão "Próximo campo" esteja clicável antes de clicar nele
                    botao_proximo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[ptooltip="Próximo campo"]')))
                    botao_proximo.click()
                except Exception as e:
                    error_code = '1009'
                    error_message = 'Erro na Etapa 6 - Demais requisitos necessários e suficientes à escolha da solução de TIC'
                    
                    # Buscar Numero do Documento Pós Erro do Processo - Rascunho 
                    numero = buscar_numero_documento(driver)
                    # driver.quit()

                    print(f'Erro ({error_code}): {error_message}')
                    # return ('error', e) # Retorna e para indicar erro
                    return ('warning', numero) # Retorna e para indicar erro

                ## Estimativa da demanda - quantidade de bens e serviços
                try:
                    # Localize o iframe pelo seletor CSS ou por qualquer outro meio disponível
                    iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe.cke_wysiwyg_frame')))

                    # Alterne para o iframe
                    driver.switch_to.frame(iframe)

                    campo_etp94_necessidade_7 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body.document-editor')))
                    campo_etp94_necessidade_7.click()

                    # Agora, preencha o campo de login com o valor desejado
                    campo_etp94_necessidade_7.send_keys(info_etp['7'])

                    # Após preencher o campo, retorne ao conteúdo principal
                    driver.switch_to.default_content()

                    # Aguarde até que o botão "Próximo campo" esteja clicável antes de clicar nele
                    botao_proximo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[ptooltip="Próximo campo"]')))
                    botao_proximo.click()
                except Exception as e:
                    error_code = '1010'
                    error_message = 'Erro na Etapa 7 - Estimativa da demanda - quantidade de bens e serviços'
                    
                    # Buscar Numero do Documento Pós Erro do Processo - Rascunho 
                    numero = buscar_numero_documento(driver)
                    # driver.quit()

                    print(f'Erro ({error_code}): {error_message}')
                    # return ('error', e) # Retorna e para indicar erro
                    return ('warning', numero) # Retorna e para indicar erro
                # print('Escolha ETP94 - Necessidade Concluida')
            
        ## Transformar o Valor em Extenso
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

        ## Etapa de Solução
        def modulo_solucao(driver,etp):

            time.sleep(5)

            if (etp == 1):
                ## Levantamento de Mercado
                try:
                    # Localize o iframe pelo seletor CSS ou por qualquer outro meio disponível
                    iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe.cke_wysiwyg_frame')))

                    # Alterne para o iframe
                    driver.switch_to.frame(iframe)

                    campo_etp40_solucao_5 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body.document-editor')))
                    campo_etp40_solucao_5.click()

                    #Agora, preencha o campo de login com o valor desejado
                    campo_etp40_solucao_5.send_keys(info_etp['5'])

                    # Após preencher o campo, retorne ao conteúdo principal
                    driver.switch_to.default_content()

                    # Aguarde até que o botão "Próximo campo" esteja clicável antes de clicar nele
                    botao_proximo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[ptooltip="Próximo campo"]')))
                    botao_proximo.click()
                except Exception as e:
                    error_code = '1008'
                    error_message = 'Erro na Etapa 5 - Levantamento de Mercado'
                    
                    # Buscar Numero do Documento Pós Erro do Processo - Rascunho 
                    numero = buscar_numero_documento(driver)
                    # driver.quit()

                    print(f'Erro ({error_code}): {error_message}')
                    # return ('error', e) # Retorna e para indicar erro
                    return ('warning', numero) # Retorna e para indicar erro

                ## Descrição da solução como um todo
                try:
                    # Localize o iframe pelo seletor CSS ou por qualquer outro meio disponível
                    iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe.cke_wysiwyg_frame')))

                    # Alterne para o iframe
                    driver.switch_to.frame(iframe)

                    campo_etp40_solucao_6 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body.document-editor')))
                    campo_etp40_solucao_6.click()

                    #Agora, preencha o campo de login com o valor desejado
                    campo_etp40_solucao_6.send_keys(info_etp['6'])

                    # Após preencher o campo, retorne ao conteúdo principal
                    driver.switch_to.default_content()

                    # Aguarde até que o botão "Próximo campo" esteja clicável antes de clicar nele
                    botao_proximo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[ptooltip="Próximo campo"]')))
                    botao_proximo.click()
                except Exception as e:
                    error_code = '1009'
                    error_message = 'Erro na Etapa 6 - Descrição da solução como um todo'
                    
                    # Buscar Numero do Documento Pós Erro do Processo - Rascunho 
                    numero = buscar_numero_documento(driver)
                    # driver.quit()

                    print(f'Erro ({error_code}): {error_message}')
                    # return ('error', e) # Retorna e para indicar erro
                    return ('warning', numero) # Retorna e para indicar erro

                ## Estimativa das Quantidades a serem Contratadas
                try:
                    # Localize o iframe pelo seletor CSS ou por qualquer outro meio disponível
                    iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe.cke_wysiwyg_frame')))

                    # Alterne para o iframe
                    driver.switch_to.frame(iframe)

                    campo_etp40_solucao_7 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body.document-editor')))
                    campo_etp40_solucao_7.click()

                    #Agora, preencha o campo com o valor desejado
                    campo_etp40_solucao_7.send_keys(info_etp['7'])

                    # Após preencher o campo, retorne ao conteúdo principal
                    driver.switch_to.default_content()

                    # Aguarde até que o botão "Próximo campo" esteja clicável antes de clicar nele
                    botao_proximo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[ptooltip="Próximo campo"]')))
                    botao_proximo.click()
                except Exception as e:
                    error_code = '1010'
                    error_message = 'Erro na Etapa 7 - Estimativa das Quantidades a serem Contratadas'
                    
                    # Buscar Numero do Documento Pós Erro do Processo - Rascunho 
                    numero = buscar_numero_documento(driver)
                    # driver.quit()

                    print(f'Erro ({error_code}): {error_message}')
                    # return ('error', e) # Retorna e para indicar erro
                    return ('warning', numero) # Retorna e para indicar erro

                ## Estimativa do Valor da Contratação
                try:
                    #Formatação do Valor
                    # Remove os pontos e troca a vírgula por ponto decimal
                    valor_sem_mascara = float(re.sub(r'[^\d,]', '', info_etp['8']).replace(',', '.'))

                    # Convertendo para um número inteiro
                    valor_inteiro = int(valor_sem_mascara)

                    # Separando casas decimais
                    valor_decimais = int ((valor_sem_mascara - valor_inteiro)* 100)

                    # Localize novamente o campo de input
                    campo_etp40_solucao_8_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[formcontrolname="valorNumerico"]')))

                    #Agora, preencha o campo com o valor desejado
                    campo_etp40_solucao_8_input.send_keys(valor_inteiro)

                    # Obtém o valor atual do campo de input
                    valor_com_mascara = campo_etp40_solucao_8_input.get_attribute("value")

                    # Encontre a posição da vírgula no valor atual
                    posicao_virgula = valor_com_mascara.find(',')

                    # Posicione o cursor após a vírgula, movendo para a direita
                    for _ in range(len(valor_com_mascara) - posicao_virgula + 1):
                        campo_etp40_solucao_8_input.send_keys(Keys.RIGHT)
                        time.sleep(1)
                        campo_etp40_solucao_8_input.send_keys(valor_decimais)

                    time.sleep(1)

                    # Localize o iframe pelo seletor CSS ou por qualquer outro meio disponível
                    iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe.cke_wysiwyg_frame')))

                    # Alterne para o iframe
                    driver.switch_to.frame(iframe)
                    time.sleep(5)

                    campo_etp40_solucao_8 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body.document-editor')))
                    campo_etp40_solucao_8.click()

                    # Valor por Extenso
                    valor_extenso = valor_por_extenso(str(valor_sem_mascara))

                    #Agora, preencha o campo de login com o valor desejado
                    #campo_etp40_solucao_8.send_keys(info_etp['8'])
                    campo_etp40_solucao_8.send_keys(valor_extenso)

                    # Após preencher o campo, retorne ao conteúdo principal
                    driver.switch_to.default_content()

                    # Role para cima
                    driver.execute_script("window.scrollTo(0, 0);")

                    time.sleep(5)
                    # Aguarde até que o botão "Próximo campo" esteja clicável antes de clicar nele
                    botao_proximo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[ptooltip="Próximo campo"]')))
                    botao_proximo.click()
                except Exception as e:
                    error_code = '1011'
                    error_message = 'Erro na Etapa 8 - Estimativa do Valor da Contratação'
                    
                    # Buscar Numero do Documento Pós Erro do Processo - Rascunho 
                    numero = buscar_numero_documento(driver)
                    # driver.quit()

                    print(f'Erro ({error_code}): {error_message}')
                    # return ('error', e) # Retorna e para indicar erro
                    return ('warning', numero) # Retorna e para indicar erro

                ## Justificativa para o Parcelamento ou não da Solução
                try:
                    # Localize o iframe pelo seletor CSS ou por qualquer outro meio disponível
                    iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe.cke_wysiwyg_frame')))

                    # Alterne para o iframe
                    driver.switch_to.frame(iframe)

                    campo_etp40_solucao_9 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body.document-editor')))
                    campo_etp40_solucao_9.click()

                    #Agora, preencha o campo de login com o valor desejado
                    campo_etp40_solucao_9.send_keys(info_etp['9'])

                    # Após preencher o campo, retorne ao conteúdo principal
                    driver.switch_to.default_content()

                    # Aguarde até que o botão "Próximo campo" esteja clicável antes de clicar nele
                    botao_proximo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[ptooltip="Próximo campo"]')))
                    botao_proximo.click()
                except Exception as e:
                    error_code = '1012'
                    error_message = 'Erro na Etapa 9 - Justificativa para o Parcelamento ou não da Solução'
                    
                    # Buscar Numero do Documento Pós Erro do Processo - Rascunho 
                    numero = buscar_numero_documento(driver)
                    # driver.quit()

                    print(f'Erro ({error_code}): {error_message}')
                    # return ('error', e) # Retorna e para indicar erro
                    return ('warning', numero) # Retorna e para indicar erro

                ## Contratações Correlatas e/ou Interdependentes
                try:
                    # Localize o iframe pelo seletor CSS ou por qualquer outro meio disponível
                    iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe.cke_wysiwyg_frame')))

                    # Alterne para o iframe
                    driver.switch_to.frame(iframe)

                    campo_etp40_solucao_10 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body.document-editor')))
                    campo_etp40_solucao_10.click()

                    #Agora, preencha o campo de login com o valor desejado
                    campo_etp40_solucao_10.send_keys(info_etp['10'])

                    # Após preencher o campo, retorne ao conteúdo principal
                    driver.switch_to.default_content()

                    # Aguarde até que o botão "Próximo campo" esteja clicável antes de clicar nele
                    botao_proximo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[ptooltip="Próximo campo"]')))
                    botao_proximo.click()
                except Exception as e:
                    error_code = '1013'
                    error_message = 'Erro na Etapa 10 - Contratações Correlatas e/ou Interdependentes'
                    
                    # Buscar Numero do Documento Pós Erro do Processo - Rascunho 
                    numero = buscar_numero_documento(driver)
                    # driver.quit()

                    print(f'Erro ({error_code}): {error_message}')
                    # return ('error', e) # Retorna e para indicar erro
                    return ('warning', numero) # Retorna e para indicar erro

                ## Alinhamento entre a Contratação e o Planejamento
                try:
                    # Localize o iframe pelo seletor CSS ou por qualquer outro meio disponível
                    iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe.cke_wysiwyg_frame')))

                    # Alterne para o iframe
                    driver.switch_to.frame(iframe)

                    campo_etp40_solucao_11 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body.document-editor')))
                    campo_etp40_solucao_11.click()

                    #Agora, preencha o campo de login com o valor desejado
                    campo_etp40_solucao_11.send_keys(info_etp['11'])

                    # Após preencher o campo, retorne ao conteúdo principal
                    driver.switch_to.default_content()

                    # Aguarde até que o botão "Próximo campo" esteja clicável antes de clicar nele
                    botao_proximo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[ptooltip="Próximo campo"]')))
                    botao_proximo.click()
                except Exception as e:
                    error_code = '1014'
                    error_message = 'Erro na Etapa 11 - Alinhamento entre a Contratação e o Planejamento'
                    
                    # Buscar Numero do Documento Pós Erro do Processo - Rascunho 
                    numero = buscar_numero_documento(driver)
                    # driver.quit()

                    print(f'Erro ({error_code}): {error_message}')
                    # return ('error', e) # Retorna e para indicar erro
                    return ('warning', numero) # Retorna e para indicar erro
                
                # print('Escolha ETP40 - Solução Concluido')
            
            elif(etp == 2):
                ## Demais Requisitos Necessários e Suficientes à Escolha da Solução de TIC
                try:
                    # Localize o iframe pelo seletor CSS ou por qualquer outro meio disponível
                    iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe.cke_wysiwyg_frame')))

                    # Alterne para o iframe
                    driver.switch_to.frame(iframe)

                    campo_etp94_solucao_8 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body.document-editor')))
                    campo_etp94_solucao_8.click()

                    # Agora, preencha o campo de login com o valor desejado
                    campo_etp94_solucao_8.send_keys(info_etp['8'])

                    # Após preencher o campo, retorne ao conteúdo principal
                    driver.switch_to.default_content()

                    # Aguarde até que o botão "Próximo campo" esteja clicável antes de clicar nele
                    botao_proximo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[ptooltip="Próximo campo"]')))
                    botao_proximo.click()
                except Exception as e:
                    error_code = '1011'
                    error_message = 'Erro na Etapa 8 - Demais Requisitos Necessários e Suficientes à Escolha da Solução de TIC'
                    
                    # Buscar Numero do Documento Pós Erro do Processo - Rascunho 
                    numero = buscar_numero_documento(driver)
                    # driver.quit()

                    print(f'Erro ({error_code}): {error_message}')
                    # return ('error', e) # Retorna e para indicar erro
                    return ('warning', numero) # Retorna e para indicar erro

                ## Análise comparativa de soluções
                try:
                    # Localize o iframe pelo seletor CSS ou por qualquer outro meio disponível
                    iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe.cke_wysiwyg_frame')))

                    # Alterne para o iframe
                    driver.switch_to.frame(iframe)

                    campo_etp94_solucao_9 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body.document-editor')))
                    campo_etp94_solucao_9.click()

                    # Agora, preencha o campo de login com o valor desejado
                    campo_etp94_solucao_9.send_keys(info_etp['9'])

                    # Após preencher o campo, retorne ao conteúdo principal
                    driver.switch_to.default_content()

                    # Aguarde até que o botão "Próximo campo" esteja clicável antes de clicar nele
                    botao_proximo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[ptooltip="Próximo campo"]')))
                    botao_proximo.click()
                except Exception as e:
                    error_code = '1012'
                    error_message = 'Erro na Etapa 9 - Análise comparativa de soluções'
                    
                    # Buscar Numero do Documento Pós Erro do Processo - Rascunho 
                    numero = buscar_numero_documento(driver)
                    # driver.quit()

                    print(f'Erro ({error_code}): {error_message}')
                    # return ('error', e) # Retorna e para indicar erro
                    return ('warning', numero) # Retorna e para indicar erro

                ## Registro de soluções consideradas inviáveis
                try:
                    # Localize o iframe pelo seletor CSS ou por qualquer outro meio disponível
                    iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe.cke_wysiwyg_frame')))

                    # Alterne para o iframe
                    driver.switch_to.frame(iframe)

                    campo_etp94_solucao_10 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body.document-editor')))
                    campo_etp94_solucao_10.click()

                    # Agora, preencha o campo de login com o valor desejado
                    campo_etp94_solucao_10.send_keys(info_etp['10'])

                    # Após preencher o campo, retorne ao conteúdo principal
                    driver.switch_to.default_content()

                    # Aguarde até que o botão "Próximo campo" esteja clicável antes de clicar nele
                    botao_proximo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[ptooltip="Próximo campo"]')))
                    botao_proximo.click()
                except Exception as e:
                    error_code = '1013'
                    error_message = 'Erro na Etapa 10 - Registro de soluções consideradas inviáveis'
                    
                    # Buscar Numero do Documento Pós Erro do Processo - Rascunho 
                    numero = buscar_numero_documento(driver)
                    # driver.quit()

                    print(f'Erro ({error_code}): {error_message}')
                    # return ('error', e) # Retorna e para indicar erro
                    return ('warning', numero) # Retorna e para indicar erro

                ## Análise comparativa de custos (TCO)
                try:
                    # Localize o iframe pelo seletor CSS ou por qualquer outro meio disponível
                    iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe.cke_wysiwyg_frame')))

                    # Alterne para o iframe
                    driver.switch_to.frame(iframe)

                    campo_etp94_solucao_11 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body.document-editor')))
                    campo_etp94_solucao_11.click()

                    # Agora, preencha o campo de login com o valor desejado
                    campo_etp94_solucao_11.send_keys(info_etp['11'])

                    # Após preencher o campo, retorne ao conteúdo principal
                    driver.switch_to.default_content()

                    # Aguarde até que o botão "Próximo campo" esteja clicável antes de clicar nele
                    botao_proximo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[ptooltip="Próximo campo"]')))
                    botao_proximo.click()
                except Exception as e:
                    error_code = '1014'
                    error_message = 'Erro na Etapa 11 - Análise comparativa de custos (TCO)'
                    # driver.quit()

                    print(f'Erro ({error_code}): {error_message}')
                    return ('error', e) # Retorna e para indicar erro

                ## Descrição da solução de TIC a ser contratada
                try:
                    # Localize o iframe pelo seletor CSS ou por qualquer outro meio disponível
                    iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe.cke_wysiwyg_frame')))

                    # Alterne para o iframe
                    driver.switch_to.frame(iframe)

                    campo_etp94_solucao_12 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body.document-editor')))
                    campo_etp94_solucao_12.click()

                    # Agora, preencha o campo de login com o valor desejado
                    campo_etp94_solucao_12.send_keys(info_etp['12'])

                    # Após preencher o campo, retorne ao conteúdo principal
                    driver.switch_to.default_content()

                    # Aguarde até que o botão "Próximo campo" esteja clicável antes de clicar nele
                    botao_proximo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[ptooltip="Próximo campo"]')))
                    botao_proximo.click()
                except Exception as e:
                    error_code = '1015'
                    error_message = 'Erro na Etapa 12 - Descrição da solução de TIC a ser contratada'
                    
                    # Buscar Numero do Documento Pós Erro do Processo - Rascunho 
                    numero = buscar_numero_documento(driver)
                    # driver.quit()

                    print(f'Erro ({error_code}): {error_message}')
                    # return ('error', e) # Retorna e para indicar erro
                    return ('warning', numero) # Retorna e para indicar erro

                ## Estimativa de custo total da contratação
                try:
                    # Remove os pontos e troca a vírgula por ponto decimal
                    valor_sem_mascara = float(re.sub(r'[^\d,]', '', info_etp['13']).replace(',', '.'))

                    # Convertendo para um número inteiro
                    valor_inteiro = int(valor_sem_mascara)

                    # Separando casas decimais
                    valor_decimais = int ((valor_sem_mascara - valor_inteiro)* 100)

                    # Localize novamente o campo de input
                    campo_etp94_solucao_13_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[formcontrolname="valorNumerico"]')))

                    # Agora, preencha o campo com o valor desejado
                    campo_etp94_solucao_13_input.send_keys(valor_inteiro)

                    # Obtém o valor atual do campo de input
                    valor_com_mascara = campo_etp94_solucao_13_input.get_attribute("value")

                    # Encontre a posição da vírgula no valor atual
                    posicao_virgula = valor_com_mascara.find(',')

                    # Posicione o cursor após a vírgula, movendo para a direita
                    for _ in range(len(valor_com_mascara) - posicao_virgula + 1):
                        campo_etp94_solucao_13_input.send_keys(Keys.RIGHT)
                        time.sleep(1)
                        campo_etp94_solucao_13_input.send_keys(valor_decimais)

                    time.sleep(1)

                    # Localize o iframe pelo seletor CSS ou por qualquer outro meio disponível
                    iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe.cke_wysiwyg_frame')))

                    # Alterne para o iframe
                    driver.switch_to.frame(iframe)

                    campo_etp94_solucao_13 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body.document-editor')))
                    campo_etp94_solucao_13.click()

                    # Valor por Extenso
                    valor_extenso = valor_por_extenso(str(valor_sem_mascara))

                    # Agora, preencha o campo de login com o valor desejado
                    #campo_etp94_solucao_13.send_keys(info_etp['13'])
                    campo_etp94_solucao_13.send_keys(valor_extenso)

                    # Após preencher o campo, retorne ao conteúdo principal
                    driver.switch_to.default_content()

                    # Role para cima
                    driver.execute_script("window.scrollTo(0, 0);")

                    # Aguarde até que o botão "Próximo campo" esteja clicável antes de clicar nele
                    botao_proximo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[ptooltip="Próximo campo"]')))
                    botao_proximo.click()
                except Exception as e:
                    error_code = '1016'
                    error_message = 'Erro na Etapa 13 - Estimativa de custo total da contratação'
                    
                    # Buscar Numero do Documento Pós Erro do Processo - Rascunho 
                    numero = buscar_numero_documento(driver)
                    # driver.quit()

                    print(f'Erro ({error_code}): {error_message}')
                    # return ('error', e) # Retorna e para indicar erro
                    return ('warning', numero) # Retorna e para indicar erro

                ## Justificativa técnica da escolha da solução
                try:
                    # Localize o iframe pelo seletor CSS ou por qualquer outro meio disponível
                    iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe.cke_wysiwyg_frame')))

                    # Alterne para o iframe
                    driver.switch_to.frame(iframe)

                    campo_etp94_solucao_14 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body.document-editor')))
                    campo_etp94_solucao_14.click()

                    # Agora, preencha o campo de login com o valor desejado
                    campo_etp94_solucao_14.send_keys(info_etp['14'])

                    # Após preencher o campo, retorne ao conteúdo principal
                    driver.switch_to.default_content()

                    # Aguarde até que o botão "Próximo campo" esteja clicável antes de clicar nele
                    botao_proximo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[ptooltip="Próximo campo"]')))
                    botao_proximo.click()
                except Exception as e:
                    error_code = '1017'
                    error_message = 'Erro na Etapa 14 - Justificativa técnica da escolha da solução'
                    
                    # Buscar Numero do Documento Pós Erro do Processo - Rascunho 
                    numero = buscar_numero_documento(driver)
                    # driver.quit()

                    print(f'Erro ({error_code}): {error_message}')
                    # return ('error', e) # Retorna e para indicar erro
                    return ('warning', numero) # Retorna e para indicar erro

                ## Justificativa econômica da escolha da solução
                try:
                    # Localize o iframe pelo seletor CSS ou por qualquer outro meio disponível
                    iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe.cke_wysiwyg_frame')))

                    # Alterne para o iframe
                    driver.switch_to.frame(iframe)

                    campo_etp94_solucao_15 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body.document-editor')))
                    campo_etp94_solucao_15.click()

                    # Agora, preencha o campo de login com o valor desejado
                    campo_etp94_solucao_15.send_keys(info_etp['15'])

                    # Após preencher o campo, retorne ao conteúdo principal
                    driver.switch_to.default_content()

                    # Aguarde até que o botão "Próximo campo" esteja clicável antes de clicar nele
                    botao_proximo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[ptooltip="Próximo campo"]')))
                    botao_proximo.click()
                except Exception as e:
                    error_code = '1018'
                    error_message = 'Erro na Etapa 15 - Justificativa econômica da escolha da solução'
                    
                    # Buscar Numero do Documento Pós Erro do Processo - Rascunho 
                    numero = buscar_numero_documento(driver)
                    # driver.quit()

                    print(f'Erro ({error_code}): {error_message}')
                    # return ('error', e) # Retorna e para indicar erro
                    return ('warning', numero) # Retorna e para indicar erro

                # print('Escolha ETP94 - Solução Concluido')

        ## Etapa de Planejamento
        def modulo_planejamento(driver,etp):

            time.sleep(5)

            if (etp == 1):
                ## Benefícios a serem alcançados com a contratação
                try:
                    # Localize o iframe pelo seletor CSS ou por qualquer outro meio disponível
                    iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe.cke_wysiwyg_frame')))

                    # Alterne para o iframe
                    driver.switch_to.frame(iframe)

                    campo_etp40_planejamento_12 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body.document-editor')))
                    campo_etp40_planejamento_12.click()

                    # Agora, preencha o campo de login com o valor desejado
                    campo_etp40_planejamento_12.send_keys(info_etp['12'])

                    # Após preencher o campo, retorne ao conteúdo principal
                    driver.switch_to.default_content()

                    # Aguarde até que o botão "Próximo campo" esteja clicável antes de clicar nele
                    botao_proximo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[ptooltip="Próximo campo"]')))
                    botao_proximo.click()
                except Exception as e:
                    error_code = '1015'
                    error_message = 'Erro na Etapa 12 - Benefícios a serem alcançados com a contratação'
                    
                    # Buscar Numero do Documento Pós Erro do Processo - Rascunho 
                    numero = buscar_numero_documento(driver)
                    # driver.quit()

                    print(f'Erro ({error_code}): {error_message}')
                    # return ('error', e) # Retorna e para indicar erro
                    return ('warning', numero) # Retorna e para indicar erro

                ## Providências a serem Adotadas
                try:
                    # Localize o iframe pelo seletor CSS ou por qualquer outro meio disponível
                    iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe.cke_wysiwyg_frame')))

                    # Alterne para o iframe
                    driver.switch_to.frame(iframe)

                    campo_etp40_planejamento_13 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body.document-editor')))
                    campo_etp40_planejamento_13.click()

                    #Agora, preencha o campo de login com o valor desejado
                    campo_etp40_planejamento_13.send_keys(info_etp['13'])

                    # Após preencher o campo, retorne ao conteúdo principal
                    driver.switch_to.default_content()

                    # Aguarde até que o botão "Próximo campo" esteja clicável antes de clicar nele
                    botao_proximo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[ptooltip="Próximo campo"]')))
                    botao_proximo.click()
                except Exception as e:
                    error_code = '1016'
                    error_message = 'Erro na Etapa 13 - Providências a serem Adotadas'
                    
                    # Buscar Numero do Documento Pós Erro do Processo - Rascunho 
                    numero = buscar_numero_documento(driver)
                    # driver.quit()

                    print(f'Erro ({error_code}): {error_message}')
                    # return ('error', e) # Retorna e para indicar erro
                    return ('warning', numero) # Retorna e para indicar erro

                ## Possíveis Impactos Ambientais
                try:
                    # Localize o iframe pelo seletor CSS ou por qualquer outro meio disponível
                    iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe.cke_wysiwyg_frame')))

                    # Alterne para o iframe
                    driver.switch_to.frame(iframe)

                    campo_etp40_planejamento_14 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body.document-editor')))
                    campo_etp40_planejamento_14.click()

                    #Agora, preencha o campo de login com o valor desejado
                    campo_etp40_planejamento_14.send_keys(info_etp['14'])

                    # Após preencher o campo, retorne ao conteúdo principal
                    driver.switch_to.default_content()

                    # Aguarde até que o botão "Próximo campo" esteja clicável antes de clicar nele
                    botao_proximo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[ptooltip="Próximo campo"]')))
                    botao_proximo.click()
                except Exception as e:
                    error_code = '1017'
                    error_message = 'Erro na Etapa 14 - Possíveis Impactos Ambientais'
                    
                    # Buscar Numero do Documento Pós Erro do Processo - Rascunho 
                    numero = buscar_numero_documento(driver)
                    # driver.quit()

                    print(f'Erro ({error_code}): {error_message}')
                    # return ('error', e) # Retorna e para indicar erro
                    return ('warning', numero) # Retorna e para indicar erro
                # print('Escolha ETP40 - Planejamento concluida')
            
            elif(etp == 2):
                ## Benefícios a serem alcançados com a contratação
                try:
                    # Localize o iframe pelo seletor CSS ou por qualquer outro meio disponível
                    iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe.cke_wysiwyg_frame')))

                    # Alterne para o iframe
                    driver.switch_to.frame(iframe)

                    campo_etp94_planejamento_16 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body.document-editor')))
                    campo_etp94_planejamento_16.click()

                    #Agora, preencha o campo de login com o valor desejado
                    campo_etp94_planejamento_16.send_keys(info_etp['16'])

                    # Após preencher o campo, retorne ao conteúdo principal
                    driver.switch_to.default_content()

                    # Aguarde até que o botão "Próximo campo" esteja clicável antes de clicar nele
                    botao_proximo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[ptooltip="Próximo campo"]')))
                    botao_proximo.click()
                except Exception as e:
                    error_code = '1019'
                    error_message = 'Erro na Etapa 16 - Benefícios a serem alcançados com a contratação'
                    
                    # Buscar Numero do Documento Pós Erro do Processo - Rascunho 
                    numero = buscar_numero_documento(driver)
                    # driver.quit()

                    print(f'Erro ({error_code}): {error_message}')
                    # return ('error', e) # Retorna e para indicar erro
                    return ('warning', numero) # Retorna e para indicar erro

                ## Providências a serem Adotadas
                try:
                    # Localize o iframe pelo seletor CSS ou por qualquer outro meio disponível
                    iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe.cke_wysiwyg_frame')))

                    # Alterne para o iframe
                    driver.switch_to.frame(iframe)

                    campo_etp94_planejamento_17 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body.document-editor')))
                    campo_etp94_planejamento_17.click()

                    #Agora, preencha o campo de login com o valor desejado
                    campo_etp94_planejamento_17.send_keys(info_etp['17'])

                    # Após preencher o campo, retorne ao conteúdo principal
                    driver.switch_to.default_content()

                    # Aguarde até que o botão "Próximo campo" esteja clicável antes de clicar nele
                    botao_proximo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[ptooltip="Próximo campo"]')))
                    botao_proximo.click()
                except Exception as e:
                    error_code = '1020'
                    error_message = 'Erro na Etapa 17 - Providências a serem Adotadas'
                    
                    # Buscar Numero do Documento Pós Erro do Processo - Rascunho 
                    numero = buscar_numero_documento(driver)
                    # driver.quit()

                    print(f'Erro ({error_code}): {error_message}')
                    # return ('error', e) # Retorna e para indicar erro
                    return ('warning', numero) # Retorna e para indicar erro
                # print('Escolha ETP94 - Planejamento concluida')
            
        ## Etapa Viabilidade
        def modulo_viabilidade(driver,etp):

            time.sleep(5)

            if(etp == 1):
                ## Declaração de Viabilidade
                try:
                    # Aguarde até que o botão "Próximo campo" esteja clicável antes de clicar nele
                    botao_proximo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[ptooltip="Próximo campo"]')))
                    botao_proximo.click()
                except Exception as e:
                    error_code = '1018'
                    error_message = 'Erro na Etapa 15 - Declaração de Viabilidade'
                    
                    # Buscar Numero do Documento Pós Erro do Processo - Rascunho 
                    numero = buscar_numero_documento(driver)
                    # driver.quit()

                    print(f'Erro ({error_code}): {error_message}')
                    # return ('error', e) # Retorna e para indicar erro
                    return ('warning', numero) # Retorna e para indicar erro

                ## Responsáveis
                try:
                    # Aguarde até que o botão "Próximo campo" esteja clicável antes de clicar nele
                    botao_proximo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[ptooltip="Próximo campo"]')))
                    botao_proximo.click()

                    # # Numero do Documento - Rascunho
                    # numero = buscar_numero_documento(driver)

                    # print('Rascunho N°-', numero)

                    # time.sleep(2)

                    # print('aqui*******************')

                    # return ('success', numero)
                except Exception as e:
                    error_code = '1019'
                    error_message = 'Erro na Etapa 16 - Responsáveis'
                    
                    # Buscar Numero do Documento Pós Erro do Processo - Rascunho 
                    numero = buscar_numero_documento(driver)
                    # driver.quit()

                    print(f'Erro ({error_code}): {error_message}')
                    # return ('error', e) # Retorna e para indicar erro
                    return ('warning', numero) # Retorna e para indicar erro
                # print('Escolha ETP40 - Viabilidade concluida')
            
            elif(etp == 2):

                ## Declaração de Viabilidade
                try:
                    # Aguarde até que o botão "Próximo campo" esteja clicável antes de clicar nele
                    botao_proximo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[ptooltip="Próximo campo"]')))
                    botao_proximo.click()   
                except Exception as e:
                    error_code = '1021'
                    error_message = 'Erro na Etapa 18 - Declaração de Viabilidade'
                    
                    # Buscar Numero do Documento Pós Erro do Processo - Rascunho 
                    numero = buscar_numero_documento(driver)
                    # driver.quit()

                    print(f'Erro ({error_code}): {error_message}')
                    # return ('error', e) # Retorna e para indicar erro
                    return ('warning', numero) # Retorna e para indicar erro

                ## Responsáveis
                try:
                    # Aguarde até que o botão "Próximo campo" esteja clicável antes de clicar nele
                    botao_proximo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[ptooltip="Próximo campo"]')))
                    botao_proximo.click()

                    # # Numero do Documento - Rascunho
                    # numero = buscar_numero_documento(driver)

                    # print('Rascunho N°-', numero)

                    # time.sleep(2)

                    # print('aqui*******************')

                    # return ('success', numero)
                except Exception as e:
                    error_code = '1022'
                    error_message = 'Erro na Etapa 19 - Responsáveis'
                    
                    # Buscar Numero do Documento Pós Erro do Processo - Rascunho 
                    numero = buscar_numero_documento(driver)
                    # driver.quit()

                    print(f'Erro ({error_code}): {error_message}')
                    # return ('error', e) # Retorna e para indicar erro
                    return ('warning', numero) # Retorna e para indicar erro

                # print('Escolha ETP94 - Viabilidade concluida')
            
        ## Buscar Numero de Rascunho
        def buscar_numero_documento(driver):

            # Role para cima
            driver.execute_script("window.scrollTo(0, 0);")
            
            # Localizar o elemento
            element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="form-etp"]/div/div/div[2]/app-campos/div[1]/div[1]/div[1]/div/ul/li[3]/span')))

            # Obter o texto do elemento
            texto_elemento = element.text

            # Extrair o valor desejado usando manipulações de string
            numero = texto_elemento.split("Nº ")[1]

            # Botao Voltar
            botao_voltar(driver)

            return numero
        
        ## Botão Voltar
        def botao_voltar(driver):
            # try:
                botao_voltar = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, 'span:nth-child(4) > .is-secondary'))
                )
                # Clique no botão "Voltar"
                botao_voltar.click()
            # except Exception as e:
            #     error_code = '1024'
            #     error_message = 'Botao Voltar não localizado'
            #     driver.quit()
                
            #     print(f'Erro ({error_code}): {error_message}')
            #     return ('error', e) # Retorna e para indicar erro

        ## Sequencia de ETP
        try:
            # Inicializando driver navegador 
            driver = inicializar_drive()

            # Conectar com a página
            conexao_comprasnet(driver)

            # Pagina de Login
            # Procedimento de Logar no ComprasNet
            processo_conexao_login(driver, usuario, senha)

            # Pagina Inicial ComprasNet
            escolhar_processo_criar_etp(driver)
            time.sleep(5)

            # Organizar Abas Abertas
            # Obtenha todas as guias abertas pelo driver
            guias = driver.window_handles

            # Alterne para a nova aba (guia) que foi aberta
            driver.switch_to.window(guias[1])  # O índice 0 é a guia original, o índice 1 é a nova guia

            # Pagina ETP - ComprasNet
            # Criacao do ETP
            escolhar_criar_etp_informado(driver, etp)

            # Etapa Informações Básicas
            modulo_informacao_basicas(driver)

            print('aqui------------------------------')

            #  Etapa de Necessidade
            modulo_necessidade(driver, etp)

            # Etapa de Solução
            modulo_solucao(driver, etp)

            # Etapa de Planejamento
            modulo_planejamento(driver, etp)

            # Etapa de Viabilidade
            modulo_viabilidade(driver, etp)

            # Numero do Documento - Rascunho
            numero = buscar_numero_documento(driver)

            print('Rascunho N°-', numero)

            time.sleep(2)

            # print('aqui*******************')

            return ('success', numero)
        
        except Exception as e:
            print("Ocorreu um erro inesperado:", e)
            print("Entre em contato com o desenvolvedor para obter suporte.")

            print('aqui*******************')
            return e

        finally:
            # Pausa a execução do script para aguardar sua interação manual com o alerta
            # input("Pressione Enter após interagir com o alerta para continuar.")

            # Feche o navegador
            driver.quit()
