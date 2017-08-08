from selenium import webdriver
import unittest
import time
from test_case.external.comp_list_page import CompListPage
from config import *
from test_case.login.login_page import LoginPage


class CompListSpec(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)

    def test_enter_comp1(self):
        """ 进入公司 """
        loginPage = LoginPage(BASE_URL,self.driver)
        compListPage = CompListPage(self.driver)
        loginPage.login(LOGIN_DATA)
        compListPage.enter_comp(COMP_NAME) 
        current_comp_name = compListPage.get_comp_name(COMP_NAME)
        self.assertEqual(current_comp_name,COMP_NAME)
        
    def tearDown(self):
        time.sleep(3)
        self.driver.quit()
    
if __name__=='_main_':
    unittest.main()
