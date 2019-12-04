from flask import Flask
from flask_restful import Api
from flask_jwt import JWT, jwt_required

from recursos.relacionamento import Relacionamento, RelacionamentoList
from security import authenticate, identity
from recursos.user import UserRegister
from recursos.topico import Topico, TopicoList
from recursos.disciplina import Disciplina, DisciplinaList
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../dado.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'segredo'
api = Api(app)
db.init_app(app)

@app.before_first_request
def criar_banco():
    db.create_all()

#cria o endpoint /auth por onde são enviados
#usuario e senha
jwt = JWT(app, authenticate, identity)

api.add_resource(Topico, '/topico/<string:iddisciplina>/<string:id>')
api.add_resource(Relacionamento, '/disciplina/<string:iddisciplina1>/<string:idtopico1>/<string:iddisciplina2>/<string:idtopico2>/')
api.add_resource(RelacionamentoList, '/relacionamentos')
api.add_resource(TopicoList, '/topicos')
api.add_resource(UserRegister, '/register')
api.add_resource(DisciplinaList, '/disciplinas')
api.add_resource(Disciplina, '/disciplina/<string:id>')

