"""DB model"""
import enum
import datetime
from sqlalchemy import and_
from sqlalchemy.types import TIMESTAMP, Enum

from app import DB


class ReactionsType(enum.Enum):
    """Reactions"""
    unamused = 1
    neutral = 2
    smile = 3
    funny = 4

joke_reaction = DB.Table('joke_reaction',
                         DB.Column('joke_id', DB.Integer, DB.ForeignKey('joke.id')),
                         DB.Column('reaction_type', Enum(ReactionsType)),
                         DB.Column('created_at', TIMESTAMP, default=datetime.datetime.utcnow)
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

    def __repr__(self):
        """info about joke"""
        return '<Joke %r>' % (self.id)

    def html_joke(self):
        """from (string) joke --> to (array) joke divided by enters"""
        return self.joke.split('\n')

    def unamused_reactions_num(self):
        reactions = DB.session.query(joke_reaction).filter(and_(joke_reaction.c.joke_id==self.id,
                                                                    joke_reaction.c.reaction_type == ReactionsType.unamused
                                                                   )).count()
        return reactions
    
    def neutral_reactions_num(self):
        reactions = DB.session.query(joke_reaction).filter(and_(joke_reaction.c.joke_id==self.id,
                                                                    joke_reaction.c.reaction_type == ReactionsType.neutral
                                                                   )).count()
        return reactions

    def smile_reactions_num(self):
        reactions = DB.session.query(joke_reaction).filter(and_(joke_reaction.c.joke_id==self.id,
                                                                    joke_reaction.c.reaction_type == ReactionsType.smile
                                                                   )).count()
        return reactions
    def funny_reactions_num(self):
        reactions = DB.session.query(joke_reaction).filter(and_(joke_reaction.c.joke_id==self.id,
                                                                    joke_reaction.c.reaction_type == ReactionsType.funny
                                                                   )).count()
        return reactions

    def all_reactions(self):
        reactions = DB.session.query(joke_reaction).filter(
                                                            joke_reaction.c.joke_id==self.id
                                                          ).count()
        return reactions
    def add_reaction(self, reaction_enum):
        """method called after a user made reaction"""
        new_reaction = joke_reaction.insert().values(joke_id=self.id, reaction_type=reaction_enum)
        DB.engine.execute(new_reaction)
        #DB.engine.execute()
        return True
