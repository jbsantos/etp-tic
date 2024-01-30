# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, desc, asc, distinct, and_, or_
from sqlalchemy.orm import relationship
from config import app_active, app_config
from model.User import User
from model.Category import Category
from flask import session

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
        
    def get_etp40_formulario_by_id(form_id):
        try:
            res = db.session.query(Etp40).filter(Etp40.id==form_id).first()
            print(res)
        except Exception as e:
            res = []
            print(e)
        finally:
            db.session.close()
            return res
        
    def get_ultimo_id_formulario():
            try:
                res = db.session.query(Etp40).order_by(Etp40.id.desc()).first()
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
    
    
    
    def salvar_edicao_etp40(form_id):

        etp40 = Etp40.query.filter_by(id=form_id).first()
        print(etp40.__dict__)
      
        if etp40 is not None:
            etp40.informacao1_40 = session['1']
            etp40.necessidade2_40 = session['2']
            etp40.necessidade3_40 = session['3']
            etp40.necessidade4_40 = session['4']
            etp40.solucao5_40 = session['5']
            etp40.solucao6_40 = session['6']
            etp40.solucao7_40 = session['7']
            etp40.solucao8_40 = session['8']
            etp40.solucao9_40 = session['9']
            etp40.solucao10_40 = session['10']
            etp40.solucao11_40 = session['11']
            etp40.planejamento12_40 = session['12']
            etp40.planejamento13_40 = session['13']
            etp40.planejamento14_40 = session['14']
            etp40.viabilidade15_40 = session['15']
            etp40.viabilidade16_40 = session['16']
            # etp40.data_create =  '2023-6-24:15:42:21'
            # etp40.usuario_id = 7
            
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
            
            data = vars(obj)  # Converter o objeto Etp40 em um dicionário
            print(data)
            res = db.session.query(Etp40).filter(Etp40.id == obj.id).update(data)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            db.session.rollback()
            return False

    def delete(form_id):
        try:
            res = db.session.query(Etp40).filter(Etp40.id == form_id).delete()
            db.session.commit()

            return True
        except Exception as e:
            return False
