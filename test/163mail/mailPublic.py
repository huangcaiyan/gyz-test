# -*- encoding=utf-8 -*-
from selenium import webdriver

class Login():
    # driver = webdriver.Chrome()  

    def user_login(self,driver):
        emailInput = driver.find_element_by_css_selector('input[type=\"text\"]')
        emailInput.clear()
        emailInput.send_keys('13683139989')
        pwdInput = driver.find_element_by_css_selector('input[type=\"password\"]')
        pwdInput.clear()
        pwdInput.send_keys('Hcy045520')
        loginBtn = driver.find_element_by_id('dologin')
        loginBtn.click()

    def user_logout(self,driver):
        logoutBtn = driver.find_element_by_link_text('退出')
        logoutBtn.click()
        driver.quit()