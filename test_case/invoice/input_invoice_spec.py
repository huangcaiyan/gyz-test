from selenium import webdriver
import unittest
import time
from base.enter_comp_page import EnterCompPage
from base.public_page import PublicPage
from test_case.invoice.invoice_page import InvoicePage
from config import Config
from data.input_invoice_data import input_invoice_general_data,output_invoice_data,input_invoice_special_data
from base.read_excel import ReadExcel

class InputInvoiceSpec(unittest.TestCase):
    # 一般纳税人－收专票测试数据
    invoice_data_file = './data/invoice_data.xlsx'

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        enterCompPage = EnterCompPage(Config.BASE_URL, self.driver)
        enterCompPage.enter_comp(Config.ENTER_COMP_INFO_YB)

    def test_input_general(self):
        publicPage = PublicPage(self.driver)
        invoicePage = InvoicePage(self.driver, Config.BASE_URL, 'input')
        invoicePage.go_to_new_invoice_page()
        invoicePage.type_input_invoice_general(input_invoice_general_data)
        time.sleep(4)

    def test_output(self):
        publicPage = PublicPage(self.driver)
        invoicePage = InvoicePage(self.driver, Config.BASE_URL, 'output')
        invoicePage.go_to_new_invoice_page()
        invoicePage.type_output_invoice(output_invoice_data)

    def test_type_input_invoice_special(self):
        """一般纳税人－报表测试－记录收专票"""
        publicPage = PublicPage(self.driver)
        invoicePage = InvoicePage(self.driver, Config.BASE_URL, 'input','专票')
        invoicePage.go_to_new_invoice_page()
        readExcel = ReadExcel(self.invoice_data_file)
        excel_data = readExcel.get_value_in_order(0)
        for input_invoice_special_data in excel_data:
            invoicePage.type_input_invoice_special(input_invoice_special_data)    
    
    def test(self):
        invoicePage = InvoicePage(self.driver, Config.BASE_URL, 'input','专票')
        invoicePage.go_to_new_invoice_page()
        readExcel = ReadExcel(self.invoice_data_file)
        excel_data = readExcel.get_value_in_order(2)
        for data in excel_data:
            invoicePage.type_category(data)
        
        


    def tearDown(self):
        self.driver.quit()


if __name__ == '_main_':
    unittest.main()
