"""unit tests for WEb Joke APP"""
import os
import unittest
from app import DB
from app import APP
from config import basedir
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
            os.path.join(basedir, TEST_DB)
        self.APP = APP.test_client()
        DB.drop_all()
        DB.create_all()
    def tearDown(self):
        """run after test scripts"""
        pass
    def test_sample(self):
        """sample test"""
        assert 1 == 1
if __name__ == "__main__":
    unittest.main()
