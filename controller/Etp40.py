from datetime import datetime

from model.Product import Product
from model.User import User
from model.Etp40 import Etp40
from flask import jsonify

class Etp40Controller:
    def get_etp40(self, limit):    
        result = []
        try:
            etp40_objects = Etp40.query.limit(limit).all()

            for etp40 in etp40_objects:
                result.append({
                    'id': etp40.id,
                    'informacao1_40': etp40.informacao1_40,
                    'necessidade2_40': etp40.necessidade2_40,
                    'necessidade3_40': etp40.necessidade3_40,
                    'necessidade4_40': etp40.necessidade4_40,
                    'solucao5_40': etp40.solucao5_40,
                    'solucao6_40': etp40.solucao6_40,
                    'solucao7_40': etp40.solucao7_40,
                    'solucao8_40': etp40.solucao8_40,
                    'solucao9_40': etp40.solucao9_40,
                    'solucao10_40': etp40.solucao10_40,
                    'solucao11_40': etp40.solucao11_40,
                    'planejamento12_40': etp40.planejamento12_40,
                    'planejamento13_40': etp40.planejamento13_40,
                    'planejamento14_40': etp40.planejamento14_40,
                    'viabilidade15_40': etp40.viabilidade15_40,
                    'viabilidade16_40': etp40.viabilidade16_40,
                    'usuario_id': etp40.usuario_id,
                     'date_created': etp40.date_created

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

    def get_etp40_by_id(self, id):
        try:
            etp40 = Etp40.query.get(id)
            print(etp40.__dict__)
            if etp40:
                result = {
                    'id': etp40.id,
                    'informacao1_40': etp40.informacao1_40,
                    'necessidade2_40': etp40.necessidade2_40,
                    'necessidade3_40': etp40.necessidade3_40,
                    'necessidade4_40': etp40.necessidade4_40,
                    'solucao5_40': etp40.solucao5_40,
                    'solucao6_40': etp40.solucao6_40,
                    'solucao7_40': etp40.solucao7_40,
                    'solucao8_40': etp40.solucao8_40,
                    'solucao9_40': etp40.solucao9_40,
                    'solucao10_40': etp40.solucao10_40,
                    'solucao11_40': etp40.solucao11_40,
                    'planejamento12_40': etp40.planejamento12_40,
                    'planejamento13_40': etp40.planejamento13_40,
                    'planejamento14_40': etp40.planejamento14_40,
                    'viabilidade15_40': etp40.viabilidade15_40,
                    'viabilidade16_40': etp40.viabilidade16_40,
                    'usuario_id': etp40.usuario_id,
                    'date_created': etp40.date_created

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
