"""unit tests for Web Joke App"""
import os
import unittest
from datetime import datetime, timedelta

from app import APP
from app import DB
from app.helpers.joke_of_the_day import current_joke
from app.models import Joke, Category, ReactionsType
from config import BASEDIR

TEST_DB = 'test.db'

def insert_jokes_categories():
        """insert some categories and jokes to test.db"""
        db_testing_categories = [
            Category(name="first category", average_rank = 1),
            Category(name="second category", average_rank = 2),
            Category(name="third category", average_rank = 3),
            Category(name="forth category", average_rank = 3.5),
            Category(name="fifth category", average_rank = 2.55)
        ]
        db_testing_jokes = [
            Joke(joke="lorem ipsum", joke_length= 11, rank=2, category_id=1),
            Joke(joke="lorem ipsum fhjf", joke_length= 11, rank=2.5, category_id=1),
            Joke(joke="lorem ipsumdddd aa", joke_length= 11, rank=3.4, category_id=4),
            Joke(joke="lorem ipsumawhadj ", joke_length= 11, rank=4, category_id=2),
            Joke(joke="lorem ipsum adds", joke_length= 11, rank=4, category_id=4),
            Joke(joke="lorem ipsum qwer", joke_length= 11, rank=2.55, category_id=2)
        ]
        DB.session.add_all(db_testing_categories)
        DB.session.add_all(db_testing_jokes)
        DB.session.commit()

def insert_joke_reactions(testing_joke):
    """insert joke reactions"""
    testing_joke.add_reaction(ReactionsType.funny)
    testing_joke.add_reaction(ReactionsType.smile)
    testing_joke.add_reaction(ReactionsType.unamused)
    testing_joke.add_reaction(ReactionsType.unamused)
    testing_joke.add_reaction(ReactionsType.funny)
    testing_joke.add_reaction(ReactionsType.funny)

class BasicTests(unittest.TestCase):
    """unit tests class"""      

    def setUp(self):
        """setting up all variables"""
        APP.config['TESTING'] = True
        APP.config['WTF_CSRF_ENABLED'] = False
        APP.config['DEBUG'] = False
        APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
            os.path.join(BASEDIR, TEST_DB)
        self.app = APP.test_client()
        DB.drop_all()
        DB.create_all()
        insert_jokes_categories()

    def tearDown(self):
        """run after test scripts"""
        pass

    def test_joke_of_the_day(self):
        """test joke of the day if there is everyday a new joke"""
        str_date = datetime.now().strftime("%Y-%m-%d")
        jokes_ids = []
        jokes_count = Joke.query.count()

        if jokes_count == 0:
            raise Exception('There are no jokes in database')

        for i in range(jokes_count):
            modified_date = datetime.strptime(str_date, "%Y-%m-%d")
            new_date = modified_date + timedelta(days=i)
            new_date = new_date.strftime("%Y-%m-%d")
            joke = current_joke(new_date)

            if joke.id in jokes_ids:
                assert False
            jokes_ids.append(joke.id)

    def test_sorting_method(self):
        """test sorting method in models"""
        testing_joke = Joke.query.get(1)
        insert_joke_reactions(testing_joke)
        testing_order = testing_joke.order_reactions()
        assert testing_order == [("funny", 3), ("unamused", 2), ("smile", 1)]

if __name__ == "__main__":
    unittest.main()
