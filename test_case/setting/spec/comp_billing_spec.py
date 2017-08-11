from selenium import webdriver
import time
import unittest
from test_case.setting.page.setting_page import SettingPage
from base.enter_comp_page import EnterCompPage
from config import *
from base.public_page import PublicPage
from test_case.setting.page.comp_billing_page import CompBillingPage


class CompBillingSpec(unittest.TestCase):
    """
    帐套页面测试
    """
    billing_page_url = BASE_URL + '/app/setting/company-billing'

    def setUp(self):
        """ 进入公司 """
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        enterCompPage = EnterCompPage(BASE_URL, self.driver)
        enterCompPage.enter_comp(ENTER_COMP_INFO)
        c_comp_name = enterCompPage.get_comp_name(COMP_NAME)
        if c_comp_name == COMP_NAME:
            self.driver.get(self.billing_page_url)
        else:
            print('————————————进入公司失败 ！————————————')
            

    def test_edit_comp_info(self):
        """ 进入公司测试"""
        publicPage = PublicPage(self.driver)
        compBillingPage = CompBillingPage(self.driver)
        r_num = publicPage.random_num(9)
        print('random num is ',r_num)



if __name__ == '_main_':
    unittest.main()
