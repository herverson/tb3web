from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from recursos.relacionamento import Relacionamento
from security import authenticate, identity
from recursos.user import UserRegister
from recursos.item import Item, ItemList
from recursos.loja import Loja, LojaList
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

api.add_resource(Item, '/item/<string:iddisciplina>/<string:id>')
api.add_resource(Relacionamento, '/disciplina/<string:iddisciplina1>/<string:idtopico1>/<string:iddisciplina2>/<string:idtopico2>/')
api.add_resource(ItemList, '/itens')
api.add_resource(UserRegister, '/register')
api.add_resource(LojaList, '/lojas')
api.add_resource(Loja, '/loja/<string:id>')
# api.add_resource(Loja, '/loja/<string:nome>')
