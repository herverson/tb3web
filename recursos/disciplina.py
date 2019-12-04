from flask_jwt import jwt_required
from flask_restful import Resource
from flask_restful import Resource, reqparse
from modelos.disciplina import DisciplinaModel

class Disciplina(Resource):
    parser = reqparse.RequestParser()
    def get(self, id):
        disciplina = DisciplinaModel.buscar_por_id(id)
        if disciplina:
            return disciplina.json()
        return {'mensagem': 'Disciplina não encontrada'}, 404

    def post(self, id):
        if DisciplinaModel.buscar_por_nome(id):
            return {'mensagem': "Disciplina com nome {} já existe.".format(id)}

        disciplina = DisciplinaModel(id)
        try:
            disciplina.insere()
        except :
            return {'mensagem': "Um erro ocorreu na inserção."}, 500

        return disciplina.json(), 201 # indica criação

    def delete(self, id):
        disciplina = DisciplinaModel.buscar_por_nome(id)

        if disciplina:
            disciplina.remove()
        else:
            return {'mensagem': 'Disciplina não encontrada'}

        return {'mensagem': 'Disciplina removido'}

    def put(self, id):
        dado = Disciplina.parser.parse_args()
        topico = DisciplinaModel.buscar_por_nome(id)
        if topico is None:
            topico = DisciplinaModel(id, **dado)
        else:
            topico.nome
        topico.insere()
        return topico.json()

class DisciplinaList(Resource):

    def get(self):
        return {'Disciplinas': [disciplina.json() for disciplina in DisciplinaModel.query.all()]}

