"""base views for Web Joke App"""
import time
from flask_security import login_required
from flask import render_template
from flask_login import current_user

from app import APP
from app.helpers import joke_of_the_day
from app.models import ReactionsType


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
    funny_reactions = current_user.get_reactions(ReactionsType.funny)
    smile_reactions = current_user.get_reactions(ReactionsType.smile)
    neutral_reactions = current_user.get_reactions(ReactionsType.neutral)
    unamused_reactions = current_user.get_reactions(ReactionsType.unamused)
    return render_template('main/profile.html',
                           head_name="Vitajte!",
                           funny_reactions = funny_reactions,
                           smile_reactions = smile_reactions,
                           neutral_reactions = neutral_reactions,
                           unamused_reactions = unamused_reactions)
