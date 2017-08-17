"""wiew for showing all categories with their jokes """
from flask import Blueprint, redirect, render_template
from flask_paginate import Pagination

from app.models import Category
from config import PAGINATION_FRAMEWORK, PER_PAGE

CATEGORIES_MOD = Blueprint('categories', __name__)
@CATEGORIES_MOD.route('/')
def index():
    """index page where are showen all categories"""
    categories = Category.query.all()
    return render_template('categories/index.html',
                           categories=categories, head_name='Kategórie vtipov')
@CATEGORIES_MOD.route('/<name>', defaults={'page': 1})
@CATEGORIES_MOD.route('/<name>/', defaults={'page': 1})
@CATEGORIES_MOD.route('/<name>/page/<page>')
@CATEGORIES_MOD.route('/<name>/page/<page>/')

def category(name, page=1):
    """specific category page with all its jokes"""
    current_category = Category.query.filter_by(name=name).first()
    if current_category is None:
        return redirect('/kategorie')
    try:
        page = int(page)
    except ValueError:
        return redirect('kategorie/' + name)
    jokes = current_category.jokes.order_by('rank desc').limit(PER_PAGE).offset((page - 1) * PER_PAGE).all()
    total = current_category.jokes.count()
    pagination = Pagination(page=page,
                            css_framework=PAGINATION_FRAMEWORK,
                            PER_PAGE=PER_PAGE,
                            total=total,
                            format_total=True,
                            format_number=True,
                           )
    return render_template('categories/category.html',
                           category=current_category,
                           jokes=jokes,
                           pagination=pagination,
                           head_name=current_category.name
                          )
