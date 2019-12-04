import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from modelos.topico import TopicoModel

class Topico(Resource):
    __tablename__ = 'topicos'

    parser = reqparse.RequestParser()
    #
    # parser.add_argument('preco',
    #                     type=float,
    #                     required=True,
    #                     help="Campo preco obrigatório.")

    parser.add_argument('id_disciplina',
                        type=int,
                        required=True,
                        help="Campo id_disciplina obrigatório.")

    @jwt_required()
    def get(self, iddisciplina, id):
        topico = TopicoModel.buscar_por_id(id)
        if topico:
            return topico.json()
        return {'mensagem': 'Tópico não encontrado'}, 404

    # @jwt_required()
    def post(self, iddisciplina, id):
        if TopicoModel.buscar_por_nome(id):
            return {'mensagem': "Tópico com nome {} já existe.".format(id)}
        dado = Topico.parser.parse_args()
        # print(dado)
        # print(id)
        topico = TopicoModel(id, **dado)

        try:
            topico.insere()
        except :
            return {'mensagem': "Um erro ocorreu na inserção."}, 500

        return topico.json(), 201 # indica criação


    def delete(self, iddisciplina, id):
        # connection = sqlite3.connect('dado.db')
        # cursor = connection.cursor()

        # query = "DELETE FROM {tabela} WHERE nome=?".format(tabela=self.NOME_TABELA)
        # cursor.execute(query, (nome,))

        # connection.commit()
        # connection.close()
        topico = TopicoModel.buscar_por_nome(id)

        if topico:
            topico.remove()

        return {'mensagem': 'Tópico removido'}

    # @jwt_required()
    def put(self, iddisciplina, id):
        dado = Topico.parser.parse_args()
        topico = TopicoModel.buscar_por_nome(id)
        if topico is None:
            topico = TopicoModel(id, **dado)
        else:
            topico.id_disciplina = dado['id_disciplina']
        topico.insere()
        return topico.json()


class TopicoList(Resource):

    def get(self):
        return {'topicos': [topico.json() for topico in TopicoModel.query.all()]}
