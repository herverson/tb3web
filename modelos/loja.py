from db import db

class LojaModel(db.Model):
    __tablename__ = 'loja'

    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(80))

    itens = db.relationship('ItemModel', lazy = 'dynamic')

    def __init__(self, nome):
        self.nome = nome
    
    def json(self):
        return {'nome': self.nome, 'itens': [item.json() for item in self.itens.all()]}

    @classmethod
    def buscar_por_nome(cls, nome):
        return cls.query.filter_by(nome=nome).first()

    def insere(self):
        db.session.add(self)
        db.session.commit()

    def remove(self):
        db.session.delete(self)
        db.session.commit()