from flask import Blueprint
from src.blueprints.alunos.routes import *
from src.blueprints.security.sercurity import auth

bp_alunos = Blueprint('alunos', __name__, static_folder='static',template_folder='templates' ,url_prefix='/alunos')

# Get Alunos
bp_alunos.add_url_rule('/', endpoint='get_alunos', view_func=get_alunos, methods=['GET'])

# Get Aluno
bp_alunos.add_url_rule('/<uuid>/', endpoint='get_aluno', view_func=get_aluno, methods=['GET'])

# Create Aluno
bp_alunos.add_url_rule('/', endpoint='create_aluno', view_func=create_aluno, methods=['POST'])

# Update Aluno
bp_alunos.add_url_rule('/<uuid>/', endpoint='update_aluno', view_func=update_aluno, methods=['PATCH'])

# Delete Aluno
bp_alunos.add_url_rule('/<uuid>/', endpoint='delete_aluno', view_func=delete_aluno, methods=['DELETE'])


def init_app(app):

    app.register_blueprint(blueprint=bp_alunos)

