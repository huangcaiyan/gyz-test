from selenium import webdriver
import time
from test_case.login.login_page import LoginPage
from test_case.external.comp_list_elem import *
from base.public_page import PublicPage


class CompListPage:

    # location

    def __init__(self, driver):
        self.driver = driver
        
    # 获取账套名称
    def get_comp_name(self, comp_name):
        current_comp_name_loc = self.driver.find_element_by_link_text(
            comp_name)
        return current_comp_name_loc.text
  
    # 点击创建公司按钮
    def click_create_comp(self):
        try:
            publicPage = PublicPage(self.driver)
            create_btn_loc = self.driver.find_element_by_xpath(
                create_comp_btn_elem)
            publicPage.click_elem(create_btn_loc)
        except expression as e:
            print('There was an exception when click_create_comp=> %s', str(e))

    # 进入公司
    # comp_name 公司名称
    def enter_comp(self, comp_name):
        comp_name_loc = self.driver.find_element_by_link_text(comp_name)
        comp_name_loc.click()
        time.sleep(3)
        c_comp_name = self.get_comp_name(comp_name)
        if c_comp_name == comp_name:
            print('当前公司公司名为： ', c_comp_name)

        else:
            print('————————————进入公司失败 ！————————————')
