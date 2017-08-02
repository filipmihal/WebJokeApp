from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import models
from app.views.categories import mod
from app.views.jokes import mod

app.register_blueprint(views.categories.mod, url_prefix='/kategorie')
app.register_blueprint(views.jokes.mod, url_prefix='/vtipy')

