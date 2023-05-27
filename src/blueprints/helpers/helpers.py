from datetime import datetime
from functools import wraps
import uuid, os

from src.extensions.sqlalchemy import db


def get_all(Model, Schema):
    def wrapper(func):
        @wraps(func)
        def decorated(*args, **kwargs):
            schema = Schema()
            objs = Model.query.all()
            objs = schema.dump(objs, many=True)
            return func(objs, *args, **kwargs)
        return decorated
    return wrapper


def get_one(Model, Schema):
    def wrapper(func):
        @wraps(func)
        def decorated(*args, **kwargs):
            schema = Schema()
            obj = Model.query.filter_by(uuid=kwargs['uuid']).first()
            obj = schema.dump(obj)
            return func(obj, *args, **kwargs)
        return decorated
    return wrapper


def create(Model, request):
    def wrapper(func):
        @wraps(func)
        def decorated(*args, **kwargs):
            obj = Model(**request.json)

            obj.uuid = uuid.uuid4().hex
            obj.created_at = datetime.now()
            obj.updated_at = datetime.now()

            return func(obj, *args, **kwargs)
        return decorated
    return wrapper


def update(Model, Schema, request):
    def wrapper(func):
        @wraps(func)
        def decorated(*args, **kwargs):
            schema = Schema()
            obj = Model.query.filter_by(uuid=kwargs['uuid']).first()
            if not obj: return {"message": f"{Model.__name__} not exists"}, 400
            fields_to_update = request.json

            for k, v in fields_to_update.items():
                if v is not None:
                    setattr(obj, k, v)

            obj.updated_at = datetime.now()
            return func(obj, *args, **kwargs)
        return decorated
    return wrapper


def delete(Model):
    def wrapper(func):
        @wraps(func)
        def decorated(*args, **kwargs):

            obj = Model.query.filter_by(uuid=kwargs['uuid']).first()

            if not obj: return {"message": f"{Model.__name__} not exists"}, 400

            return func(obj, *args, **kwargs)
        return decorated
    return wrapper


