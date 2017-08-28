from selenium import webdriver
import time
from base.public_page import PublicPage
from test_case.external.beginning_period_elem import *


class BeginningPeriodPage(object):
    def __init__(self, driver):
        # self.driver = webdriver.Chrome()
        self.driver = driver

    def go_to_finance_import_page(self):
        publicPage = PublicPage(self.driver)
        publicPage.click_elem()

    # 分配银行
    # 设置银行账户名称
    # 点击分配窗口
    def open_bank_distribute(self):
        publicPage = PublicPage(self.driver)
        publicPage.click_elem(bank_distribute_elem)
        time.sleep(1)

    def set_account_name(self, account_name):
        publicPage = PublicPage(self.driver)
        account_name_loc = self.driver.find_element_by_xpath(account_name_elem)
        publicPage.set_value(account_name_loc, account_name)

    # 设置开户银行
    def set_bank_name(self, bank_name):
        publicPage = PublicPage(self.driver)
        bank_name_loc = self.driver.find_element_by_xpath(bank_name_elem)
        publicPage.set_value(bank_name_loc, bank_name)

    # 设置支行
    def set_bank_branch(self, branch_name):
        publicPage = PublicPage(self.driver)
        branch_name_loc = self.driver.find_element_by_xpath(bank_branch_elem)
        publicPage.set_value(branch_name_loc, branch_name)

    # 分配银行整合
    def distribute_bank(self, bank_info):
        publicPage = PublicPage(self.driver)
        # self.open_bank_distribute()
        account_name_loc = self.driver.find_element_by_xpath(account_name_elem)
        bank_name_loc = self.driver.find_element_by_xpath(bank_name_elem)
        branch_name_loc = self.driver.find_element_by_xpath(bank_branch_elem)
        bank_num_loc = self.driver.find_element_by_xpath(bank_num_elem)
        bank_initial_balance_loc = self.driver.find_element_by_xpath(
            bank_initial_balance_elem)
        save_bank_btn_loc = self.driver.find_element_by_xpath(
            save_bank_btn_elem)
        publicPage.set_value(account_name_loc, bank_info[0])
        publicPage.set_value(bank_name_loc, bank_info[1])
        publicPage.set_value(branch_name_loc, bank_info[2])
        publicPage.set_value(bank_num_loc, bank_info[3])
        publicPage.set_value(bank_initial_balance_loc, bank_info[4])
        publicPage.click_elem(save_bank_btn_loc)
        time.sleep(2)
