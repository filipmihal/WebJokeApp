"""DB model"""
from app import DB



joke_reaction = DB.Table('joke_reaction',
                         DB.Column('joke_id', DB.Integer, DB.ForeignKey('joke.id')),
                         DB.Column('reaction_id', DB.Integer, DB.ForeignKey('reaction.id')),
                         DB.Column('ip_address', DB.String(128), unique=True)
                        )

class Category(DB.Model):
    """Joke category model """
    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(128), index=True, unique=True)
    average_rank = DB.Column(DB.Float)
    jokes = DB.relationship('Joke', backref='category', lazy='dynamic')

    def __repr__(self):
        """info about category"""
        return '<Category %r>' % (self.name)

class Joke(DB.Model):
    """Joke model"""
    id = DB.Column(DB.Integer, primary_key=True)
    joke = DB.Column(DB.Text, index=True)
    joke_length = DB.Column(DB.Integer)
    rank = DB.Column(DB.Float, index=True)
    category_id = DB.Column(DB.Integer, DB.ForeignKey('category.id'))
    reactions = DB.relationship('Reaction',
                                secondary=joke_reaction,
                                backref='reaction',
                                lazy='dynamic')

    def __repr__(self):
        """info about joke"""
        return '<Joke %r>' % (self.id)

    def html_joke(self):
        """from (string) joke --> to (array) joke divided by enters"""
        return self.joke.split('\n')

    def have_reaction(self, current_ip):
        """check if client has already reacted current joke"""
        return self.reactions.filter(joke_reaction.c.ip_address == current_ip).first()

    def reaction(self, current_ip, current_reaction_id):
        if not self.have_reaction(current_ip):
            #self.reactions.append(user)
            return self

class Reaction(DB.Model):
    """joke reaction"""
    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(128), unique=True)
    image_src = DB.Column(DB.String(128), unique=True)
    rate = DB.Column(DB.Integer, unique=True)
    jokes = DB.relationship('Joke',
                                secondary=joke_reaction,
                                backref='reaction',
                                lazy='dynamic')

    def __repr__(self):
        """info about joke reaction"""
        return '<Joke %r>' % (self.id)
