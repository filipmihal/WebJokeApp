from flask import render_template, flash, redirect, url_for, Blueprint
from flask_paginate import Pagination, get_page_parameter, get_page_args
from ..models import Category
# from .models import Category

mod = Blueprint('categories', __name__)

@mod.route('/')
def index():
    categories = Category.query.all()
    return render_template('categories/index.html',
        categories=categories, head_name = 'Kategórie vtipov')

@mod.route('/<name>')
def category(name):
    category = Category.query.filter_by(name=name).first()
    #ak som nenasiel ziadnu kategoriu
    if category == None:
        return redirect('/kategorie')
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    per_page = 10
    
    jokes = category.jokes.order_by('rank desc').limit(per_page).offset((page - 1) * per_page).all()
    total = category.jokes.count()
    pagination = Pagination(page=page,
                                css_framework='foundation',
                                per_page=per_page,
                                total=total,
                                record_name='users',
                                format_total=True,
                                format_number=True,
                                )
    return render_template('categories/category.html',
                           category=category, jokes = jokes, pagination=pagination)

