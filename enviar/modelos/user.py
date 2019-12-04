import sqlite3
from db import db

class UserModel(db.Model):

    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(20))

    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    @classmethod
    def encontrar_por_nome(cls, nome):
        return cls.query.filter_by(username=nome).first()
        # connection = sqlite3.connect('dado.db')
        # cursor = connection.cursor()

        # query = "SELECT * FROM {tabela} WHERE nome=?".format(tabela=cls.NOME_TABELA)
        # resultado = cursor.execute(query, (nome,))
        # linha = resultado.fetchone()
        # if linha:
        #     usuario = cls(*linha)
        # else:
        #     usuario = None
        
        # connection.close()
        # return usuario
    
    @classmethod
    def encontrar_por_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
        # connection = sqlite3.connect('dado.db')
        # cursor = connection.cursor()

        # query = "SELECT * FROM {tabela} WHERE id=?".format(tabela=cls.NOME_TABELA)
        # resultado = cursor.execute(query, (_id,))
        # linha = resultado.fetchone()
        # if linha:
        #     usuario = cls(*linha)
        # else:
        #     usuario = None
        
        # connection.close()
        # return usuario

    def insere(self):
        db.session.add(self)
        db.session.commit()
