from selenium import webdriver
import time
import unittest
from setting_page import SettingPage
from base.enter_comp_page import EnterCompPage
class CompanyBillingSpec(unittest.TestCase):
    """
    编辑帐套信息
    """

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        EnterCompPage(self.driver,)

        self.setting_page = SettingPage(self.driver,'comp_billing')
