""" view for showing all jokes and unique jokes """
from flask import Blueprint, redirect, render_template, request, json
from flask_paginate import Pagination

from app.models import Joke
from app.models import ReactionsType
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

@JOKES_MOD.route('/rate-joke', methods=['POST'])
def rate_joke():
    """add new reaction to database"""
    joke_id = request.form["joke_id"]
    reaction_id = request.form["reaction_id"]
    try:
        reaction_id = int(reaction_id)
    except:
        return False

    try:
        joke_id = int(joke_id)
    except:
        return False

    if reaction_id == 1:
        reaction = ReactionsType.unamused
    elif reaction_id == 2:
        reaction = ReactionsType.neutral
    elif reaction_id == 3:
        reaction = ReactionsType.smile
    elif reaction_id == 4:
        reaction = ReactionsType.funny
    
    current_joke = Joke.query.filter_by(id=joke_id).first()
    if not current_joke:
        return False

    new_reaction = current_joke.add_reaction(reaction)
    if not new_reaction:
         return json.dumps({'status': 'False'});
    else:
        return json.dumps({'status': 'True'});
    

