from flask_restful import Resource
from modelos.loja import LojaModel

class Loja(Resource):
    
    def get(self, nome):
        loja = LojaModel.buscar_por_nome(nome)
        if loja:
            return loja.json()
        return {'mensagem': 'Loja não encontrada'}, 404

    def post(self, nome):
        if LojaModel.buscar_por_nome(nome):
            return {'mensagem': "Loja com nome {} já existe.".format(nome)}

        loja = LojaModel(nome)
        try:
            loja.insere()
        except :
            return {'mensagem': "Um erro ocorreu na inserção."}, 500

        return loja.json(), 201 # indica criação 

    def delete(self, nome):
        loja = LojaModel.buscar_por_nome(nome)

        if loja:
            loja.remove()

        return {'mensagem': 'Loja removido'}

class LojaList(Resource):

    def get(self):
        return {'lojas': [loja.json() for loja in LojaModel.query.all()]}
