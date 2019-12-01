from flask_restful import Resource
from modelos.loja import DisciplinaModel

class Loja(Resource):
    
    def get(self, id):
        loja = DisciplinaModel.buscar_por_id(id)
        if loja:
            return loja.json()
        return {'mensagem': 'Disciplina não encontrada'}, 404

    def post(self, id):
        if DisciplinaModel.buscar_por_nome(id):
            return {'mensagem': "Disciplina com nome {} já existe.".format(id)}

        loja = DisciplinaModel(id)
        try:
            loja.insere()
        except :
            return {'mensagem': "Um erro ocorreu na inserção."}, 500

        return loja.json(), 201 # indica criação 

    def delete(self, id):
        loja = DisciplinaModel.buscar_por_nome(id)

        if loja:
            loja.remove()

        return {'mensagem': 'Loja removido'}

class LojaList(Resource):

    def get(self):
        return {'Disciplinas': [loja.json() for loja in DisciplinaModel.query.all()]}

