# -*- coding: utf-8 -*-
from flask import Flask, request,url_for, redirect, render_template, Response, json, abort, session, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, login_user, logout_user
from functools import wraps
from bs4 import BeautifulSoup

# config import
from config import app_config, app_active

# controllers
from controller.User import UserController
from controller.Product import ProductController
from admin.Admin import start_views
from flask_bootstrap import Bootstrap
import os
config = app_config[app_active]

def create_app(config_name):
    config = app_config[config_name]
    app = Flask(__name__, template_folder='templates')
    app.url_map.strict_slashes = False
    login_manager = LoginManager()
    login_manager.init_app(app)
    
    app.secret_key = config.SECRET
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
   #app.config["SQLALCHEMY_ECHO"] = True
  #  app.config["SQLALCHEMY_RECORD_QUERIES"] = True
    app.config['FLASK_ADMIN_SWATCH'] = 'paper'
    app.config['BABEL_DEFAULT_LOCALE'] = 'pt_BR'
    app.config['BABEL_DEFAULT_TIMEZONE'] = 'America/Sao_Paulo'
    
    db = SQLAlchemy(config.APP)
    db.init_app(app)
    migrate = Migrate(app, db)
    start_views(app,db)

    Bootstrap(app)

    #db.create_all()

    @app.after_request
    def after_request(response):
        #response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        return response

    def auth_token_required(f):
        @wraps(f)
        def verify_token(*args, **kwargs):
            user = UserController()
            try:
                result = user.verify_auth_token(request.headers['access_token'])
                if result['status'] == 200:
                    return f(*args, **kwargs)
                else:
                    abort(result['status'], result['message'])
            except KeyError as e:
                abort(401, 'Você precisa enviar um token de acesso')

        return verify_token

    @app.route('/')
    def index():
        return render_template('/etp/index.html')
    
    @app.route('/etp94')
    def etp94():
        return render_template('/etp94/etp94.html')
    
    @app.route('/etp40')
    def etp40():
    #     # Abrir o arquivo HTML e ler o seu conteúdo
    #     with open('templates/etp/aside.html', 'r') as file:
    #         html = file.read()
    #     soup = BeautifulSoup(html, 'html.parser')

    # # Encontrar todos os elementos <a> e obter o valor do atributo href
    #     href_values = [a['href'] for a in soup.find_all('a')]

    #     print(str(href_values))
    #     return render_template('resultado.html', href_values=href_values)
        return render_template('/etp/etp40.html')
    
    @app.route('/informacao',methods=['GET'])
    def componet():

        return render_template('etp/info_basico_etp40.html')
    
    @app.route('/descricao',methods=['GET'])
    def descricao():
        
        return render_template('etp/descricao.html')
    
    @app.route('/area-requisitante',methods=['GET'])
    def area_requisitante():

        return render_template('etp/area-requisitante.html')
    
    @app.route('/requisito',methods=['GET'])
    def requisito():

        return render_template('etp/requisito.html')

    @app.route('/mercado',methods=['GET'])
    def mercado():
        return render_template('etp/mercado.html')
    
    @app.route('/solucao',methods=['GET'])
    def solucao():
        return render_template('etp/solucao.html')
    
    @app.route('/estimativa-quantidade',methods=['GET'])
    def estimativa_quantidade():
        return render_template('etp/estimativa-quantidade.html')
       
    @app.route('/estimativa-valor',methods=['GET'])
    def estimativa_valor():
        return render_template('etp/estimativa-valor.html')
    
    @app.route('/justificativa',methods=['GET'])
    def justificativa():
        return render_template('etp/justificativa.html')
    
    @app.route('/contratacoes',methods=['GET'])
    def contratacoes():
        return render_template('etp/contratacoes.html')    
    
    @app.route('/alinhamento',methods=['GET'])
    def alinhamento():
        return render_template('etp/alinhamento.html')  
    
    @app.route('/beneficios',methods=['GET'])
    def beneficios():
        return render_template('etp/beneficios.html') 
    
    @app.route('/providencias',methods=['GET'])
    def providencias():
        return render_template('etp/providencias.html') 
    
    @app.route('/impactos',methods=['GET'])
    def impactos():
        return render_template('etp/impactos.html') 
    
    @app.route('/declaracao',methods=['GET'])
    def declaracao():
        return render_template('etp/declaracao.html') 

    @app.route('/responsavel',methods=['GET'])
    def responsavel():
        return render_template('etp/responsavel.html') 
    
    @app.route('/rota1', methods=['POST', 'GET'])
    
    def rota1():
        if request.method == 'POST':
            conteudo = request.form.get('conteudo')
            session['conteudo'] = conteudo
     
            return redirect('/rota1')

    # Verificar se a informação está armazenada na sessão
        conteudo = session.get('conteudo')
        
        return render_template('rota1.html', conteudo=conteudo)
        #return render_template('rota1.html')

    @app.route('/rota2', methods=['POST', 'GET'])
    def rota2():
         if request.method == 'POST':
            conteudo = request.form.get('conteudo')
            session['conteudo'] = conteudo
            #print(conteudo2)
            return redirect('/rota2')

    # Verificar se a informação está armazenada na sessão
         conteudo = session.get('conteudo')

         return render_template('rota2.html', conteudo=conteudo)
     
     
     
    @app.route('/rota3', methods=['POST', 'GET'])
    def rota3():
        if request.method == 'POST':
            conteudo2 = request.form.get('conteudo2')
            session['conteudo2'] = conteudo2
            print(conteudo2)
            return redirect('/rota3')

        # Verificar se a informação está armazenada na sessão
        conteudo2 = session.get('conteudo2')

        return render_template('rota3.html', conteudo2=conteudo2)
            #return render_template('rota1.html')
            
            #return render_template('rota2.html')
        #return render_template('rota2.html')

    @app.route('/ultima', methods=['POST'])
    def ultima():
        print(session)
        conteudo = session.get('conteudo')
        print(conteudo)
        sessoes = ['conteudo', 'conteudo2']
        for sessao in sessoes:
            session.pop(sessao, None)
        return render_template('ultima.html')

    
    @app.route('/login/')
    def login():
        return render_template('login.html', data={'status': 200, 'msg': None, 'type': None})

    @app.route('/login/', methods=['POST'])
    def login_post():
        user = UserController()

        email = request.form['email']
        password = request.form['password']

        result = user.login(email, password)

        if result:
            if result.role == 4:
                return render_template('login.html', data={'status': 401, 'msg': 'Seu usuário não tem permissão para acessar o admin', 'type':2})
            else:
                login_user(result)
                return redirect('/admin')
        else:
            return render_template('login.html', data={'status': 401, 'msg': 'Dados de usuário incorretos', 'type': 1})

    @app.route('/recovery-password/')
    def recovery_password():
        # Capítulo 11
        return render_template('recovery.html', data={'status': 200, 'msg': None, 'type': None})

    @app.route('/recovery-password/', methods=['POST'])
    def send_recovery_password():
        user = UserController()

        result = user.recovery(request.form['email'])

        # Capítulo 11 - Alterar parâmetros
        if result['status_code'] == 200 or result['status_code'] == 202:
            return render_template('recovery.html', data={'status': result['status_code'], 'msg': 'Você receberá um e-mail em sua caixa para alteração de senha.', 'type': 3})
        else:
            return render_template('recovery.html', data={'status': result['status_code'], 'msg': result['body'], 'type': 1})
    
    @app.route('/new-password/<recovery_code>')
    def new_password(recovery_code):
        user = UserController()
        result = user.verify_auth_token(recovery_code)
        
        if result['status'] == 200:
            res = user.get_user_by_recovery(str(recovery_code))
            if res is not None:
                return render_template('new_password.html', data={'status': result['status'], 'msg': None, 'type': None, 'user_id': res.id})
            else:
                return render_template('recovery.html', data={'status': 400, 'msg': 'Erro ao tentar acessar os dados do usuário. Tente novamente mais tarde.', 'type': 1})
        else:
            return render_template('recovery.html', data={'status': result['status'], 'msg': 'Token expirado ou inválido, solicite novamente a alteração de senha', 'type': 1})

    @app.route('/new-password/', methods=['POST'])
    def send_new_password():
        user = UserController()
        user_id = request.form['user_id']
        password = request.form['password']

        result = user.new_password(user_id, password)

        if result:
            return render_template('login.html', data={'status': 200, 'msg': 'Senha alterada com sucesso!', 'type': 3, 'user_id': user_id})
        else:
            return render_template('new_password.html', data={'status': 401, 'msg': 'Erro ao alterar senha.', 'type': 1, 'user_id': user_id})

    @app.route('/products/', methods=['GET'])
    @app.route('/products/<limit>', methods=['GET'])
    @auth_token_required
    def get_products(limit=None):
        header = {
            'access_token': request.headers['access_token'],
            "token_type": "JWT"
        }

        product = ProductController()
        response = product.get_products(limit=limit)
        return Response(json.dumps(response, ensure_ascii=False), mimetype='application/json'), response['status'], header

    @app.route('/product/<product_id>', methods=['GET'])
    @auth_token_required
    def get_product(product_id):
        header = {
            'access_token': request.headers['access_token'],
            "token_type": "JWT"
        }
        
        product = ProductController()
        response = product.get_product_by_id(product_id = product_id)

        return Response(json.dumps(response, ensure_ascii=False), mimetype='application/json'), response['status'], header

    @app.route('/user/<user_id>', methods=['GET'])
    @auth_token_required
    def get_user_profile(user_id):
        header = {
            'access_token': request.headers['access_token'],
            "token_type": "JWT"
        }

        user = UserController()
        response = user.get_user_by_id(user_id=user_id)

        return Response(json.dumps(response, ensure_ascii=False), mimetype='application/json'), response['status'], header

    @app.route('/login_api/', methods=['POST'])
    def login_api():
        header = {}
        user = UserController()

        email = request.json['email']
        password = request.json['password']

        result = user.login(email, password)
        code = 401
        response = {"message": "Usuário não autorizado", "result": []}

        if result:
            if result.active:
                result = {
                    'id': result.id,
                    'username': result.username,
                    'email': result.email,
                    'date_created': result.date_created,
                    'active': result.active
                }

                header = {
                    "access_token": user.generate_auth_token(result),
                    "token_type": "JWT"
                }
                code = 200
                response["message"] = "Login realizado com sucesso"
                response["result"] = result

        return Response(json.dumps(response, ensure_ascii=False), mimetype='application/json'), code, header
    
    @app.route('/logout')
    def logout_send():
        logout_user()
        return render_template('login.html', data={'status': 200, 'msg': 'Usuário deslogado com sucesso!', 'type':3})

    @login_manager.user_loader
    def load_user(user_id):
        user = UserController()
        return user.get_admin_login(user_id)
    

    @app.route('/minha_funcao')
    def minha_funcao():
    # Coloque o código que gera o HTML desejado aqui
        
        codigo_html = render_template('/etp/aside.html', )

        # Realize a modificação no código HTML
        codigo_html = codigo_html.replace('id="' + 'info_basico-nav' + '" class="nav-content collapse', 'id="' + 'info_basico-nav' + '" class="nav-content collapse show')
        
        return codigo_html

    app.jinja_env.globals.update(minha_funcao=minha_funcao)

##################################################################
    @app.route('/informacao1-94', methods=['POST', 'GET'])
    def informacao1_94():
        if request.method == 'POST':
            conteudoinformacao1 = request.form.get('conteudoinformacao1')
            session['conteudoinformacao1'] = conteudoinformacao1
            return redirect('/informacao1-94')

        # Verificar se a informação está armazenada na sessão
        conteudoinformacao1 = session.get('conteudoinformacao1')

        return render_template('etp94/1informacao-94.html', conteudoinformacao1=conteudoinformacao1)
    
    @app.route('/necessidade2-94', methods=['POST', 'GET'])
    def necessidade2_94():
        if request.method == 'POST':
            conteudonecessidade2 = request.form.get('conteudonecessidade2')
            session['conteudonecessidade2'] = conteudonecessidade2
            return redirect('/necessidade2-94')

        # Verificar se a informação está armazenada na sessão
        conteudonecessidade2 = session.get('conteudonecessidade2')

        return render_template('etp94/2necessidade-94.html', conteudonecessidade2=conteudonecessidade2)
    
    @app.route('/necessidade3-94', methods=['POST', 'GET'])
    def necessidade3_94():
        if request.method == 'POST':
            conteudonecessidade3 = request.form.get('conteudonecessidade3')
            session['conteudonecessidade3'] = conteudonecessidade3
            return redirect('/necessidade3-94')

        # Verificar se a informação está armazenada na sessão
        conteudonecessidade3 = session.get('conteudonecessidade3')

        return render_template('etp94/3necessidade-94.html', conteudonecessidade3=conteudonecessidade3)
    
    @app.route('/necessidade4-94', methods=['POST', 'GET'])
    def necessidade4_94():
        if request.method == 'POST':
            conteudonecessidade4 = request.form.get('conteudonecessidade4')
            session['conteudonecessidade4'] = conteudonecessidade4
            return redirect('/necessidade4-94')

        # Verificar se a informação está armazenada na sessão
        conteudonecessidade4 = session.get('conteudonecessidade4')

        return render_template('etp94/4necessidade-94.html', conteudonecessidade4=conteudonecessidade4)
    
    @app.route('/necessidade5-94', methods=['POST', 'GET'])
    def necessidade5_94():
        if request.method == 'POST':
            conteudonecessidade5 = request.form.get('conteudonecessidade5')
            session['conteudonecessidade5'] = conteudonecessidade5
            return redirect('/necessidade5-94')

        # Verificar se a informação está armazenada na sessão
        conteudonecessidade5 = session.get('conteudonecessidade5')

        return render_template('etp94/5necessidade-94.html', conteudonecessidade5=conteudonecessidade5)
    
    @app.route('/necessidade6-94', methods=['POST', 'GET'])
    def necessidade6_94():
        if request.method == 'POST':
            conteudonecessidade6 = request.form.get('conteudonecessidade6')
            session['conteudonecessidade6'] = conteudonecessidade6
            return redirect('/necessidade6-94')

        # Verificar se a informação está armazenada na sessão
        conteudonecessidade6 = session.get('conteudonecessidade6')

        return render_template('etp94/6necessidade-94.html', conteudonecessidade6=conteudonecessidade6)
    
    @app.route('/necessidade7-94', methods=['POST', 'GET'])
    def necessidade7_94():
        if request.method == 'POST':
            conteudonecessidade7 = request.form.get('conteudonecessidade7')
            session['conteudonecessidade7'] = conteudonecessidade7
            return redirect('/necessidade7-94')

        # Verificar se a informação está armazenada na sessão
        conteudonecessidade7 = session.get('conteudonecessidade7')

        return render_template('etp94/7necessidade-94.html', conteudonecessidade7=conteudonecessidade7)
    
    @app.route('/solucao8-94', methods=['POST', 'GET'])
    def solucao8_94():
        if request.method == 'POST':
            conteudosolucao8 = request.form.get('conteudosolucao8')
            session['conteudosolucao8'] = conteudosolucao8
            return redirect('/solucao8-94')

        # Verificar se a informação está armazenada na sessão
        conteudosolucao8 = session.get('conteudosolucao8')

        return render_template('etp94/8solucao-94.html', conteudosolucao8=conteudosolucao8)
    
    @app.route('/solucao9-94', methods=['POST', 'GET'])
    def solucao9_94():
        if request.method == 'POST':
            conteudosolucao9 = request.form.get('conteudosolucao9')
            session['conteudosolucao9'] = conteudosolucao9
            return redirect('/solucao9-94')

        # Verificar se a informação está armazenada na sessão
        conteudosolucao9 = session.get('conteudosolucao9')

        return render_template('etp94/9solucao-94.html', conteudosolucao9=conteudosolucao9)
    
    @app.route('/solucao10-94', methods=['POST', 'GET'])
    def solucao10_94():
        if request.method == 'POST':
            conteudosolucao10 = request.form.get('conteudosolucao10')
            session['conteudosolucao10'] = conteudosolucao10
            return redirect('/solucao10-94')

        # Verificar se a informação está armazenada na sessão
        conteudosolucao10 = session.get('conteudosolucao10')

        return render_template('etp94/10solucao-94.html', conteudosolucao10=conteudosolucao10)
    
    @app.route('/solucao11-94', methods=['POST', 'GET'])
    def solucao11_94():
        if request.method == 'POST':
            conteudosolucao11 = request.form.get('conteudosolucao11')
            session['conteudosolucao11'] = conteudosolucao11
            return redirect('/solucao11-94')

        # Verificar se a informação está armazenada na sessão
        conteudosolucao11 = session.get('conteudosolucao11')

        return render_template('etp94/11solucao-94.html', conteudosolucao11=conteudosolucao11)
    
    @app.route('/solucao12-94', methods=['POST', 'GET'])
    def solucao12_94():
        if request.method == 'POST':
            conteudosolucao12 = request.form.get('conteudosolucao12')
            session['conteudosolucao12'] = conteudosolucao12
            return redirect('/solucao12-94')

        # Verificar se a informação está armazenada na sessão
        conteudosolucao12 = session.get('conteudosolucao12')

        return render_template('etp94/12solucao-94.html', conteudosolucao12=conteudosolucao12)
    
    @app.route('/solucao13-94', methods=['POST', 'GET'])
    def solucao13_94():
        if request.method == 'POST':
            conteudosolucao13 = request.form.get('conteudosolucao13')
            session['conteudosolucao13'] = conteudosolucao13
            return redirect('/solucao13-94')

        # Verificar se a informação está armazenada na sessão
        conteudosolucao13 = session.get('conteudosolucao13')

        return render_template('etp94/13solucao-94.html', conteudosolucao13=conteudosolucao13)
    
    @app.route('/solucao14-94', methods=['POST', 'GET'])
    def solucao14_94():
        if request.method == 'POST':
            conteudosolucao14 = request.form.get('conteudosolucao14')
            session['conteudosolucao14'] = conteudosolucao14
            return redirect('/solucao14-94')

        # Verificar se a informação está armazenada na sessão
        conteudosolucao14 = session.get('conteudosolucao14')

        return render_template('etp94/14solucao-94.html', conteudosolucao14=conteudosolucao14)
    
    @app.route('/solucao15-94', methods=['POST', 'GET'])
    def solucao15_94():
        if request.method == 'POST':
            conteudosolucao15 = request.form.get('conteudosolucao15')
            session['conteudosolucao15'] = conteudosolucao15
            return redirect('/solucao15-94')

        # Verificar se a informação está armazenada na sessão
        conteudosolucao15 = session.get('conteudosolucao15')

        return render_template('etp94/15solucao-94.html', conteudosolucao15=conteudosolucao15)
    
    @app.route('/planejamento16-94', methods=['POST', 'GET'])
    def planejamento16_94():
        if request.method == 'POST':
            conteudoplanejamento16 = request.form.get('conteudoplanejamento16')
            session['conteudoplanejamento16'] = conteudoplanejamento16
            return redirect('/planejamento16-94')

        # Verificar se a informação está armazenada na sessão
        conteudoplanejamento16 = session.get('conteudoplanejamento16')

        return render_template('etp94/16planejamento-94.html', conteudoplanejamento16=conteudoplanejamento16)
    
    @app.route('/planejamento17-94', methods=['POST', 'GET'])
    def planejamento17_94():
        if request.method == 'POST':
            conteudoplanejamento17 = request.form.get('conteudoplanejamento17')
            session['conteudoplanejamento17'] = conteudoplanejamento17
            return redirect('/planejamento17-94')

        # Verificar se a informação está armazenada na sessão
        conteudoplanejamento17 = session.get('conteudoplanejamento17')

        return render_template('etp94/17planejamento-94.html', conteudoplanejamento17=conteudoplanejamento17)
       
    @app.route('/viabilidade18-94', methods=['POST', 'GET'])
    def viabilidade18_94():
        if request.method == 'POST':
            conteudoviabilidade18 = request.form.get('conteudoviabilidade18')
            session['conteudoviabilidade18'] = conteudoviabilidade18
            return redirect('/viabilidade18-94')

        # Verificar se a informação está armazenada na sessão
        conteudoviabilidade18 = session.get('conteudoviabilidade18')

        return render_template('etp94/18viabilidade-94.html', conteudoviabilidade18=conteudoviabilidade18)
    
    @app.route('/viabilidade19-94', methods=['POST', 'GET'])
    def viabilidade19_94():
        if request.method == 'POST':
            conteudoviabilidade19 = request.form.get('conteudoviabilidade19')
            session['conteudoviabilidade19'] = conteudoviabilidade19
            return redirect('/viabilidade19-94')

        # Verificar se a informação está armazenada na sessão
        conteudoviabilidade19 = session.get('conteudoviabilidade19')

        return render_template('etp94/19viabilidade-94.html', conteudoviabilidade19=conteudoviabilidade19)
    
    @app.route('/ultima-94', methods=['POST'])
    def ultima_94():
        conteudoultimo = session.get('conteudoultimo')
        sessoes = ['conteudo', 'conteudo2']
        for sessao in sessoes:
            session.pop(sessao, None)
        return render_template('ultima-94.html')
    




##################################################################

# Registre a função no Jinja2

    return app
