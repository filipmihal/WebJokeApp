"""init module"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
APP = Flask(__name__)
APP.config.from_object('config')
DB = SQLAlchemy(APP)
from app import models
from app.views.categories import CATEGORIES_MOD
from app.views.jokes import JOKES_MOD
APP.register_blueprint(CATEGORIES_MOD, url_prefix='/kategorie')
APP.register_blueprint(JOKES_MOD, url_prefix='/vtipy')
