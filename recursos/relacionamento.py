import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from modelos.relacionamento import RelacionamentoModel

class Relacionamento(Resource):
    NOME_TABELA = 'relacionamentos'

    parser = reqparse.RequestParser()
    #
    parser.add_argument('descricao',
                        type=str,
                        required=True,
                        help="Campo descricao obrigatório.")
    #
    # parser.add_argument('id_disciplina2',
    #                     type=int,
    #                     required=True,
    #                     help="Campo id_disciplina2 obrigatório.")
    #
    # @jwt_required()
    def get(self, iddisciplina1, idtopico1, iddisciplina2, idtopico2):
        item = RelacionamentoModel.buscar_relacao(iddisciplina1, idtopico1, iddisciplina2, idtopico2)
        if item:
            return item.json()
        return {'mensagem': 'Relacionamento não encontrado'}, 404

    # @jwt_required()
    def post(self, iddisciplina1, idtopico1, iddisciplina2, idtopico2):
        # if TopicoModel.buscar_por_nome(id):
        #     return {'mensagem': "Topico como nome {} já existe.".format(id)}

        dado = Relacionamento.parser.parse_args()
        item = RelacionamentoModel(iddisciplina1, idtopico1, iddisciplina2, idtopico2, **dado)

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
        item = RelacionamentoModel.buscar_por_nome(id)

        if item:
            item.remove()

        return {'mensagem': 'Relacionamento removido'}

    # @jwt_required()
    def put(self, id):
        dado = Relacionamento.parser.parse_args()
        item = RelacionamentoModel.buscar_por_nome(id)
        if item is None:
            item = RelacionamentoModel(id, **dado)
        # else:
        #     item.preco = dado['preco']
        item.insere()
        return item.json()

class RelacionamentoList(Resource):

    def get(self):
        return {'Relacionamentos': [item.json() for item in RelacionamentoModel.query.all()]}
