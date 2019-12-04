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
        relacionamento = RelacionamentoModel.buscar_relacao(iddisciplina1, idtopico1, iddisciplina2, idtopico2)
        if relacionamento:
            return relacionamento.json()
        return {'mensagem': 'Relacionamento não encontrado'}, 404

    # @jwt_required()
    def post(self, iddisciplina1, idtopico1, iddisciplina2, idtopico2):
        # if TopicoModel.buscar_por_nome(id):
        #     return {'mensagem': "Topico como nome {} já existe.".format(id)}

        dado = Relacionamento.parser.parse_args()
        relacionamento = RelacionamentoModel(iddisciplina1, idtopico1, iddisciplina2, idtopico2, **dado)

        try:
            relacionamento.insere()
        except :
            return {'mensagem': "Um erro ocorreu na inserção."}, 500

        return relacionamento.json(), 201 # indica criação

    # @jwt_required()
    def delete(self, iddisciplina1, idtopico1, iddisciplina2, idtopico2):
        # connection = sqlite3.connect('dado.db')
        # cursor = connection.cursor()

        # query = "DELETE FROM {tabela} WHERE nome=?".format(tabela=self.NOME_TABELA)
        # cursor.execute(query, (nome,))

        # connection.commit()
        # connection.close()
        relacionamento = RelacionamentoModel.buscar_relacao(iddisciplina1, idtopico1, iddisciplina2, idtopico2)

        if relacionamento:
            relacionamento.remove()

        return {'mensagem': 'Relacionamento removido'}

    # @jwt_required()
    # dado = Topico.parser.parse_args()
    # topico = TopicoModel.buscar_por_nome(id)
    # if topico is None:
    #     topico = TopicoModel(id, **dado)
    # else:
    #     topico.id_disciplina = dado['id_disciplina']
    # topico.insere()
    # return topico.json()
    def put(self, iddisciplina1, idtopico1, iddisciplina2, idtopico2):
        dado = Relacionamento.parser.parse_args()
        relacionamento = RelacionamentoModel.buscar_relacao(iddisciplina1, idtopico1, iddisciplina2, idtopico2)
        if relacionamento is None:
            relacionamento = RelacionamentoModel(iddisciplina1, idtopico1, iddisciplina2, idtopico2)
        else:
            relacionamento.descricao = dado['descricao']
        relacionamento.insere()
        return relacionamento.json()

class RelacionamentoList(Resource):

    def get(self):
        return {'Relacionamentos': [relacionamento.json() for relacionamento in RelacionamentoModel.query.all()]}
