from selenium import webdriver
import time
from base.public_page import PublicPage
from test_case.invoice.input_invoice_elem import InputInvoiceElem
from selenium.webdriver.support.ui import Select


class InvoicePage:

    # invoice_type:发票类型
    def __init__(self, driver, invoice_type):
        # self.driver = webdriver.Chrome()
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

# 选择发票类型
    def select_invoice_type(self, invoice_name):
        publicPage = PublicPage(self.driver)
        drop_loc = self.driver.find_element_by_xpath(
            InputInvoiceElem.invoice_type_drop_xpath)
        publicPage.select_dropdown_item(drop_loc, invoice_name)

# 输入发票号
    def set_invoice_num(self, invoice_num):
        publicPage = PublicPage(self.driver)
        invoice_num_loc = self.driver.find_element_by_xpath(
            InputInvoiceElem.invoice_num_xpath)
        publicPage.set_value(invoice_num_loc, invoice_num)

# 选择类别：f_type_name：一级类别名，s_type_name：二级类别名
    def select_category(self, category_name):
        publicPage = PublicPage(self.driver)
        drop_loc = self.driver.find_element_by_xpath(
            InputInvoiceElem.type_drop_xpath)
        publicPage.click_elem(drop_loc)
        time.sleep(2)
        s1 = Select(self.driver.find_element_by_css_selector('.parent-options'))
        for sele  in s1.options:
            print(sele.text)
