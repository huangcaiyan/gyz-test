from selenium import webdriver
import time
from test_case.login.login_page import LoginPage


class CompListPage:

    # location
    create_comp_xpath = '//*[@id="body"]/company-list/div[1]/div[3]/div[2]/button[1]'

    def __init__(self, driver):
        self.driver = driver

    def get_comp_name(self, comp_name):
        current_comp_name_loc = self.driver.find_element_by_link_text(
            comp_name)
        return current_comp_name_loc.text

    # 进入公司
    # comp_name 公司名称
    def enter_comp(self, comp_name):
        comp_name_loc = self.driver.find_element_by_link_text(comp_name)
        comp_name_loc.click()
        time.sleep(3)        
        c_comp_name = self.get_comp_name(comp_name)
        if c_comp_name == comp_name:
            print('当前公司公司名为： ',c_comp_name)

        else:
            print('————————————进入公司失败 ！————————————')

