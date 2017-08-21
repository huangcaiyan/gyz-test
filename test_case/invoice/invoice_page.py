from selenium import webdriver
import time
from base.public_page import PublicPage
from test_case.invoice.invoice_elem import *
from selenium.webdriver.support.ui import Select


class InvoicePage:

    # element loc

 # invoice_type:发票类型
    def __init__(self, driver, invoice_type):
        self.driver = webdriver.Chrome()
        self.driver = driver
        self.invoice_type = invoice_type


# 去发票列表页面
    def go_to_invoice_list(self, base_url):
        publicPage = PublicPage(self.driver)
        self.driver.get(base_url + '/app/invoice/' +
                        self.invoice_type + '-invoice')
        time.sleep(3)

# 去记发票页面
    def go_to_new_invoice_page(self, base_url):
        self.driver.get(base_url + '/app/invoice/tab/new-' +
                        self.invoice_type + '-invoice')
        time.sleep(3)

# 选择发票类型,invoice_name:发票类型名称（专票、普票、无票）
    def select_invoice_type(self, invoice_name):
        publicPage = PublicPage(self.driver)
        drop_loc = self.driver.find_element_by_xpath(
            '//*[@id="body"]/tab/new-' + self.invoice_type + '-invoice/div/div[2]/ul/div[1]/div/label[2]/ng-select')
        publicPage.select_dropdown_item(drop_loc, invoice_name)
        time.sleep(1)

# 选择对方信息,contact_name：往来名称
    def select_contact(self, contact_name):
        publicPage = PublicPage(self.driver)
        drop_loc = self.driver.find_element_by_xpath(
            '//*[@id="body"]/tab/new-' + self.invoice_type + '-invoice/div/div[2]/ul/div[1]/div/label[3]/ng-select')
        publicPage.select_dropdown_item(drop_loc, contact_name)
        time.sleep(1)

# 选择发票状态(开票),invoice_status:发票状态（税控自开、税控代开）
    def select_invoice_status(self, invoice_status):
        publicPage = PublicPage(self.driver)
        drop_loc = self.driver.find_element_by_xpath(Invoice_Status_Drop_Xpath)
        time.sleep(1)


# 输入发票号
    def set_invoice_num(self, invoice_num):
        publicPage = PublicPage(self.driver)
        invoice_num_loc = self.driver.find_element_by_xpath(
            '//*[@id="body"]/tab/new-' + self.invoice_type + '-invoice/div/div[2]/ul/div[1]/div/label[4]/div/input')
        publicPage.set_value(invoice_num_loc, invoice_num)
        time.sleep(1)

# 选择类别：p_indexe：一级类别index，c_index：二级类别index
    def select_category(self, p_index, c_index):
        publicPage = PublicPage(self.driver)
        drop_loc = self.driver.find_element_by_xpath(
            '//*[@id="body"]/tab/new-' + self.invoice_type + '-invoice/div/div[2]/ul/table/tbody/tr[1]/td[1]/ng-select')
        publicPage.click_elem(drop_loc)
        time.sleep(2)

        s1 = self.driver.find_elements_by_css_selector(
            '.parent-options')[p_index]
        publicPage.click_elem(s1)
        time.sleep(1)

        s2 = self.driver.find_elements_by_css_selector(
            '.children-options')[c_index]
        return publicPage.click_elem(s2)
        time.sleep(1)

# 选择部门性质,partment_name:部门性质名称（销售部门、管理部门）
    def select_partment(self, partment_name):
        publicPage = PublicPage(self.driver)
        drop_loc = self.driver.find_element_by_xpath(
            '//*[@id="body"]/tab/new-' + self.invoice_type + '-invoice/div/div[2]/ul/table/tbody/tr[1]/td[2]/ng-select')
        publicPage.select_dropdown_item(drop_loc, partment_name)
        time.sleep(1)


# 税率选择，tax_rate:税率（1.5%，3%，5%，6%，11%，13%，17%）
    def select_tax_rate(self, tax_rate):
        publicPage = PublicPage(self.driver)
        drop_loc = self.driver.find_element_by_xpath(
            '//*[@id="body"]/tab/new-' + self.invoice_type + '-invoice/div/div[2]/ul/table/tbody/tr[1]/td[3]/ng-select')
        publicPage.select_dropdown_item(drop_loc, tax_rate)
        time.sleep(1)

# 选择进项税类别,tax_category_name:进项税类别名称
    def select_input_tax_category(self, tax_category_name):
        publicPage = PublicPage(self.driver)
        drop_loc = self.driver.find_element_by_xpath(Tax_Category_Drop_Xpath)
        publicPage.select_dropdown_item(drop_loc, tax_category_name)
        time.sleep(1)


# 设置金额,sum:价税合计
    def set_sum(self, sum):
        publicPage = PublicPage(self.driver)
        sum_loc = self.driver.find_element_by_tag_name('bp-input')
        publicPage.set_value(sum_loc, sum)
        time.sleep(1)

# 设置备注,attach_value:备注内容
    def set_attach(self, attach_value):
        publicPage = PublicPage(self.driver)
        attach_loc = self.driver.find_element_by_xpath('//*[@id="body"]/tab/new-' + self.invoice_type + '-invoice/div/div[2]/ul/table/tbody/tr[1]/td[5]/input')
        publicPage.set_value(attach_loc, attach_value)
        time.sleep(1)

# 添加标签,tag_name:标签名
    def add_tag(self, tag_name):
        publicPage = PublicPage(self.driver)
        add_btn_loc = self.driver.find_elements_by_css_selector('.addTagFont')
        publicPage.click_elem(add_btn_loc)
        time.sleep(1)

# 点击保存并新增
    def save_and_add(self):
        publicPage = PublicPage(self.driver)
        btn_loc = self.driver.find_element_by_css_selector('.btn-again')
        publicPage.click_elem(btn_loc)
        time.sleep(1)

# 点击保存
    def save(self):
        publicPage = PublicPage(self.driver)
        btn_loc = self.driver.find_element_by_css_selector(
            '//*[@id="body"]/tab/new-' + self.invoice_type + '-invoice/div/div[2]/ul/div[3]/div/span/button[2]')
        publicPage.click_elem(btn_loc)
        time.sleep(1)

# 点击取消
    def cancel(self):
        publicPage = PublicPage(self.driver)
        btn_loc = self.driver.find_element_by_xpath(
            '//*[@id="body"]/tab/new-' + self.invoice_type + '-invoice/div/div[2]/ul/div[3]/div/span/button[3]')
        publicPage.click_elem(btn_loc)
        time.sleep(1)

# (收票-普票)发票类型、对方信息、类别、部门性质、税率、价税合计、备注
    def set_input_invoice_general(self, input_invoice_general_info):
        self.select_invoice_type(input_invoice_general_info[0])
        self.select_contact(input_invoice_general_info[1])
        self.select_category(input_invoice_general_info[2])
        self.select_partment(input_invoice_general_info[3])
        self.select_tax_rate(input_invoice_general_info[4])
        self.set_sum(input_invoice_general_info[5])
        self.set_attach(input_invoice_general_info[6])
        self.save_and_add()

# (收票－专票)发票类型、对方信息、发票号码、类别、部门性质、税率、进项税类别、价税合计、备注
    def set_input_invoice_special(self, input_invoice_special_info):
        self.select_invoice_type(input_invoice_special_info[0])
        self.select_contact(input_invoice_special_info[1])
        self.set_invoice_num(input_invoice_special_info[2])
        self.select_category(input_invoice_special_info[3])
        self.select_partment(input_invoice_special_info[4])
        self.select_tax_rate(input_invoice_special_info[5])
        self.select_input_tax_category(input_invoice_special_info[6])
        self.set_sum(input_invoice_special_info[7])
        self.set_attach(input_invoice_special_info[8])
        self.save_and_add()
