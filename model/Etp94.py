# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, desc, asc, distinct, and_, or_
from sqlalchemy.orm import relationship
from config import app_active, app_config
from model.User import User
from flask import session

config = app_config[app_active]
db = SQLAlchemy(config.APP)

class Etp94(db.Model):
        
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    informacao1_94 = db.Column(db.Text)
    necessidade2_94 = db.Column(db.Text)
    necessidade3_94 = db.Column(db.Text)
    necessidade4_94 = db.Column(db.Text)
    necessidade5_94 = db.Column(db.Text)
    necessidade6_94 = db.Column(db.Text)
    necessidade7_94 = db.Column(db.Text)
    solucao8_94 = db.Column(db.Text)
    solucao9_94 = db.Column(db.Text)
    solucao10_94 = db.Column(db.Text)
    solucao11_94 = db.Column(db.Text)
    solucao12_94 = db.Column(db.Text)
    solucao13_94 = db.Column(db.Text)
    solucao14_94 = db.Column(db.Text)
    solucao15_94 = db.Column(db.Text)
    planejamento16_94 = db.Column(db.Text)
    planejamento17_94 = db.Column(db.Text)
    viabilidade18_94 = db.Column(db.Text)
    viabilidade19_94 = db.Column(db.Text)
    date_created = db.Column(db.DateTime(6), default=db.func.current_timestamp(), nullable=False)

    usuario_id = db.Column(db.Integer, db.ForeignKey(User.id))
    usuario = relationship(User)
    
    # def __init__(self, informacao1_94, necessidade2_94, necessidade3_94, necessidade4_94, solucao5_94, solucao6_94, solucao7_94, solucao8_94, solucao9_94, solucao10_94, solucao11_94, planejamento12_94, planejamento13_94, planejamento14_94, viabilidade15_94, viabilidade16_94, usuario_id):
    #     self.informacao1_94 = informacao1_94
    #     self.necessidade2_94 = necessidade2_94
    #     self.necessidade3_94 = necessidade3_94
    #     self.necessidade4_94 = necessidade4_94
    #     self.solucao5_94 = solucao5_94
    #     self.solucao6_94 = solucao6_94
    #     self.solucao7_94 = solucao7_94
    #     self.solucao8_94 = solucao8_94
    #     self.solucao9_94 = solucao9_94
    #     self.solucao10_94 = solucao10_94
    #     self.solucao11_94 = solucao11_94
    #     self.planejamento12_94 = planejamento12_94
    #     self.planejamento13_94 = planejamento13_94
    #     self.planejamento14_94 = planejamento14_94
    #     self.viabilidade15_94 = viabilidade15_94
    #     self.viabilidade16_94 = viabilidade16_94
    #     self.usuario_id = usuario_id

    def get_all(self):
        try:
            res = db.session.query(Etp94).all()
            
        except Exception as e:
            res = []
            print(e)
        finally:
            db.session.close()
            return res
        
    def get_etp94_by_id(self, id):
        try:
         
            res = db.session.query(Etp94).filter(Etp94.usuario_id==id).all()
          
        except Exception as e:
            res = []
            print(e)
        finally:
            db.session.close()
            return res
        
    def get_etp94_formulario_by_id(form_id):
        try:
            res = db.session.query(Etp94).filter(Etp94.id==form_id).first()
            print(res)
        except Exception as e:
            res = []
            print(e)
        finally:
            db.session.close()
            return res
        
    def get_ultimo_id_formulario():
            try:
                res = db.session.query(Etp94).order_by(Etp94.id.desc()).first()
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
    
    def salvar_edicao_etp94(form_id):

        etp94 = Etp94.query.filter_by(id=form_id).first()
      
        if etp94 is not None:
            etp94.informacao1_94 = session['1']
            etp94.necessidade2_94 = session['2']
            etp94.necessidade3_94 = session['3']
            etp94.necessidade4_94 = session['4']
            etp94.necessidade5_94 = session['5']
            etp94.necessidade6_94 = session['6']
            etp94.necessidade7_94 = session['7']
            etp94.solucao8_94 = session['8']
            etp94.solucao9_94 = session['9']
            etp94.solucao10_94 = session['10']
            etp94.solucao11_94 = session['11']
            etp94.solucao12_94 = session['12']
            etp94.solucao13_94 = session['13']
            etp94.solucao14_94 = session['14']
            etp94.solucao15_94 = session['15']
            etp94.planejamento16_94 = session['16']
            etp94.planejamento17_94 = session['17']
            etp94.viabilidade18_94 = session['18']
            etp94.viabilidade19_94 = session['19']
            # etp94.data_create =  '2023-6-24:15:42:21'
            # etp94.usuario_id = 7
            
            try:
 
                db.session.commit()
                return "Registro atualizado com sucesso."
            except Exception as e:
                db.session.rollback()
                print(e)
                return "Ocorreu um erro ao atualizar o registro."

        else:
            return "Registro não encontrado."
    
    def update(obj):
        try:
            
            data = vars(obj)  # Converter o objeto Etp94 em um dicionário
            print(data)
            res = db.session.query(Etp94).filter(Etp94.id == obj.id).update(data)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            db.session.rollback()
            return False

    def delete(form_id):
        try:
            res = db.session.query(Etp94).filter(Etp94.id == form_id).delete()
            db.session.commit()

            return True
        except Exception as e:
            return False

