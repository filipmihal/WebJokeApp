""" view for showing all jokes and unique jokes """
from flask import Blueprint, redirect, render_template
from flask_paginate import Pagination

from app.models import Joke
from config import PAGINATION_FRAMEWORK, PER_PAGE

JOKES_MOD = Blueprint('jokes', __name__)

@JOKES_MOD.route('/', defaults={'page': 1})
@JOKES_MOD.route('/page/<page>')
@JOKES_MOD.route('/page/<page>/')
def index(page):
    """index page where all jokes are showed ordered by rank """
    try:
        page = int(page)
    except ValueError:
        return redirect('/')
    jokes = Joke.query.order_by('rank desc').limit(PER_PAGE).offset((page - 1) * PER_PAGE).all()
    total = Joke.query.count()
    pagination = Pagination(page=page,
                            css_framework=PAGINATION_FRAMEWORK,
                            PER_PAGE=PER_PAGE,
                            total=total,
                            format_total=True,
                            format_number=True,
                           )
    return render_template('jokes/index.html',
                           jokes=jokes, pagination=pagination)

@JOKES_MOD.route('/<joke_id>')
def joke(joke_id):
    """view for one specific joke"""
    current_joke = Joke.query.filter_by(id=joke_id).first()
    return render_template('jokes/joke.html',
                           joke=current_joke)
