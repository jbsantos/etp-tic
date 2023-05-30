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

from admin.Views import UserView, HomeView, RoleView, CategoryView, ProductView, PaginasView

def start_views(app, db):
    admin = Admin(app, name='ETP ', base_template='admin/base.html', template_mode='bootstrap3', index_view=HomeView())

    admin.add_view(RoleView(Role, db.session, "Funções",  category="Usuários"))
    admin.add_view(UserView(User, db.session, "Usuários", category="Usuários"))
    admin.add_view(CategoryView(Category, db.session, 'Categorias', category="ETP DIGITAL"))
    admin.add_view(ProductView(Product, db.session, "Cadastro", category="ETP DIGITAL"))
    admin.add_view(PaginasView(Paginas, db.session, 'Manual', category="Informações"))



    admin.add_link(MenuLink(name='Logout', url='/logout'))
