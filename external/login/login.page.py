# -*- encoding=utf-8 -*-
from selenium import webdriver
import time
class Login():
    # login
    def user_login(self,driver,username,password):
        usernameInput = driver.find_element_by_id('usernameInput')
        usernameInput.send_keys(username)
        passwordInput = driver.find_element_by_id('passwordInput')
        passwordInput.send_keys(password)
        loginButton = driver.find_element_by_id('loginButton')
        loginButton.click()
        time.sleep(3)

    def user_logout(self,driver):
        logoutDropdown = driver.find_element_by_xpath('//*[@id="personalInfoDropdownMenu"]/span')
        logoutDropdown.click()
        logoutBtn = driver.find_element_by_xpath('//*[@id="page-wrapper"]/navbar/div/nav/div[2]/ul/li[2]/ul/li[2]/a')
        logoutBtn.click()
        time.sleep(2)
        driver.quit()

    # def comp_login(self,driver):
    #     compName = driver.find_element_by_link_text('公司0714-3')
    #     compName.click()

    # def comp_logout(self,driver):
    #     compLogoutLink = driver.find_element_by_id('CompanyDropdownMenu')
    #     compLogoutLink.click()

   

    