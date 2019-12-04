from db import db


class TopicoModel(db.Model):
    __tablename__ = 'topico'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80))
    id_disciplina = db.Column(db.Integer, db.ForeignKey('disciplina.id'))

    disciplina = db.relationship('DisciplinaModel')

    def __init__(self, nome, id_disciplina):
        self.nome = nome
        self.id_disciplina = id_disciplina

    def json(self):
        return {'nome': self.nome, 'id_disciplina': self.id_disciplina}

    @classmethod
    def buscar_por_nome(cls, nome):
        return cls.query.filter_by(nome=nome).first()

    @classmethod
    def buscar_por_id(cls, id):
        return cls.query.filter_by(id=id).first()
        # connection = sqlite3.connect('dado.db')
        # cursor = connection.cursor()

        # query = "SELECT * FROM {tabela} WHERE nome=?".format(tabela=cls.NOME_TABELA)
        # resultado = cursor.execute(query, (nome,))
        # linha = resultado.fetchone()
        # connection.close()

        # if linha:
        #     return cls(*linha)

    def insere(self):
        db.session.add(self)
        db.session.commit()
        # connection = sqlite3.connect('dado.db')
        # cursor = connection.cursor()

        # query = "INSERT INTO {tabela} VALUES(?, ?)".format(tabela=self.NOME_TABELA)
        # cursor.execute(query, (self.nome, self.preco))

        # connection.commit()
        # connection.close()

    def remove(self):
        db.session.delete(self)
        db.session.commit()
