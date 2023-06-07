# -*- coding: utf-8 -*-
from flask import Flask, request,url_for, redirect, render_template, Response, json, abort, session, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, login_user, logout_user
from functools import wraps
#from bs4 import BeautifulSoup

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
        return render_template('/etp40/index.html')
    
    @app.route('/etp94')
    def etp94():
        return render_template('/etp94/etp94.html')
    
    @app.route('/etp40')
    def etp40():
    #     # Abrir o arquivo HTML e ler o seu conteúdo
    #     with open('templates/etp40/aside.html', 'r') as file:
    #         html = file.read()
    #     soup = BeautifulSoup(html, 'html.parser')

    # # Encontrar todos os elementos <a> e obter o valor do atributo href
    #     href_values = [a['href'] for a in soup.find_all('a')]

    #     print(str(href_values))
    #     return render_template('resultado.html', href_values=href_values)
        return render_template('/etp40/etp40.html')
    
    @app.route('/informacoes1-40',methods=['POST', 'GET'])
    def informacoes1_40():

        return render_template('etp40/1informacoes-40.html')
    
    @app.route('/necessidade2-40',methods=['POST', 'GET'])
    def necessidade2_40():
        
        return render_template('etp40/2necessidade-40.html')
    
    @app.route('/necessidade3-40',methods=['POST', 'GET'])
    def necessidade3_40():

        return render_template('etp40/3necessidade-40.html')
    
    @app.route('/necessidade4-40',methods=['POST', 'GET'])
    def necessidade4_40():

        return render_template('etp40/4necessidade-40.html')

    @app.route('/solucao5-40',methods=['POST', 'GET'])
    def solucao5_40():
        return render_template('etp40/5solucao-40.html')
    
    @app.route('/solucao6-40',methods=['POST', 'GET'])
    def solucao6_40():
        return render_template('etp40/6solucao-40.html')
    
    @app.route('/solucao7-40',methods=['POST', 'GET'])
    def solucao7_40():
        return render_template('etp40/7solucao-40.html')
       
    @app.route('/solucao8-40',methods=['POST', 'GET'])
    def solucao8_40():
        return render_template('etp40/8solucao-40.html')
    
    @app.route('/solucao9-40',methods=['POST', 'GET'])
    def solucao9_40():
        return render_template('etp40/9solucao-40.html')
    
    @app.route('/solucao10-40',methods=['POST', 'GET'])
    def solucao10_40():
        return render_template('etp40/10solucao-40.html')    
    
    @app.route('/solucao11-40',methods=['POST', 'GET'])
    def solucao11_40():
        return render_template('etp40/11solucao-40.html')  
    
    @app.route('/planejamento12-40',methods=['POST', 'GET'])
    def planejamento12_40():
        return render_template('etp40/12planejamento-40.html') 
    
    @app.route('/planejamento13-40',methods=['POST', 'GET'])
    def planejamento13_40():
        return render_template('etp40/13planejamento-40.html') 
    
    @app.route('/planejamento14-40',methods=['POST', 'GET'])
    def planejamento14_40():
        return render_template('etp40/14planejamento-40.html') 
    
    @app.route('/viabilidade15-40',methods=['POST', 'GET'])
    def viabilidade15_40():
        return render_template('etp40/15viabilidade-40.html') 

    @app.route('/viabilidade16-40',methods=['POST', 'GET'])
    def viabilidade16_40():
        return render_template('etp40/16viabilidade-40.html') 
    
    @app.route('/profile',methods=['POST', 'GET'])
    def profile():
        return render_template('etp40/users-profile.html') 
    
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
        
        codigo_html = render_template('/etp40/aside.html', )

        # Realize a modificação no código HTML
        codigo_html = codigo_html.replace('id="' + 'info_basico-nav' + '" class="nav-content collapse', 'id="' + 'info_basico-nav' + '" class="nav-content collapse show')
        
        return codigo_html

    app.jinja_env.globals.update(minha_funcao=minha_funcao)


# Registre a função no Jinja2

    return app
