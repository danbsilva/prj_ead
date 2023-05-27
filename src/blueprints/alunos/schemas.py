from src.extensions.marshmallow import ma
from src.models import Aluno


class AlunoGetSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Aluno
        exclude = ('id','password',)


class AlunoPostSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Aluno
        exclude = ('id','uuid',)
