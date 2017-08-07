"""base views for Web Joke App"""
from app import APP
from flask import render_template
@APP.route('/')
def index():
    """Homepage"""
    return render_template('main/index.html',
                           head_name="Vitajte!")
