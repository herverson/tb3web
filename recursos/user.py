import sqlite3
from flask_restful import Resource, reqparse
from modelos.user import UserModel

NOME_TABELA = 'usuarios'

class UserRegister(Resource):
    NOME_TABELA = 'usuarios'

    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="Campo obrigatório."
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="Campo obrigatório."
                        )

    def post(self):
        dado = UserRegister.parser.parse_args()

        if UserModel.encontrar_por_nome(dado['username']):
            return {"mensagem": "Usuário existente."}, 400
        
        usuario = UserModel(**dado)
        usuario.insere()

        # connection = sqlite3.connect('dado.db')
        # cursor = connection.cursor()

        # query = "INSERT INTO {tabela} VALUES (NULL, ?, ?)".format(tabela=NOME_TABELA)
        # cursor.execute(query, (dado['username'], dado['password']))

        # connection.commit()
        # connection.close()

        return {"mensagem": "Usuário criado com sucesso"}, 

