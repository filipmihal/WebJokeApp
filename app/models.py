from app import db


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True, unique=True)
    average_rank = db.Column(db.Float)
    jokes = db.relationship('Joke', backref='category', lazy='dynamic')

    def __repr__(self):
        return '<Category %r>' % (self.name)
       


class Joke(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    joke = db.Column(db.Text, index=True)
    joke_length = db.Column(db.Integer)
    rank = db.Column(db.Float, index=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    def __repr__(self):
        return '<Joke %r>' % (self.id)

    def html_joke(self):
       return self.joke.split('\n')
