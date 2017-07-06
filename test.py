# -*- coding: utf-8 -*- 
from selenium import webdriver
import time
import HTMLTestRunner

dr = webdriver.Chrome()
# dr.set_window_size(240, 320)
dr.maximize_window()
dr.get('https://firms.guanplus.com/login')


usernameInput = dr.find_element_by_id('usernameInput')
passwordInput = dr.find_element_by_id('passwordInput')
loginButton = dr.find_element_by_id('loginButton')

usernameInput.send_keys('13683139989')
passwordInput.send_keys('qq123456')
loginButton.click()
time.sleep(2)

pageTitle = dr.title.encode('utf-8').strip()  #transfer str to bytes
pageUrl = dr.current_url.encode('utf-8').strip()

print ("title of current page is %s" ,pageTitle)
print('url of current page is %s',pageUrl)
time.sleep(2)

dr.back()
time.sleep(2)

dr.forward()
time.sleep(2)
dr.quit()
