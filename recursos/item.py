import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from modelos.item import TopicoModel

class Item(Resource):
    NOME_TABELA = 'topicos'

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
    
    # @jwt_required()
    def get(self, iddisciplina, id):
        item = TopicoModel.buscar_por_id(id)
        if item:
            return item.json()
        return {'mensagem': 'Tópico não encontrado'}, 404

    # @jwt_required()
    def post(self, iddisciplina, id):
        # if TopicoModel.buscar_por_nome(id):
        #     return {'mensagem': "Topico como nome {} já existe.".format(id)}

        dado = Item.parser.parse_args()
        # print(dado)
        item = TopicoModel(id, dado)

        try:
            item.insere()
        except :
            return {'mensagem': "Um erro ocorreu na inserção."}, 500

        return item.json(), 201 # indica criação 

    # @jwt_required()
    def delete(self, id):
        # connection = sqlite3.connect('dado.db')
        # cursor = connection.cursor()

        # query = "DELETE FROM {tabela} WHERE nome=?".format(tabela=self.NOME_TABELA)
        # cursor.execute(query, (nome,))

        # connection.commit()
        # connection.close()
        item = TopicoModel.buscar_por_nome(id)

        if item:
            item.remove()

        return {'mensagem': 'Tópico removido'}

    # @jwt_required()
    def put(self, id):
        dado = Item.parser.parse_args()
        item = TopicoModel.buscar_por_nome(id)
        if item is None:
            item = TopicoModel(id, **dado)
        # else:
        #     item.preco = dado['preco']
        item.insere()
        return item.json()

class ItemList(Resource):

    def get(self):
        return {'topicos': [item.json() for item in TopicoModel.query.all()]}
