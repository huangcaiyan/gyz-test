# -*- encoding=utf-8 -*-
from selenium import webdriver

driver = webdriver.Chrome()

# login
def login():
    # driver = webdriver.Chrome()
    idInput = driver.find_element_by_id('idInput')
    idInput.clear()
    idInput.send_keys('username')
    pwdInput = driver.find_element_by_id('pwdInput')
    pwdInput.clear()
    pwdInput.send_keys('password')
    loginBtn = driver.find_element_by_id('loginBtn')
    loginBtn.click()

def logout():
    #  driver = webdriver.Chrome()
     logoutBtn = driver.find_element_by_link_text('退出')
     logoutBtn.click()
     driver.quit()

driver.implicitly_wait(10)
driver.get('http://www.126.com')
login()

logout()

    