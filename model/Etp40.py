# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, desc, asc, distinct, and_, or_
from sqlalchemy.orm import relationship
from config import app_active, app_config
from model.User import User
from model.Category import Category

config = app_config[app_active]
db = SQLAlchemy(config.APP)

class Etp40(db.Model):
        
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    informacao1_40 = db.Column(db.Text)
    necessidade2_40 = db.Column(db.Text)
    necessidade3_40 = db.Column(db.Text)
    necessidade4_40 = db.Column(db.Text)
    solucao5_40 = db.Column(db.Text)
    solucao6_40 = db.Column(db.Text)
    solucao7_40 = db.Column(db.Text)
    solucao8_40 = db.Column(db.Text)
    solucao9_40 = db.Column(db.Text)
    solucao10_40 = db.Column(db.Text)
    solucao11_40 = db.Column(db.Text)
    planejamento12_40 = db.Column(db.Text)
    planejamento13_40 = db.Column(db.Text)
    planejamento14_40 = db.Column(db.Text)
    viabilidade15_40 = db.Column(db.Text)
    viabilidade16_40 = db.Column(db.Text)
    date_created = db.Column(db.DateTime(6), default=db.func.current_timestamp(), nullable=False)

    usuario_id = db.Column(db.Integer, db.ForeignKey(User.id))
    usuario = relationship(User)
    
    # def __init__(self, informacao1_40, necessidade2_40, necessidade3_40, necessidade4_40, solucao5_40, solucao6_40, solucao7_40, solucao8_40, solucao9_40, solucao10_40, solucao11_40, planejamento12_40, planejamento13_40, planejamento14_40, viabilidade15_40, viabilidade16_40, usuario_id):
    #     self.informacao1_40 = informacao1_40
    #     self.necessidade2_40 = necessidade2_40
    #     self.necessidade3_40 = necessidade3_40
    #     self.necessidade4_40 = necessidade4_40
    #     self.solucao5_40 = solucao5_40
    #     self.solucao6_40 = solucao6_40
    #     self.solucao7_40 = solucao7_40
    #     self.solucao8_40 = solucao8_40
    #     self.solucao9_40 = solucao9_40
    #     self.solucao10_40 = solucao10_40
    #     self.solucao11_40 = solucao11_40
    #     self.planejamento12_40 = planejamento12_40
    #     self.planejamento13_40 = planejamento13_40
    #     self.planejamento14_40 = planejamento14_40
    #     self.viabilidade15_40 = viabilidade15_40
    #     self.viabilidade16_40 = viabilidade16_40
    #     self.usuario_id = usuario_id

    def get_all(self):
        try:
     
            res = db.session.query(Etp40).all()
            
        except Exception as e:
            res = []
            print(e)
        finally:
            db.session.close()
            return res
        
    def get_etp40_by_id(self, id):
        try:
         
            res = db.session.query(Etp40).filter(Etp40.usuario_id==id).all()
          
        except Exception as e:
            res = []
            print(e)
        finally:
            db.session.close()
            return res
    
    def save(self):
        print(self)
        db.session.add(self)  # Adiciona o objeto ao contexto de sessão do SQLAlchemy
        result = db.session.commit()  # Confirma as alterações no banco de dados
        return result