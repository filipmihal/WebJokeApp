from flask import render_template, flash, redirect, url_for, Blueprint
from flask_paginate import Pagination, get_page_parameter, get_page_args
from ..models import Joke
# from .models import Category

mod = Blueprint('jokes', __name__)

@mod.route('/')
def index():
    page, per_page, offset = get_page_args(page_parameter='page',
        per_page_parameter='per_page')
    per_page = 10
    jokes = Joke.query.order_by('rank desc').limit(per_page).offset((page - 1) * per_page).all()
    total = Joke.query.count()
    pagination = Pagination(page=page,
                                css_framework='foundation',
                                per_page=per_page,
                                total=total,
                                record_name='jokes',
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



