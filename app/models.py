"""DB model"""
import enum
from datetime import datetime
from operator import itemgetter
from sqlalchemy.types import TIMESTAMP, Enum

from app import DB


class ReactionsType(enum.Enum):
    """Reactions"""
    unamused = 1
    neutral = 2
    smile = 3
    funny = 4

class JokeReaction(DB.Model):
    """jokes reactions model"""
    __tablename__ = 'joke_reaction'
    id = DB.Column(DB.Integer, primary_key=True)
    joke_id = DB.Column(DB.Integer, DB.ForeignKey('joke.id'))
    reaction_type = DB.Column(Enum(ReactionsType))
    created_at = DB.Column(TIMESTAMP, default=datetime.utcnow, nullable=False)

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
    reactions = DB.relationship('JokeReaction', backref='joke_reaction', lazy='dynamic')

    def __repr__(self):
        """info about joke"""
        return '<Joke %r>' % (self.id)

    def html_joke(self):
        """from (string) joke --> to (array) joke divided by enters"""
        return self.joke.split('\n')

    def reactions_num(self, reaction_type):
        """number of specific reaction"""
        return self.reactions.filter(JokeReaction.reaction_type == reaction_type).count()

    def all_reactions(self):
        """number of all reactions for specifi joke"""
        return self.reactions.count()

    def order_reactions(self):
        """order reactions"""
        reactions_data = [
            ("unamused", self.reactions_num(ReactionsType.unamused)),
            ("neutral", self.reactions_num(ReactionsType.neutral)),
            ("smile", self.reactions_num(ReactionsType.smile)),
            ("funny", self.reactions_num(ReactionsType.funny))]
        reactions_data = [item for item in reactions_data if item[1] > 0]
        reactions_data = sorted(reactions_data, key=itemgetter(1), reverse=True)
        return reactions_data

    def add_reaction(self, reaction_type):
        """method called after a user made reaction"""
        new_reaction = JokeReaction(joke_id=self.id, reaction_type=reaction_type)
        DB.session.add(new_reaction)
        DB.session.commit()
