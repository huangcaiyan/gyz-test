from selenium import webdriver
import time
import unittest
from base.enter_comp_page import EnterCompPage
from config import *


class EnterCompSpec(unittest.TestCase):
    """
    编辑帐套信息
    """

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)

    def test_enter_comp(self):
        """ 进入公司测试"""
        enterCompPage = EnterCompPage(BASE_URL, self.driver)
        enterCompPage.enter_comp(ENTER_COMP_INFO)
        c_comp_name = enterCompPage.get_comp_name(COMP_NAME)
        self.assertEqual(c_comp_name, COMP_NAME)


if __name__ == '_main_':
    unittest.main()
