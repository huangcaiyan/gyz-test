from selenium import webdriver
import unittest
import time
from config import *
from test_case.login.login_page import LoginPage
from .invoice_page import InvoicePage
from base.enter_comp_page import EnterCompPage

class RecordInputInvoiceSpec(unittest.TestCase):
    input_invoice_list_url = BASE_URL + '/app/invoice/input-invoice'

    

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(BASE_URL)
        enter_comp_page = EnterCompPage(self.driver,ENTER_COMP_INFO)
        invoicePage = InvoicePage(self.driver,'input')

    def test1(self):
        invoicePage = InvoicePage(self.driver,'input')
        invoicePage.go_to_invoice_list(BASE_URL)
        c_url = self.driver.current_url
        assertEqual(self.input_invoice_list_url,c_url)


    def tearDown(self):
        time.sleep(2)
        self.driver.quit()


if __name__ == '_main_':
    unittest.main()

