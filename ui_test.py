""" UI tests for Web Joke App """
import unittest
import math
from random import randint
from selenium import webdriver
from app.models import Category
from app import APP
from sqlalchemy.sql.expression import func
from flask import url_for
from config import PER_PAGE
class BasicTests(unittest.TestCase):
    """class for all unit tests"""
    def setUp(self):
        """setting up all necessary variables"""
        self.driver = webdriver.PhantomJS()
        self.driver.set_window_size(1120, 550)
        APP.config['TESTING'] = True
        APP.config['WTF_CSRF_ENABLED'] = False
        APP.config['DEBUG'] = False
        APP.config['SERVER_NAME'] = "http://localhost:5000"
        self.APP = APP.test_client()
    def tearDown(self):
        """run after test"""
        self.driver.quit()
    def test_category_page(self):
        """test the title of the category page"""
        self.driver.get(APP.config['SERVER_NAME'] + "/kategorie/")
        title = self.driver.find_element_by_xpath('/html/body/div/div[1]/div/div/div/h1')
        assert title is not None
        assert len(title.get_attribute("innerText")) > 3
        categories = self.driver.find_elements_by_class_name('card-nav-tabs')
        assert len(categories) >= 9
    def test_category_paginator(self):
        """test funcionality of the paginator"""
        category = Category.query.order_by(func.random()).first()
        total_jokes = category.jokes.count()
        pages = math.ceil(total_jokes / PER_PAGE)
        remainder = total_jokes % PER_PAGE
        if remainder == 0:
            remainder = PER_PAGE
        with APP.app_context():
            category_url = url_for('categories.category', name=category.name, _external=False)
        current_page_num = str(randint(1, pages))
        url = APP.config['SERVER_NAME'] + category_url + "page/" + current_page_num
        self.driver.get(url)
        jokes = self.driver.find_elements_by_class_name('joke')
        jokes_num = len(jokes)
        if current_page_num == pages:
            assert jokes_num == remainder
        else:
            assert jokes_num == int(PER_PAGE)
if __name__ == "__main__":
    unittest.main()
