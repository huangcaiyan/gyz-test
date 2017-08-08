from selenium import webdriver
import unittest
import time
from test_case.login.login_page import LoginPage 



class ScrollSpec(unittest.TestCase):

    def setUp(self,driver):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)

    def scroll_top():
        js = 'var q = document.body.scrollTop=0'
        return self.driver.execu

    def scroll_foot():
        js = 'var q = document.body.scrollTop=10000'

    
