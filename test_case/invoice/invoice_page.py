from selenium import webdriver
import time
from base.public_page import PublicPage
from test_case.invoice.invoice_elem import *
from selenium.webdriver.support.ui import Select


class InvoicePage:

    # element loc

 # invoice_type:发票类型
    def __init__(self, driver, base_url, invoice_type,invoice_name):
        # self.driver = webdriver.Chrome()
        self.driver = driver
        self.base_url = base_url
        self.invoice_type = invoice_type
        self.invoice_name = invoice_name

# 去发票列表页面
    def go_to_invoice_list(self):
        publicPage = PublicPage(self.driver)
        self.driver.get(self.base_url + '/app/invoice/' +
                        self.invoice_type + '-invoice')
        time.sleep(3)

# 去记发票页面
    def go_to_new_invoice_page(self):
        self.driver.get(self.base_url + '/app/invoice/tab/new-' +
                        self.invoice_type + '-invoice')
        time.sleep(3)

# 选择发票类型;
# invoice_name:发票类型名称（专票、普票、无票）
    def select_invoice_type(self):
        publicPage = PublicPage(self.driver)
        drop_loc = self.driver.find_element_by_xpath(
            '//*[@id="body"]/tab/new-' + self.invoice_type + '-invoice/div/div[2]/ul/div[1]/div/label[2]/ng-select')
        publicPage.select_dropdown_item(drop_loc, self.invoice_name)
        time.sleep(1)

# 选择对方信息;
# contact_name：往来名称
    def select_contact(self, contact_name):
        publicPage = PublicPage(self.driver)
        if self.invoice_type == 'input':
            drop_loc = self.driver.find_element_by_xpath(
                input_contact_drop_elem)
        elif self.invoice_type == 'output':
            drop_loc = self.driver.find_element_by_xpath(
                output_contact_drop_elem)
        else:
            return Error
        publicPage.select_dropdown_item(drop_loc, contact_name)
        time.sleep(1)

# 选择发票状态(开票);
# invoice_status:发票状态（税控自开、税控代开）;
# invoice_status_drop_elem:发票状态下拉展开xpath
    def select_invoice_status(self, invoice_status):
        publicPage = PublicPage(self.driver)
        drop_loc = self.driver.find_element_by_xpath(invoice_status_drop_elem)
        publicPage.select_dropdown_item(drop_loc, invoice_status)
        time.sleep(1)

# 输入发票号
    def set_invoice_num(self, invoice_num):
        publicPage = PublicPage(self.driver)
        if self.invoice_type == 'input':
            invoice_num_loc = self.driver.find_element_by_xpath(
                input_invoice_sum_elem)
        elif self.invoice_type == 'output':
            invoice_num_loc = self.driver.find_element_by_xpath(
                output_invoice_sum_elem)
        else:
            return Error
        publicPage.set_value(invoice_num_loc, invoice_num)
        time.sleep(1)

# 选择类别;
# p_indexe：一级类别index;
# c_index：二级类别index;
    def select_category(self, p_index, c_index):
        publicPage = PublicPage(self.driver)
        drop_loc = self.driver.find_element_by_xpath(
            '//*[@id="body"]/tab/new-' + self.invoice_type + '-invoice/div/div[2]/ul/table/tbody/tr[1]/td[1]/ng-select')
        publicPage.click_elem(drop_loc)
        time.sleep(2)

        s1 = self.driver.find_elements_by_css_selector(parent_elem)[p_index]
        publicPage.click_elem(s1)
        time.sleep(1)

        s2 = self.driver.find_elements_by_css_selector(child_elem)[c_index]
        return publicPage.click_elem(s2)
        time.sleep(1)

# 选择部门性质;
# partment_name:部门性质名称（销售部门、管理部门）
    def select_partment(self, partment_name):
        publicPage = PublicPage(self.driver)
        drop_loc = self.driver.find_element_by_xpath(
            '//*[@id="body"]/tab/new-' + self.invoice_type + '-invoice/div/div[2]/ul/table/tbody/tr[1]/td[2]/ng-select')
        publicPage.select_dropdown_item(drop_loc, partment_name)
        time.sleep(1)


# 税率选择;
# tax_rate:税率（1.5%，3%，5%，6%，11%，13%，17%）
    def select_tax_rate(self, tax_rate):
        publicPage = PublicPage(self.driver)
        drop_loc = self.driver.find_element_by_xpath(
            '//*[@id="body"]/tab/new-' + self.invoice_type + '-invoice/div/div[2]/ul/table/tbody/tr[1]/td[3]/ng-select')
        publicPage.select_dropdown_item(drop_loc, tax_rate)
        time.sleep(1)

# 选择进项税类别
# tax_category_name:进项税类别名称;
# tax_category_drop_elem:下拉展开xpath
    def select_input_tax_category(self, tax_category_name):
        publicPage = PublicPage(self.driver)
        drop_loc = self.driver.find_element_by_xpath(tax_category_drop_elem)
        publicPage.select_dropdown_item(drop_loc, tax_category_name)
        time.sleep(1)

# 设置金额
# sum:价税合计;
# sum_elem:金额tag_name;
    def set_sum(self, sum):
        publicPage = PublicPage(self.driver)
        # sum_loc = self.driver.find_element_by_tag_name(sum_elem)
        sum_loc = self.driver.find_element_by_css_selector(sum_elem)
        publicPage.set_value(sum_loc, sum)
        time.sleep(1)

# 设置备注
# attach_value:备注内容;
    def set_attach(self, attach_value):
        publicPage = PublicPage(self.driver)
        if self.invoice_type == 'input' and self.invoice_name == '专票':
            attach_loc = self.driver.find_element_by_xpath(
                '//*[@id="body"]/tab/new-' + self.invoice_type + '-invoice/div/div[2]/ul/table/tbody/tr[1]/td[6]/input')
        else:
            attach_loc = self.driver.find_element_by_xpath(
                '//*[@id="body"]/tab/new-' + self.invoice_type + '-invoice/div/div[2]/ul/table/tbody/tr[1]/td[5]/input')
        publicPage.set_value(attach_loc, attach_value)
        time.sleep(1)

# 新增明细;
# new_row_elem:新增明细link_text
    def new_row(self):
        publicPage = PublicPage(self.driver)
        new_row_loc = self.driver.find_element_by_link_text(new_row_elem)
        publicPage.click_elem(new_row_loc)
        time.sleep(1)


# 添加标签;
# tag_name:标签名;
# add_tag_btn_elem:添加标签按钮class;
    def add_tag(self, tag_name):
        publicPage = PublicPage(self.driver)
        add_btn_loc = self.driver.find_elements_by_css_selector(
            add_tag_btn_elem)
        publicPage.click_elem(add_btn_loc)
        time.sleep(1)

# 点击保存并新增
# add_and_save_elem:保存并新增 class
    def save_and_add(self):
        publicPage = PublicPage(self.driver)
        btn_loc = self.driver.find_element_by_css_selector(add_and_save_elem)
        publicPage.click_elem(btn_loc)
        time.sleep(1)

# 点击保存
    def save(self):
        publicPage = PublicPage(self.driver)
        btn_loc = self.driver.find_element_by_xpath(
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
    def type_input_invoice_general(self, input_invoice_general_info):
        self.select_invoice_type(input_invoice_general_info[0])
        self.select_contact(input_invoice_general_info[1])
        self.select_category(
            input_invoice_general_info[2][0], input_invoice_general_info[2][1])
        self.select_partment(input_invoice_general_info[3])
        self.select_tax_rate(input_invoice_general_info[4])
        self.set_sum(input_invoice_general_info[5])
        self.set_attach(input_invoice_general_info[6])
        # self.save_and_add()
        self.save()
        time.sleep(5)

# (收票－专票)发票类型、对方信息、发票号码、类别、部门性质、税率、进项税类别、价税合计、备注
    def type_input_invoice_special(self, input_invoice_special_info):
        # self.select_invoice_type(input_invoice_special_info[0])
        self.select_invoice_type()        
        self.select_contact(input_invoice_special_info[1])
        self.set_invoice_num(input_invoice_special_info[2])
        self.select_category(
            input_invoice_special_info[3][0], input_invoice_special_info[3][0])
        self.select_partment(input_invoice_special_info[4])
        self.select_tax_rate(input_invoice_special_info[5])
        self.select_input_tax_category(input_invoice_special_info[6])
        self.set_sum(input_invoice_special_info[7])
        self.set_attach(input_invoice_special_info[8])
        self.save_and_add()

# (收票－专票)发票类型、对方信息、发票号码、类别、部门性质、税率、进项税类别、价税合计、备注
    def type_input_invoice_special1(self, input_invoice_special_info):
        # self.select_invoice_type(input_invoice_special_info[0])
        self.select_invoice_type()        
        self.select_contact(input_invoice_special_info[1])
        self.set_invoice_num(input_invoice_special_info[2])
        self.select_category(input_invoice_special_info[3])
        self.select_partment(input_invoice_special_info[4])
        self.select_tax_rate(input_invoice_special_info[5])
        self.select_input_tax_category(input_invoice_special_info[6])
        self.set_sum(input_invoice_special_info[7])
        self.set_attach(input_invoice_special_info[8])

# 开票,发票类型、发票状态、对方信息、发票号码、类别、部门性质、税率、总额、备注
    def type_output_invoice(self, output_invoice_info):
        # self.select_invoice_type(output_invoice_info[0])
        self.select_invoice_type()        
        self.select_invoice_status(output_invoice_info[1])
        self.select_contact(output_invoice_info[2])
        self.set_invoice_num(output_invoice_info[3])
        self.select_category(
            output_invoice_info[4][0], output_invoice_info[4][1])
        self.select_partment(output_invoice_info[5])
        self.select_tax_rate(output_invoice_info[6])
        self.set_sum(output_invoice_info[7])
        self.set_attach(output_invoice_info[8])
        self.save_and_add()
