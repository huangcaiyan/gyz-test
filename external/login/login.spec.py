# -*- encoding=utf-8 -*-
from selenium import webdriver
from public import Login
import time

class LoginTest():
    
    def __init__(self):
        self.login = Login()
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get('https://firms.guanplus.com/login')

    def test_admin_login(self):
        username = '13683139989'
        password = 'qq123456'
        # login = Login()            
        self.login.user_login(self.driver,username,password)
        # self.driver.quit()        
    
    def test_assistant_login(self):
        username = '18612198503'
        password = 'qq123456'
        # login = Login()                    
        self.login.user_login(self.driver,username,password)
        self.driver.quit()
    
    def test_user_logout(self):
        self.login.user_logout()
        self.driver.quit()
    


LoginTest().test_admin_login()
LoginTest().test_user_logout()




    