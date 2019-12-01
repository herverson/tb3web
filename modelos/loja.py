from db import db

class DisciplinaModel(db.Model):
    __tablename__ = 'disciplina'

    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(80))

    topicos = db.relationship('TopicoModel', lazy = 'dynamic')

    def __init__(self, nome):
        self.nome = nome
        self.id
    
    def json(self):
        return {'nome': self.nome, 'id': self.id, 'topicos': [topico.json() for topico in self.topicos.all()]}

    @classmethod
    def buscar_por_nome(cls, nome):
        return cls.query.filter_by(nome=nome).first()

    def buscar_por_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def insere(self):
        db.session.add(self)
        db.session.commit()

    def remove(self):
        db.session.delete(self)
        db.session.commit()