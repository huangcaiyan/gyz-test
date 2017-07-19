from selenium import webdriver
import time
from mailPublic import Login

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://mail.163.com/')

# login
login = Login()
login.user_login(driver)

time.sleep(2)

login.user_logout(driver)