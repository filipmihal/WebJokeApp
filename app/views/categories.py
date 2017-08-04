from flask import render_template, flash, redirect, url_for, Blueprint
from flask_paginate import Pagination, get_page_parameter, get_page_args
from app.models import Category
from config import per_page, pagination_framework
# from .models import Category

mod = Blueprint('categories', __name__)

@mod.route('/')
def index():
    categories = Category.query.all()
    return render_template('categories/index.html',
        categories=categories, head_name = 'Kategórie vtipov')

@mod.route('/<name>', defaults={'page': 1})
@mod.route('/<name>/', defaults={'page': 1})
@mod.route('/<name>/page/<page>')
@mod.route('/<name>/page/<page>/')
def category(name, page = 1):
    category = Category.query.filter_by(name=name).first()

    if category is None:
        return redirect('/kategorie')

    try:
        page = int(page)
    except ValueError:
        return redirect('kategorie/' + name)
    
    jokes = category.jokes.order_by('rank desc').limit(per_page).offset((page - 1) * per_page).all()
    total = category.jokes.count()
    pagination = Pagination(page=page,
        css_framework= pagination_framework,
        per_page=per_page,
        total=total,
        format_total=True,
        format_number=True,
    )
    return render_template('categories/category.html',
                           category=category, jokes = jokes, pagination=pagination, head_name = category.name)

