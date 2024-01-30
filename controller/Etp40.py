from datetime import datetime
from model.Product import Product
from model.User import User
from model.Etp40 import Etp40
from flask import jsonify, session, request
from config import app_active, app_config
from flask_sqlalchemy import SQLAlchemy
from flask_login import current_user
from bs4 import BeautifulSoup

config = app_config[app_active]
db = SQLAlchemy(config.APP)

class Etp40Controller:
    def __init__(self):
        self.etp40_model = Etp40()
    
    def get_etp40(self, limit):    
        result = []
    
        try:
            etp40_objects = Etp40.query.limit(limit).all()

            for etp40 in etp40_objects:
                result.append({
                    'id': etp40.id,
                    'informacao1_40': etp40.informacao1_40,
                    'necessidade2_40': etp40.necessidade2_40,
                    'necessidade3_40': etp40.necessidade3_40,
                    'necessidade4_40': etp40.necessidade4_40,
                    'solucao5_40': etp40.solucao5_40,
                    'solucao6_40': etp40.solucao6_40,
                    'solucao7_40': etp40.solucao7_40,
                    'solucao8_40': etp40.solucao8_40,
                    'solucao9_40': etp40.solucao9_40,
                    'solucao10_40': etp40.solucao10_40,
                    'solucao11_40': etp40.solucao11_40,
                    'planejamento12_40': etp40.planejamento12_40,
                    'planejamento13_40': etp40.planejamento13_40,
                    'planejamento14_40': etp40.planejamento14_40,
                    'viabilidade15_40': etp40.viabilidade15_40,
                    'viabilidade16_40': etp40.viabilidade16_40,
                    'usuario_id': etp40.usuario_id,
                    'date_created': etp40.date_created.strftime("%Y-%m-%d %H:%M:%S")
                })
            status = 200
        except Exception as e:
            print(e)
            result = []
            status = 400
        finally:
            return jsonify({
                'result': result,
                'status': status
            })

    def get_etp40_by_id(self, id):
        try:
            etp40 = Etp40.query.get(id)
            print(etp40.__dict__)
            if etp40:
                result = {
                    'id': etp40.id,
                    'informacao1_40': etp40.informacao1_40,
                    'necessidade2_40': etp40.necessidade2_40,
                    'necessidade3_40': etp40.necessidade3_40,
                    'necessidade4_40': etp40.necessidade4_40,
                    'solucao5_40': etp40.solucao5_40,
                    'solucao6_40': etp40.solucao6_40,
                    'solucao7_40': etp40.solucao7_40,
                    'solucao8_40': etp40.solucao8_40,
                    'solucao9_40': etp40.solucao9_40,
                    'solucao10_40': etp40.solucao10_40,
                    'solucao11_40': etp40.solucao11_40,
                    'planejamento12_40': etp40.planejamento12_40,
                    'planejamento13_40': etp40.planejamento13_40,
                    'planejamento14_40': etp40.planejamento14_40,
                    'viabilidade15_40': etp40.viabilidade15_40,
                    'viabilidade16_40': etp40.viabilidade16_40,
                    'usuario_id': etp40.usuario_id,
                    'date_created': etp40.date_created.strftime("%Y-%m-%d %H:%M:%S")
                }
                status = 200
            else:
                result = {}
                status = 404
        except Exception as e:
            print(e)
            result = {}
            status = 400
        finally:
            return jsonify({
                'result': result,
                'status': status
            })
               
    def save_etp40():
        def remove_html_tags(text):
                soup = BeautifulSoup(text, 'html.parser')
                return soup.get_text()  
            
        result = []
        status = 400  # Define o status inicial como 400 (erro)

    
        status = 400  # Define o status inicial como 400 (erro)

        try:
            etp40_data = {}  # Dicionário para armazenar os dados da sessão

            for etapa in range(1, 17):
                conteudo_editor = session.get(str(etapa), '')
                
                if etapa == 8:
                    input_value = request.args.get('valor')
                    if input_value is not None:
                        conteudo_editor = input_value

                if conteudo_editor is not None:
                    if conteudo_editor.strip() == '' or conteudo_editor.strip() == '<br>':
                        conteudo_editor = ' '  # Define como vazio se o conteúdo for vazio ou contiver apenas <br>
                else:
                    conteudo_editor = ' '
                    
                conteudo_editor= remove_html_tags(conteudo_editor)
                

                etp40_data[str(etapa)] = conteudo_editor  # Armazena o conteúdo da sessão no dicionário
                
            etp40 = Etp40(
                informacao1_40=etp40_data.get('1', ''),
                necessidade2_40=etp40_data.get('2', ''),
                necessidade3_40=etp40_data.get('3', ''),
                necessidade4_40=etp40_data.get('4', ''),
                solucao5_40=etp40_data.get('5', ''),
                solucao6_40=etp40_data.get('6', ''),
                solucao7_40=etp40_data.get('7', ''),
                solucao8_40=etp40_data.get('8', ''),
                solucao9_40=etp40_data.get('9', ''),
                solucao10_40=etp40_data.get('10', ''),
                solucao11_40=etp40_data.get('11', ''),
                planejamento12_40=etp40_data.get('12', ''),
                planejamento13_40=etp40_data.get('13', ''),
                planejamento14_40=etp40_data.get('14', ''),
                viabilidade15_40=etp40_data.get('15', ''),
                viabilidade16_40=etp40_data.get('16', ''),
                usuario_id= current_user.id,  # Certifique-se de obter o valor correto da sessão
                
                date_created=datetime.now()  # Define a data de criação como o momento atual
            )

            res = etp40.save()  # Chama o método de salvamento no modelo
            
            if res:
                print(res)
                status = 200  # Define o status como 200 (sucesso)
                result = "Dados salvos com sucesso"
            else:
                print(etp40)
                status = 400  # Define o status como 200 (sucesso)
                result = "Não salvou"
                
            status = 200  # Define o status como 200 (sucesso)
            result = "Dados salvos com sucesso"
        except Exception as e:
            print(e)
            result = "Erro ao salvar os dados"

        return jsonify({
            'result': result,
            'status': status
        })

    def retomar_session_etp40(form_id):
        try:
            etp40 = Etp40.get_etp40_formulario_by_id(form_id)  # Recupera o registro da tabela Etp40 com base no ID do formulário
            
            if etp40 is not None:
                session['1'] = etp40.informacao1_40
                session['2'] = etp40.necessidade2_40
                session['3'] = etp40.necessidade3_40
                session['4'] = etp40.necessidade4_40
                session['5'] = etp40.solucao5_40
                session['6'] = etp40.solucao6_40
                session['7'] = etp40.solucao7_40
                session['8'] = etp40.solucao8_40
                session['9'] = etp40.solucao9_40
                session['10'] = etp40.solucao10_40
                session['11'] = etp40.solucao11_40
                session['12'] = etp40.planejamento12_40
                session['13'] = etp40.planejamento13_40
                session['14'] = etp40.planejamento14_40
                session['15'] = etp40.viabilidade15_40
                session['16'] = etp40.viabilidade16_40

                return True  # Retorna True para indicar que os dados foram recuperados com sucesso
            else:
                return False  # Retorna False se o registro não for encontrado

        except Exception as e:
            print(e)
            return False  # Retorna False em caso de erro

    def salvar_edicao_etp40(form_id):

        result = Etp40.salvar_edicao_etp40(form_id)
        return result

    def ultimo_id_formulario():
        
        res = Etp40.get_ultimo_id_formulario()

        return res
            
    def retoma_session_etp40(form_id):
        try:
            etp40 = Etp40.get_etp40_formulario_by_id(form_id)  # Recupera o registro da tabela Etp40 com base no ID do formulário
            
            if etp40 is not None:
                session['1'] = etp40.informacao1_40
                session['2'] = etp40.necessidade2_40
                session['3'] = etp40.necessidade3_40
                session['4'] = etp40.necessidade4_40
                session['5'] = etp40.solucao5_40
                session['6'] = etp40.solucao6_40
                session['7'] = etp40.solucao7_40
                session['8'] = etp40.solucao8_40
                session['9'] = etp40.solucao9_40
                session['10'] = etp40.solucao10_40
                session['11'] = etp40.solucao11_40
                session['12'] = etp40.planejamento12_40
                session['13'] = etp40.planejamento13_40
                session['14'] = etp40.planejamento14_40
                session['15'] = etp40.viabilidade15_40
                session['16'] = etp40.viabilidade16_40

                return session  # Retorna True para indicar que os dados foram recuperados com sucesso
            else:
                return 'False'  # Retorna False se o registro não for encontrado

        except Exception as e:
            print(e)
            return False  # Retorna False em caso de erro

    def deletar_etp40(form_id):
        try:
            res = Etp40.delete(form_id)
            return True
        except Exception as e:
            print(e)
            return False  # Retorna False em caso de erro    
