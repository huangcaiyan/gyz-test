from selenium import webdriver
import time
import unittest
from config import Config
from .fixed_assets_page import FixedAssetsPage 
from base.public_page import PublicPage 
from base.enter_comp_page import EnterCompPage 

class FixedSpec(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        enterCompPage = EnterCompPage(Config.BASE_URL,self.driver)
        enterCompPage.enter_comp(Config.ENTER_COMP_INFO_YB)
    # 
    def test_select_invoice_type(self):
        """记固定资产－选择发票类型测试"""
        self.driver.get(Config.BASE_URL + '')
        publicPage = PublicPage(self.driver)
        fixedAssertsPage = FixedAssetsPage(self.driver,'fixed')
        fixedAssertsPage.go_to_record_page()
        fixedAssertsPage.select_invoice_type('专票')
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == '_main_':
    unittest.main()
