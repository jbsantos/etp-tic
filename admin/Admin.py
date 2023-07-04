# -*- coding: utf-8 -*-
from flask_admin import Admin
# Capítulo 10 - Remover
from flask_admin.contrib.sqla import ModelView
from flask_admin.menu import MenuLink

from model.Role import Role
from model.User import User
from model.Category import Category
from model.Product import Product
from model.Paginas import Paginas
from model.Etp40 import Etp40
from model.Etp94 import Etp94

from admin.Views import UserView, HomeView, RoleView, CategoryView, ProductView, PaginasView, Etp40View, Etp94View

def start_views(app, db):
    admin = Admin(app, name='ETP DIGITAL SYSTEM', base_template='admin/base.html', template_mode='bootstrap3', index_view=HomeView())

    admin.add_view(RoleView(Role, db.session, "Funções",  category="Usuários"))
    admin.add_view(UserView(User, db.session, "Usuários", category="Usuários"))
    admin.add_view(CategoryView(Category, db.session, 'Categorias', category="ETP DIGITAL"))
    admin.add_view(ProductView(Product, db.session, "Cadastro", category="ETP DIGITAL"))
    admin.add_view(PaginasView(Paginas, db.session, 'Manual', category="Informações"))
    admin.add_view(Etp40View(Etp40, db.session, 'ETP40', category="Registro ETP"))
    admin.add_view(Etp94View(Etp94, db.session, 'ETP94', category="Registro ETP"))




    admin.add_link(MenuLink(name='Logout', url='/logout'))
