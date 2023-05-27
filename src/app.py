from flask import Flask
from src.config import load_settings as ls
from dotenv import load_dotenv

load_dotenv()


def create_app():

	app = Flask(__name__)
	ls.init_app(app=app)

	return app