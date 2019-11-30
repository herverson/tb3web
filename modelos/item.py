from db import db

class ItemModel(db.Model):
    __tablename__ = 'item'

    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(80))
    preco = db.Column(db.Float(precision = 2))
    id_loja = db.Column(db.Integer, db.ForeignKey('loja.id'))

    loja = db.relationship('LojaModel')

    def __init__(self, nome, preco, id_loja):
        self.nome = nome
        self.preco = preco
        self.id_loja = id_loja

    def json(self):
        return {'nome': self.nome, 'preco': self.preco, 'id_loja': self.id_loja}

    @classmethod
    def buscar_por_nome(cls, nome):
        return cls.query.filter_by(nome = nome).first()
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