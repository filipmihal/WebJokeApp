"""base views for Web Joke App"""
from app import APP
from flask import render_template
from app.helpers import joke_of_the_day
import time
@APP.route('/')
def index():
    """Homepage"""
    today = time.strftime("%Y-%m-%d")
    current_joke = joke_of_the_day.current_joke(today)
    return render_template('main/index.html',
                           head_name="Vitajte!", joke_of_the_day=current_joke)
