"""base views for Web Joke App"""
import time
from flask_security import login_required
from flask import render_template

from app import APP
from app.helpers import joke_of_the_day


@APP.route('/')
def index():
    """Homepage"""
    today = time.strftime("%Y-%m-%d")
    day_name = time.strftime("%w")
    day_num = time.strftime("%d")
    month = time.strftime("%m")
    current_joke = joke_of_the_day.current_joke(today)
    ui_date = joke_of_the_day.UiDate(day_name, day_num, month)
    return render_template('main/index.html',
                           head_name="Vitajte!", joke_of_the_day=current_joke, ui_date=ui_date)


@APP.route('/moj-profil')
@login_required
def profile():
    """profile page"""
    return render_template('main/profile.html',
                           head_name="Vitajte!")
