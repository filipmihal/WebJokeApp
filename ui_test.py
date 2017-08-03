from selenium import webdriver
import unittest

class BasicTests(unittest.TestCase):
 
    ############################
    #### setup and teardown ####
    ############################
 
    # executed prior to each test
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        self.driver.set_window_size(1120, 550)
 
    # executed after each test
    def tearDown(self):
        self.driver.quit()
 
 
###############
#### tests ####
###############
    def test_category_page(self):
        self.driver.get("http://localhost:8000/kategorie/")
        title = self.driver.find_element_by_xpath('/html/body/div/div[1]/div/div/div/h1')
        assert title is not None
        assert len(title.get_attribute("innerText")) > 3
 
if __name__ == "__main__":
    unittest.main()
