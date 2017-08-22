from selenium import webdriver
import unittest
import time
from base.enter_comp_page import EnterCompPage
from base.public_page import PublicPage
from test_case.invoice.invoice_page import InvoicePage
from config import Config
from data.input_invoice_data import input_invoice_general_data,output_invoice_data,input_invoice_special_data


class InputInvoiceSpec(unittest.TestCase):

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

    def test_input_special(self):
        publicPage = PublicPage(self.driver)
        invoicePage = InvoicePage(self.driver, Config.BASE_URL, 'input',input_invoice_special_data[0])
        invoicePage.go_to_new_invoice_page()
        invoicePage.type_input_invoice_special(input_invoice_special_data)    
    
        


    def tearDown(self):
        self.driver.quit()


if __name__ == '_main_':
    unittest.main()
