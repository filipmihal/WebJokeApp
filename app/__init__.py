"""init module"""
#from werkzeug.contrib.fixers import ProxyFix
from flask_mail import Mail
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, login_required 
APP = Flask(__name__)
APP.config.from_object('config')
DB = SQLAlchemy(APP)
from app import models
from app.views.categories import CATEGORIES_MOD
from app.views.jokes import JOKES_MOD
import app.views.main
from flask_mail import Mail
# Bootstrap
from flask_bootstrap import Bootstrap
Bootstrap(APP)
USER_DATASTORE = SQLAlchemyUserDatastore(DB, models.User, models.Role)
SECURITY = Security(APP, USER_DATASTORE)
mail = Mail(APP)
APP.register_blueprint(CATEGORIES_MOD, url_prefix='/kategorie')
APP.register_blueprint(JOKES_MOD, url_prefix='/vtipy')
