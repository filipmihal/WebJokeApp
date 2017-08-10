"""DB model"""
import enum
import datetime
from operator import itemgetter
from sqlalchemy import and_
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
    created_at = DB.Column(Enum(ReactionsType))

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

    def reactions_num(self, current_enum):
        """number of specific reaction"""
        reactions = self.reactions.filter(JokeReaction.reaction_type == current_enum).count()
        return reactions

    def all_reactions(self):
        """number of all reactions for specifi joke"""
        reactions = self.reactions.count()
        return reactions

    def order_reactions(self):
        """order reactions"""
        unamused_num = self.reactions_num(ReactionsType.unamused)
        neutral_num = self.reactions_num(ReactionsType.neutral)
        smile_num = self.reactions_num(ReactionsType.smile)
        funny_num = self.reactions_num(ReactionsType.funny)
        reactions_data = []
        if unamused_num != 0:
            reactions_data.append(("unamused", unamused_num))
        if neutral_num != 0:
            reactions_data.append(("neutral", neutral_num))
        if smile_num != 0:
            reactions_data.append(("smile", smile_num))
        if funny_num != 0:
            reactions_data.append(("funny", funny_num))
        reactions_data = sorted(reactions_data, key=itemgetter(1), reverse=True)
        return reactions_data
    def add_reaction(self, reaction_enum):
        """method called after a user made reaction"""
        new_reaction = JokeReaction(joke_id=self.id, reaction_type=reaction_enum)
        DB.session.add(new_reaction)
        DB.session.commit()
        #DB.engine.execute()
        return True
