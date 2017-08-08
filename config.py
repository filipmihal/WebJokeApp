"""configuration file for Joke app"""
import os

import app

BASEDIR = os.path.abspath(os.path.dirname(__file__))
APP_ROOT_FOLDER = os.path.abspath(os.path.dirname(app.__file__))

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(BASEDIR, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False

PER_PAGE = 10
PAGINATION_FRAMEWORK = 'foundation'
