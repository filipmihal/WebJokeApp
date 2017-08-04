from selenium import webdriver
import unittest
from app.models import Category
from  sqlalchemy.sql.expression import func
import math
from random import randint
from flask import url_for
from app import app
import os
from config import per_page
class BasicTests(unittest.TestCase):
 
    ############################
    #### setup and teardown ####
    ############################
 
    # executed prior to each test
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        self.driver.set_window_size(1120, 550)
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SERVER_NAME'] = "http://localhost:5000"
        self.app = app.test_client()
 
    # executed after each test
    def tearDown(self):
        self.driver.quit()
 
###############
#### tests ####
###############
    def test_category_page(self):
        self.driver.get(app.config['SERVER_NAME'] + "/kategorie/")

        #testing the title
        title = self.driver.find_element_by_xpath('/html/body/div/div[1]/div/div/div/h1')
        assert title is not None
        assert len(title.get_attribute("innerText")) > 3

        #testing the categories
        categories = self.driver.find_elements_by_class_name('card-nav-tabs')
        assert len(categories) >= 9

    def test_category_paginator(self):
        category = Category.query.order_by(func.random()).first()
        total_jokes = category.jokes.count()
        pages = math.ceil(total_jokes / per_page)
        remainder = total_jokes % per_page
        if remainder == 0:
            remainder = per_page

        with app.app_context():
            category_url = url_for('categories.category', name=category.name, _external=False)

        current_page_num = str(randint(1,pages))
        url = app.config['SERVER_NAME'] + category_url + "page/" + current_page_num

        self.driver.get(url)
        jokes = self.driver.find_elements_by_class_name('joke')
        jokes_num = len(jokes)
        if current_page_num == pages:
            assert jokes_num == remainder
        else:
            assert jokes_num == int(per_page)

if __name__ == "__main__":
    unittest.main()
