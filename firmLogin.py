from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest
import HTMLTestRunner


class firmLoginTest(unittest.TestCase):
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://firms.xxx.com/login')

    def test_login(self):
        driver = self.driver
        username = 'xxx'
        password = 'xxxx'

        usernameElem = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_id('usernameInput'))
        passwordElem = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_id('passwordInput'))
        loginButtonElem = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_id('loginButton'))

        usernameElem.clear()
        usernameElem.send_keys(username)

        passwordElem.clear()
        passwordElem.send_keys(password)

        loginButtonElem.click()
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('loginButton'))

    def tearDown(self):
        self.driver.quit()

if __name__ == '_main_':
    HTMLTestRunner.main()
