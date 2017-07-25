# -*- encoding=utf-8 -*-
from selenium import webdriver
import time
class LoginPage():
    # login

    # element locate
    usernameInput = driver.find_element_by_id('usernameInput')
    passwordInput = driver.find_element_by_id('passwordInput')
    loginButton = driver.find_element_by_id('loginButton')
          
    def __init__(self,url,driver):
        self.url = url
        self.driver = driver
   
    # login
    def user_login(self,driver,username,password):
        self.driver.get(self.url)
        # username
        self.usernameInput.clear()
        self.usernameInput.sendkeys(username)

        # password
        self.passwordInput.clear()
        self.passwordInput.sendkeys(password)

        # click login button
        self.loginButton.click()
        time.sleep(10)


        

   

    