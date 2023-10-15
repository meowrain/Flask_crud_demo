from flask import Flask
from .views import library_system
import pymysql


def create_app():
    app = Flask(__name__)
    app.secret_key = 'dsfasfsdfdafsf'
    app.register_blueprint(library_system.lib_sys)
    return app