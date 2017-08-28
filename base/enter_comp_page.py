from selenium import webdriver
import time
from test_case.login.login_page import LoginPage
from base.public_page import PublicPage
from base.enter_comp_elem import *
from test_case.setting.page.comp_billing_page import CompBillingPage 


class EnterCompPage:

    # location
    create_comp_xpath = '//*[@id="body"]/company-list/div[1]/div[3]/div[2]/button[1]'

    def __init__(self, url, driver):
        self.url = url
        self.driver = driver

    def get_comp_name(self, comp_name):
        current_comp_name_loc = self.driver.find_element_by_link_text(
            comp_name)
        return current_comp_name_loc.text

    # 进入公司
    # comp_name 公司名称
    def enter_comp(self, enter_comp_info):
        loginPage = LoginPage(self.url, self.driver)
        loginPage.login(enter_comp_info[0])
        comp_name_loc = self.driver.find_element_by_link_text(
            enter_comp_info[1])
        comp_name_loc.click()
        time.sleep(5)
        c_comp_name = self.get_comp_name(enter_comp_info[1])
        if c_comp_name == enter_comp_info[1]:
            print('当前公司公司名为： ', c_comp_name)
        else:
            print('————————————进入公司失败 ！————————————')
            
# 创建帐套
    def set_comp_name(self,comp_name):
        publicPage = PublicPage(self.driver)
        comp_name_loc = self.driver.find_element_by_name(comp_name_elem)
        publicPage.set_value(comp_name_loc,comp_name)

    def set_legal_person_name(self,legal_person_name):
        publicPage = PublicPage(self.driver)
        legal_person_name_loc = self.driver.find_element_by_name(legal_person_name_elem)
        publicPage.set_value(legal_person_name_loc,legal_person_name)

    def set_registered_capital_name(self,registered_capital_name):
        publicPage = PublicPage(self.driver)
        registered_capital_name_loc = self.driver.find_element_by_name(registered_capital_name_elem)
        publicPage.set_value(registered_capital_name_loc,registered_capital_name)


    # def create_comp(self,new_comp_info):
    #     loginPage = LoginPage(self.url,self.driver)
    #     loginPage.login(new_comp_info[0])



