from selenium import webdriver
import unittest
import time
import sys
import os
from .login_page import LoginPage
from base.alert_page import AlertPage
from base.danger_page import DangerPage


class LoginSpec(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)  
        self.base_url = "https://firms.guanplus.com"

    def test_login(self):
        """登陆管有帐"""
        loginpage = LoginPage(self.base_url, self.driver)
        loginpage.login('13683139989', 'qq123456')
        personal_name = loginpage.personal_name_show()
        self.assertEqual(personal_name, 'huangcaiyan0714')
        print('personal_name is ', personal_name)

    def test_login1(self):
        """ 用户不存在 """
        loginpage = LoginPage(self.base_url, self.driver)
        loginpage.login('13683139980', 'qq123456')

        alertpage = AlertPage(self.driver)
        alert_msg = alertpage.get_alert_msg()
        # print('test_login2 alert_msg =>',alert_msg)
        self.assertEqual(alert_msg, '此用户不存在')

    def test_login2(self):
        """ 密码不正确 """
        loginpage = LoginPage(self.base_url, self.driver)
        loginpage.login('13683139989', 'qq1234567')

        alertpage = AlertPage(self.driver)
        alert_msg = alertpage.get_alert_msg()
        self.assertEqual(alert_msg, '密码不正确')

    def test_login3(self):
        """ 用户名为空 """
        loginpage = LoginPage(self.base_url, self.driver)
        loginpage.login('', 'qq123456')

        dangerpage = DangerPage(self.driver)
        danger_msg = dangerpage.get_danger_msg()
        self.assertEqual(danger_msg, '请填写手机')

    def test_login4(self):
        """ 密码为空 """
        loginpage = LoginPage(self.base_url, self.driver)
        loginpage.login('13683139989', '')

        dangerpage = DangerPage(self.driver)
        danger_msg = dangerpage.get_danger_msg()
        self.assertEqual(danger_msg, '请填写密码')

    def test_login5(self):
        """ 手机格式不正确 """
        loginpage = LoginPage(self.base_url, self.driver)
        loginpage.login('136', '')

        dangerpage = DangerPage(self.driver)
        danger_msg = dangerpage.get_danger_msg()
        self.assertEqual(danger_msg, '手机格式不正确')

    def tearDown(self):
        self.driver.quit()
        self.driver.find_element_by_xpath


if __name__ == "__main__":
    unittest.main()
