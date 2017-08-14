"""configuration file for Joke app"""
import os

import app
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


SECURITY_POST_LOGIN = '/profile'
SECURITY_REGISTERABLE = True
SECURITY_PASSWORD_HASH = 'bcrypt'
SECURITY_PASSWORD_SALT = os.environ.get("PASSWORD_SALT")

MAIL_SERVER = 'smtp.mailgun.org'
MAIL_PORT = 465
MAIL_USE_SSL = False
MAIL_USE_TSL = True
MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
MAIL_DEFAULT_SENDER = 'MAIL FROM: <jakub.promedia@gmail.com>'
MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

BASEDIR = os.path.abspath(os.path.dirname(__file__))
APP_ROOT_FOLDER = os.path.abspath(os.path.dirname(app.__file__))

CSRF_ENABLED = True
SECRET_KEY = os.environ.get("SECRET_KEY")

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(BASEDIR, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False

PER_PAGE = 10
PAGINATION_FRAMEWORK = 'foundation'

SOCIAL_FACEBOOK = {
    'consumer_key': os.environ.get("FB_KEY"),
    'consumer_secret': os.environ.get("FB_SECRET")
}

SOCIAL_TWITTER = {
    'consumer_key': os.environ.get("TWT_KEY"),
    'consumer_secret': os.environ.get("TWT_SECRET")
}

SOCIAL_GOOGLE = {
    'consumer_key': os.environ.get("GGL_KEY"),
    'consumer_secret': os.environ.get("GGL_SECRET")
}

