from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()


def init_app(app):
    db.init_app(app=app)
    Migrate(app=app, db=db)


def create_all(app):
    with app.app_context():
        db.create_all()