from selenium import webdriver
import time
from test_case.login.login_page import LoginPage
from base.public_page import PublicPage
from base.enter_comp_elem import *
from test_case.setting.page.comp_billing_page import CompBillingPage
from selenium.webdriver.support.ui import WebDriverWait
from test_case.setting.page.comp_billing_elem import *
# from test_case.external.comp_list_elem import *


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

    # def type_create_comp_info(self,new_comp_info):
    #     compBillingPage = CompBillingPage(self.driver)
    #     compBillingPage.set_comp_name(new_comp_info[0])
    #     compBillingPage.set_legal_person_name(new_comp_info[1])
    #     compBillingPage.set_registered_capital(new_comp_info[2])
    #     compBillingPage.select_prov(new_comp_info[3])
    #     compBillingPage.select_city(new_comp_info[4])
    #     compBillingPage.select_distr(new_comp_info[5])
    #     compBillingPage.select_begin_date(new_comp_info[6])
    #     compBillingPage.set_tax_num(new_comp_info[7])
    #     compBillingPage.select_industry(new_comp_info[8])
        
        

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
    # new_comp_info：创建公司信息list
    # page_url:创建公司页面url
    def create_comp(self,page_url, new_comp_info):
        loginPage = LoginPage(self.url, self.driver)
        compBillingPage = CompBillingPage(self.driver)
        loginPage.login(new_comp_info[0])
        time.sleep(2)
        self.driver.get(page_url)
        time.sleep(3)

        # try:
        #     WebDriverWait(driver, 10).until(
        #         self.driver.find_element_by_xpath(create_comp_btn_elem)
        #         .is_displayed())
        #     self.driver.get(page_url)
        #     time.sleep(4)

