from db import db

class RelacionamentoModel(db.Model):
    __tablename__ = 'relacionamentos'

    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(80))
    id_topico1 = db.Column(db.Integer)
    id_disciplina1 = db.Column(db.Integer)
    id_topico2 = db.Column(db.Integer)
    id_disciplina2 = db.Column(db.Integer)

    # disciplina = db.relationship('DisciplinaModel')
    # topico = db.relationship('TopicoModel')

    def __init__(self, iddisciplina1, idtopico1, iddisciplina2, idtopico2, descricao):
        self.descricao = descricao
        self.id_topico1 = idtopico1
        self.id_disciplina1 = iddisciplina1
        self.id_topico2 = idtopico2
        self.id_disciplina2 = iddisciplina2

    def json(self):
        return {'descricao': self.descricao, 'id_topico1': self.id_topico1, 'id_topico2': self.id_topico2,
                'id_disciplina1': self.id_disciplina1, 'id_disciplina2': self.id_disciplina2}

    @classmethod
    def buscar_por_nome(cls, nome):
        return cls.query.filter_by(nome=nome).first()

    @classmethod
    def buscar_relacao(cls, id_disciplina1, idtopico1, iddisciplina2, idtopico2):
        return cls.query.filter_by(id_disciplina1=id_disciplina1, id_disciplina2=iddisciplina2, id_topico1=idtopico1, id_topico2=idtopico2).first()

    @classmethod
    def buscar_por_id(cls, id):
        return cls.query.filter_by(id=id).first()


    def insere(self):
        db.session.add(self)
        db.session.commit()

    def remove(self):
        db.session.delete(self)
        db.session.commit()
