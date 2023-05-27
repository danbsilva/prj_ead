import random

from flask import render_template, jsonify, request
from sqlalchemy.exc import *

from src.models import Aluno

from src.blueprints.helpers.helpers import *
from src.blueprints.alunos.schemas import AlunoGetSchema, AlunoPostSchema

get_aluno_schema = AlunoGetSchema()
post_aluno_schema = AlunoPostSchema()


@get_all(Aluno, AlunoGetSchema)
def get_alunos(objs):
    return objs


@get_one(Aluno, AlunoGetSchema)
def get_aluno(obj, uuid):
    return obj


@create(Aluno, request)
def create_aluno(obj):
    try:
        obj.ra = random.randrange(100000, 999999, 1)
        db.session.add(obj)
        db.session.commit()
        obj = get_aluno_schema.dump(obj)

        return obj
    except Exception as e:
        return {"message": e._message()}, 400


@update(Aluno, AlunoGetSchema, request)
def update_aluno(obj, uuid):
    try:
        db.session.add(obj)
        db.session.commit()

        obj = get_aluno_schema.dump(obj)

        return obj
    except Exception as e:
        return {"message": e._message()}, 400

@delete(Aluno)
def delete_aluno(obj, uuid):

    db.session.delete(obj)
    db.session.commit()
    return {"message": "Aluno deleted"}, 200
