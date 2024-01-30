# -*- coding: utf-8 -*-
from flask_admin import AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
# Capítulo 10
from flask_login import current_user
from flask import redirect,request
from wtforms.fields import StringField
from wtforms.widgets import TextInput
from flask_admin.form import DateTimePickerWidget
from wtforms import DateTimeField
from wtforms import StringField
from flask_admin.form import widgets

from config import app_config, app_active

from model.User import User
from model.Category import Category
from model.Product import Product
from model.Etp40 import Etp40
from model.Etp94 import Etp94
import datetime

from flask_admin.contrib.sqla import ModelView
from wtforms import DateTimeLocalField
from flask_admin.form import DateTimePickerWidget
from flask import request, redirect
from flask_login import current_user

#import locale
#locale.setlocale(locale.LC_ALL,'pt_BR.ISO8859-1')
config = app_config[app_active]

class HomeView(AdminIndexView):
    extra_css = [config.URL_MAIN + 'static/css/home.css','https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css']

    @expose('/')
    def index(self):
        user_model = User()
        category_model = Category()
        #product_model = Product()
        etpa40_model = Etp40()
        etp94_model = Etp94()
       
        etp40 = etpa40_model.get_all()
        etp94 = etp94_model.get_all()
        
        if len(etp40) == 0:
            print('etp vazio')
            etp40 = 'por favor registre'

        if len(etp94) == 0:
            print('etp vazio')
            etp94 = 'por favor registre'

        
        etpa40_by_id = etpa40_model.get_etp40_by_id(current_user.id) 
        if etpa40_by_id == None or etpa40_by_id == '':
            etpa40_by_id = 'Não há registro'
        
        etp94_by_id = etp94_model.get_etp94_by_id(current_user.id) 
        if etp94_by_id == None or etp94_by_id == '':
            etp94_by_id = 'Não há registro'

        users = user_model.get_total_users()
        categories = category_model.get_total_categories()
        #products = product_model.get_total_products()
        #last_products = product_model.get_last_products()
        data_sistema  = str(datetime.datetime.now().strftime('%B'))
        return self.render('home_admin.html', report={
            'users': users[0],
            'categories': categories[0],
          #  'products': products[0],
            'etp40': etp40[0],
            'etp40_id':etpa40_by_id,
            'etp94': etp94[0],
            'etp94_id':etp94_by_id,
            
        }, etp40 = etpa40_by_id,  etp94 = etp94_by_id, data_sistema=data_sistema)


    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self,name,**kwargs):
        if current_user.is_authenticated:
            return redirect('/admin')
        else:
            return redirect('/login')
        

            



class UserView(ModelView):
    def on_form_prefill(self, form, id):
        if request and request.method == 'GET':
            model = self.get_one(id)
            form.date_created.data = model.date_created.strftime('%Y-%m-%d %H:%M:%S') if model.date_created else ''

    form_args = {
        'date_created': {
            'widget': DateTimeLocalField()
        }
    }

    column_labels = {
        'funcao': 'Função',
        'username': 'Nome de usuário',
        'email': 'E-mail',
        'date_created': 'Data de Criação',
        'last_update': 'Última atualização',        
        'active': 'Estado',
        'password': 'Senha',
    }

    column_descriptions = {
        'funcao': 'Função no painel administrativo',
        'username': 'Nome de usuário no sistema',
        'email': 'E-mail do usuário no sistema',
        'date_created': 'Data de Criação do usuário no sistema',
        'last_update': 'Última atualização desse usuário no sistema',        
        'active': 'Estado ativo ou inativo no sistema',
        'password': 'Senha do usuário no sistema',
    }

    column_exclude_list = ['password', 'recovery_code']
    form_excluded_columns = ['last_update', 'recovery_code']

    form_widget_args = {
        'password': {
            'type': 'password'
        }
    }
    

    form_widget_args = {
        'date_created': {
            'widget': widgets.DateTimePickerWidget()
        }
    }
    form_overrides = {
        'date_created': StringField
    }

    form_args = {
        'date_created': {
            'widget': widgets.DateTimePickerWidget()
        }
    }

    can_set_page_size = True
    can_view_details = True
    column_searchable_list = ['username', 'email']
    column_filters = ['username', 'email', 'funcao']
    create_modal = True
    edit_modal = True
    can_export = True
    column_editable_list = ['username', 'email', 'funcao', 'active']
    column_sortable_list = ['username']
    column_default_sort = [('username', True), ('date_created', True)]
    column_details_exclude_list = ['password', 'recovery_code']
    column_export_exclude_list = ['password', 'recovery_code']

    export_types = ['json', 'yaml', 'csv', 'xls', 'df']

    def on_model_change(self, form, User, is_created):
        if 'password' in form:
            if form.password.data is not None:
                User.set_password(form.password.data)
            else:
                del form.password
        # Inverter formato da data antes de salvar no banco
        if 'date_created' in form:
            if form.date_created.data:
                print(type(form.date_created.data), 'testeeee')
                # Converter a string de data no formato correto
                date_created = datetime.datetime.strptime(form.date_created.data, '%Y-%m-%d %H:%M:%S')
                #form.date_created.data = datetime.strptime(form.date_created.data, '%d-%m-%Y %H:%M:%S')
                # Converter novamente em string no formato desejado
                form.date_created.data = date_created.strftime('%Y-%m-%d %H:%M:%S')

    # Capítulo 10
    def is_accessible(self):
        role = current_user.role
        if role == 1:
            self.can_create = True
            self.can_edit = True
            self.can_delete = True
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        if current_user.is_authenticated:
            return redirect('/admin')
        else:
            return redirect('/login')


# Capítulo 10
class RoleView(ModelView):
    def is_accessible(self):
        role = current_user.role
        if role == 1:
            self.can_create = True
            self.can_edit = True
            self.can_delete = True
            return current_user.is_authenticated


class PaginasView(ModelView):
    can_view_details = True
    create_modal = True
    edit_modal = True
    column_display_pk = True
    can_view_details = True

    base_template = 'admin_base.html'
    def is_accessible(self):
        role = current_user.role
        if role == 1:
            self.can_create = True
            self.can_edit = True
            self.can_delete = True
            return current_user.is_authenticated
    def inaccessible_callback(self,name,**kwargs):
        if current_user.is_authenticated:
            return redirect('/admin')
        else:
            return redirect('/login')

class Etp40View(ModelView):
    can_view_details = True
    create_modal = True
    edit_modal = True
    column_display_pk = True
    can_view_details = True

    base_template = 'admin_base.html'
    def is_accessible(self):
        role = current_user.role
        if role == 1:
            self.can_create = True
            self.can_edit = True
            self.can_delete = True
            return current_user.is_authenticated
    def inaccessible_callback(self,name,**kwargs):
        if current_user.is_authenticated:
            return redirect('/admin')
        else:
            return redirect('/login')
   
class Etp94View(ModelView):
    can_view_details = True
    create_modal = True
    edit_modal = True
    column_display_pk = True
    can_view_details = True

    base_template = 'admin_base.html'
    def is_accessible(self):
        role = current_user.role
        if role == 1:
            self.can_create = True
            self.can_edit = True
            self.can_delete = True
            return current_user.is_authenticated
    def inaccessible_callback(self,name,**kwargs):
        if current_user.is_authenticated:
            return redirect('/admin')
        else:
            return redirect('/login')
       
class CategoryView(ModelView):
    base_template = 'admin_base.html'
    can_view_details = True

    def is_accessible(self):
        role = current_user.role
        if role == 1:
            self.can_create = True
            self.can_edit = True
            self.can_delete = True
            return current_user.is_authenticated
        elif role == 2:
            self.can_create = True
            self.can_edit = True
            self.can_delete = True
            return current_user.is_authenticated

    def inaccessible_callback(self,name,**kwargs):
        if current_user.is_authenticated:
            return redirect('/admin')
        else:
            return redirect('/login')

class ProductView(ModelView):
    base_template = 'admin_base.html'
    can_view_details = True
    
    def is_accessible(self):
        role = current_user.role
        if role == 1:
            self.can_create = True
            self.can_edit = True
            self.can_delete = True
        elif role == 2:
            self.can_create = True
            self.can_edit = True
            self.can_delete = True
        elif role == 3:
            self.can_create = True
            self.can_edit = True
            self.can_delete = False

        return current_user.is_authenticated

    def inaccessible_callback(self,name,**kwargs):
        if current_user.is_authenticated:
            return redirect('/admin')
        else:
            return redirect('/login')