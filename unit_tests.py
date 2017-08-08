"""unit tests for WEb Joke APP"""
import os
import unittest
from datetime import datetime, timedelta

from app import APP
from app.helpers.joke_of_the_day import current_joke
from app.models import Joke
from config import BASEDIR

TEST_DB = 'test.db'

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
    def tearDown(self):
        """run after test scripts"""
        pass

    def test_joke_of_the_day(self):
        """test joke of the day if there is everyday a new joke"""
        str_date = '2017-08-14'
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

if __name__ == "__main__":
    unittest.main()
