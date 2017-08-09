from selenium import webdriver
import time
import unittest
from test_case.setting.page.setting_page import SettingPage
from base.enter_comp_page import EnterCompPage
from config import *
class CompBillingSpec(unittest.TestCase):
    """
    编辑帐套信息
    """

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)

    def test_enter_comp(self):
        enterCompPage = EnterCompPage(BASE_URL,self.driver)

        
if __name__=='_main_':
    unittest.main()
