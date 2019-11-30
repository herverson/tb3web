import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from modelos.item import ItemModel

class Item(Resource):
    NOME_TABELA = 'itens'

    parser = reqparse.RequestParser()

    parser.add_argument('preco',
                        type=float,
                        required=True,
                        help="Campo obrigatório.")

    parser.add_argument('id_loja',
                        type=int,
                        required=True,
                        help="Campo obrigatório.")
    
    # @jwt_required()
    def get(self, nome):
        item = ItemModel.buscar_por_nome(nome)
        if item:
            return item.json()
        return {'mensagem': 'Item não encontrado'}, 404

    # @jwt_required()
    def post(self, nome):
        if ItemModel.buscar_por_nome(nome):
            return {'mensagem': "Item como nome {} já existe.".format(nome)}

        dado = Item.parser.parse_args()
        item = ItemModel(nome, **dado)

        try:
            item.insere()
        except :
            return {'mensagem': "Um erro ocorreu na inserção."}, 500

        return item.json(), 201 # indica criação 

    # @jwt_required()
    def delete(self, nome):
        # connection = sqlite3.connect('dado.db')
        # cursor = connection.cursor()

        # query = "DELETE FROM {tabela} WHERE nome=?".format(tabela=self.NOME_TABELA)
        # cursor.execute(query, (nome,))

        # connection.commit()
        # connection.close()
        item = ItemModel.buscar_por_nome(nome)

        if item:
            item.remove()

        return {'mensagem': 'Item removido'}

    # @jwt_required()
    def put(self, nome):
        dado = Item.parser.parse_args()
        item = ItemModel.buscar_por_nome(nome)
        if item is None:
            item = ItemModel(nome, **dado)
        else:
            item.preco = dado['preco']
        item.insere()
        return item.json()

class ItemList(Resource):

    def get(self):
        return {'itens': [item.json() for item in ItemModel.query.all()]}
