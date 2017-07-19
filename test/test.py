# -*- coding: utf-8 -*- 
from selenium import webdriver
import time
import HTMLTestRunner

# set up
dr = webdriver.Chrome()
# dr.set_window_size(240, 320)
dr.maximize_window()
dr.get('https://firms.guanplus.com/login')

# elems locatior
usernameInput = dr.find_element_by_id('usernameInput')
passwordInput = dr.find_element_by_id('passwordInput')
loginButton = dr.find_element_by_id('loginButton')

# login in
usernameInput.send_keys('13683139989')
passwordInput.send_keys('qq123456')
loginButton.click()
time.sleep(2)

# click company name
compName = dr.find_element_by_link_text('公司0714-3')

# get current window's handle
dashboard_windows = dr.current_window_handle

compName.click()
time.sleep(2)
btns = dr.find_elements_by_class_name("btn")
dr.find_element_by_css_selector('button[class=\"btn btn-primary  dropdown-toggle\"]').click()  
time.sleep(1)
dr.find_element_by_css_selector('button[data-title=\"再次结转\"]').click()
time.sleep(1)
# dr.find_elements_by_css_selector('button[class=\"btn btn-default btn-primary\"]').pop(1).click()
dr.switch_to_window

#transfer str to bytes 
pageTitle = dr.title.encode('utf-8').strip()  
pageUrl = dr.current_url.encode('utf-8').strip()

# print page title and url
print ("title of current page is %s" ,pageTitle)
print('url of current page is %s',pageUrl)
time.sleep(2)


time.sleep(2)
dr.quit()
