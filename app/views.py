from flask import render_template, flash, redirect, url_for
from app import app
from .forms import LoginForm
from .models import Category
from .models import Joke

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)

# @app.route('/kategorie/', defaults={'name': None})
@app.route('/kategorie/<name>')
def category(name):
    category = Category.query.filter_by(name=name).first()
    #ak som nenasiel ziadnu kategoriu
    if category == None:
        categories = Category.query.all()
        return render_template('categories.html',
            categories=categories)
    jokes = []
    for joke in category.jokes:
        new_joke = []
        new_joke.append(joke.joke.split('\n'))
        new_joke.append(joke.joke_length)
        new_joke.append(joke.rank)
        jokes.append(new_joke)

    return render_template('category.html',
                           category=category, jokes = jokes)

