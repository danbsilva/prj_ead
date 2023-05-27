from src.extensions.sqlalchemy import db


class Aluno(db.Model):

    __tablename__ = 'alunos'

    id = db.Column(db.Integer, primary_key=True, index=True)
    uuid = db.Column(db.String, unique=True, nullable=False, index=True)
    ra = db.Column(db.String, unique=True, nullable=False, index=True)
    nome = db.Column(db.String, nullable=False, index=True)
    cpf = db.Column(db.String, unique=True, nullable=False, index=True)
    email = db.Column(db.String, unique=True, nullable=False, index=True)
    password = db.Column(db.String)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

