from flask import render_template, flash, redirect, url_for, Blueprint
from flask_paginate import Pagination, get_page_parameter, get_page_args
from app.models import Joke
from config import per_page, pagination_framework
# from .models import Category

mod = Blueprint('jokes', __name__)

@mod.route('/', defaults={'page': 1})
@mod.route('/page/<page>')
@mod.route('/page/<page>/')
def index(page):
    try:
        page = int(page)
    except ValueError:
        return redirect('kategorie/' + name)
    
    jokes = Joke.query.order_by('rank desc').limit(per_page).offset((page - 1) * per_page).all()
    total = Joke.query.count()
    pagination = Pagination(page=page,
        css_framework=pagination_framework,
        per_page=per_page,
        total=total,
        format_total=True,
        format_number=True,
    )
    return render_template('jokes/index.html',
        jokes=jokes, pagination=pagination)

@mod.route('/<id>')
def joke(id):
    joke = Joke.query.filter_by(id=id).first()
    return render_template('jokes/joke.html',
        joke=joke)



