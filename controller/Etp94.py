from datetime import datetime
from model.Product import Product
from model.User import User
from model.Etp94 import Etp94
from flask import jsonify, session, request
from config import app_active, app_config
from flask_sqlalchemy import SQLAlchemy
from flask_login import current_user
from bs4 import BeautifulSoup

config = app_config[app_active]
db = SQLAlchemy(config.APP)

class Etp94Controller:
    def __init__(self):
        self.etp94_model = Etp94()
    
    
    def get_etp94(self, limit):    
        result = []
    
        try:
            etp94_objects = Etp94.query.limit(limit).all()

            for etp94 in etp94_objects:
                result.append({
                    'id': etp94.id,
                    'informacao1_94': etp94.informacao1_94,
                    'necessidade2_94': etp94.necessidade2_94,
                    'necessidade3_94': etp94.necessidade3_94,
                    'necessidade4_94': etp94.necessidade4_94,
                    'necessidade5_94': etp94.necessidade5_94,
                    'necessidade6_94': etp94.necessidade6_94,
                    'necessidade7_94': etp94.necessidade7_94,
                    'solucao8_94': etp94.solucao8_94,
                    'solucao9_94': etp94.solucao9_94,
                    'solucao10_94': etp94.solucao10_94,
                    'solucao11_94': etp94.solucao11_94,
                    'solucao12_94': etp94.solucao12_94,
                    'solucao13_94': etp94.solucao13_94,
                    'solucao14_94': etp94.solucao14_94,
                    'solucao15_94': etp94.solucao15_94,
                    'planejamento16_94': etp94.planejamento16_94,
                    'planejamento17_94': etp94.planejamento17_94,
                    'viabilidade18_94': etp94.viabilidade18_94,
                    'viabilidade19_94': etp94.viabilidade19_94,
                    'usuario_id': etp94.usuario_id,
                    'date_created': etp94.date_created.strftime("%Y-%m-%d %H:%M:%S")
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

    def get_etp94_by_id(self, id):
        try:
            etp94 = Etp94.query.get(id)
            print(etp94.__dict__)
            if etp94:
                result = {
                    'id': etp94.id,
                    'informacao1_94': etp94.informacao1_94,
                    'necessidade2_94': etp94.necessidade2_94,
                    'necessidade3_94': etp94.necessidade3_94,
                    'necessidade4_94': etp94.necessidade4_94,
                    'necessidade5_94': etp94.necessidade5_94,
                    'necessidade6_94': etp94.necessidade6_94,
                    'necessidade7_94': etp94.necessidade7_94,
                    'solucao8_94': etp94.solucao8_94,
                    'solucao9_94': etp94.solucao9_94,
                    'solucao10_94': etp94.solucao10_94,
                    'solucao11_94': etp94.solucao11_94,
                    'solucao12_94': etp94.solucao12_94,
                    'solucao13_94': etp94.solucao13_94,
                    'solucao14_94': etp94.solucao14_94,
                    'solucao15_94': etp94.solucao15_94,
                    'planejamento16_94': etp94.planejamento16_94,
                    'planejamento17_94': etp94.planejamento17_94,
                    'viabilidade18_94': etp94.viabilidade18_94,
                    'viabilidade19_94': etp94.viabilidade19_94,
                    'usuario_id': etp94.usuario_id,
                    'date_created': etp94.date_created.strftime("%Y-%m-%d %H:%M:%S")
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
               
    def save_etp94():
        def remove_html_tags(text):
                soup = BeautifulSoup(text, 'html.parser')
                return soup.get_text()  
            
        result = []
        status = 400  # Define o status inicial como 400 (erro)

    
        status = 400  # Define o status inicial como 400 (erro)

        try:
            etp94_data = {}  # Dicionário para armazenar os dados da sessão

            for etapa in range(1, 20):
                conteudo_editor = session.get(str(etapa), '')
                
                if etapa == 13:
                    input_value = request.args.get('valor')
                    if input_value is not None:
                        conteudo_editor = input_value

                if conteudo_editor is not None:
                    if conteudo_editor.strip() == '' or conteudo_editor.strip() == '<br>':
                        conteudo_editor = ' '  # Define como vazio se o conteúdo for vazio ou contiver apenas <br>
                else:
                    conteudo_editor = ' '
                    
                conteudo_editor= remove_html_tags(conteudo_editor)
                

                etp94_data[str(etapa)] = conteudo_editor  # Armazena o conteúdo da sessão no dicionário
                
            etp94 = Etp94(
                informacao1_94=etp94_data.get('1', ''),
                necessidade2_94=etp94_data.get('2', ''),
                necessidade3_94=etp94_data.get('3', ''),
                necessidade4_94=etp94_data.get('4', ''),
                necessidade5_94=etp94_data.get('5', ''),
                necessidade6_94=etp94_data.get('6', ''),
                necessidade7_94=etp94_data.get('7', ''),
                solucao8_94=etp94_data.get('8', ''),
                solucao9_94=etp94_data.get('9', ''),
                solucao10_94=etp94_data.get('10', ''),
                solucao11_94=etp94_data.get('11', ''),
                solucao12_94=etp94_data.get('12', ''),
                solucao13_94=etp94_data.get('13', ''),
                solucao14_94=etp94_data.get('14', ''),
                solucao15_94=etp94_data.get('15', ''),
                planejamento16_94=etp94_data.get('16', ''),
                planejamento17_94=etp94_data.get('17', ''),
                viabilidade18_94=etp94_data.get('18', ''),
                viabilidade19_94=etp94_data.get('19', ''),
                usuario_id= current_user.id,  # Certifique-se de obter o valor correto da sessão
                
                date_created=datetime.now()  # Define a data de criação como o momento atual
            )

            res = etp94.save()  # Chama o método de salvamento no modelo
            
            if res:
                print(res)
                status = 200  # Define o status como 200 (sucesso)
                result = "Dados salvos com sucesso"
            else:
                print(etp94)
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

    def retomar_session_etp94(form_id):
        try:
            etp94 = Etp94.get_etp94_formulario_by_id(form_id)  # Recupera o registro da tabela Etp94 com base no ID do formulário
            
            if etp94 is not None:
                session['1'] = etp94.informacao1_94
                session['2'] = etp94.necessidade2_94
                session['3'] = etp94.necessidade3_94
                session['4'] = etp94.necessidade4_94
                session['5'] = etp94.necessidade5_94
                session['6'] = etp94.necessidade6_94
                session['7'] = etp94.necessidade7_94
                session['8'] = etp94.solucao8_94
                session['9'] = etp94.solucao9_94
                session['10'] = etp94.solucao10_94
                session['11'] = etp94.solucao11_94
                session['12'] = etp94.solucao12_94
                session['13'] = etp94.solucao13_94
                session['14'] = etp94.solucao14_94
                session['15'] = etp94.solucao15_94
                session['16'] = etp94.planejamento16_94
                session['17'] = etp94.planejamento17_94
                session['18'] = etp94.viabilidade18_94
                session['19'] = etp94.viabilidade19_94

                return True  # Retorna True para indicar que os dados foram recuperados com sucesso
            else:
                return False  # Retorna False se o registro não for encontrado

        except Exception as e:
            print(e)
            return False  # Retorna False em caso de erro

    def salvar_edicao_etp94(form_id):

        result = Etp94.salvar_edicao_etp94(form_id)
        return result

    def ultimo_id_formulario():
        
        res = Etp94.get_ultimo_id_formulario()

        return res
            
    def retoma_session_etp94(form_id):
        try:
            etp94 = Etp94.get_etp94_formulario_by_id(form_id)  # Recupera o registro da tabela Etp94 com base no ID do formulário
            
            if etp94 is not None:
                session['1'] = etp94.informacao1_94
                session['2'] = etp94.necessidade2_94
                session['3'] = etp94.necessidade3_94
                session['4'] = etp94.necessidade4_94
                session['5'] = etp94.necessidade5_94
                session['6'] = etp94.necessidade6_94
                session['7'] = etp94.necessidade7_94
                session['8'] = etp94.solucao8_94
                session['9'] = etp94.solucao9_94
                session['10'] = etp94.solucao10_94
                session['11'] = etp94.solucao11_94
                session['12'] = etp94.solucao12_94
                session['13'] = etp94.solucao13_94
                session['14'] = etp94.solucao14_94
                session['15'] = etp94.solucao15_94
                session['16'] = etp94.planejamento16_94
                session['17'] = etp94.planejamento17_94
                session['18'] = etp94.viabilidade18_94
                session['19'] = etp94.viabilidade19_94

                return session  # Retorna True para indicar que os dados foram recuperados com sucesso
            else:
                return False  # Retorna False se o registro não for encontrado

        except Exception as e:
            print(e)
            return False  # Retorna False em caso de erro

    def deletar_etp94(form_id):
        try:
            res = Etp94.delete(form_id)
            return True
        except Exception as e:
            print(e)
            return False  # Retorna False em caso de erro

