# -*- coding: utf-8 -*-
from sqlalchemy import func
from flask_sqlalchemy import SQLAlchemy
from config import app_active, app_config
from model.User import User

config = app_config[app_active]
db = SQLAlchemy(config.APP)

class Paginas(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(15), unique=True, nullable=False)
    descricao = db.Column(db.Text(), nullable=True)

    def __repr__(self):
        return self.nome

    # def get_total_paginas(self):
    #     try:
    #         res = db.session.query(func.count(Paginas.id)).first()
    #         if res == 0 or res == None:
    #             res=1
    #     except Exception as e:
    #         res = []
    #         print(e)
    #     finally:
    #         db.session.close()
    #         return res