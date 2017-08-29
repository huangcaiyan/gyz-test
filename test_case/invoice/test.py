from selenium import webdriver
import time
import unittest
from config import Config
from test_case.invoice.invoice_page import InvoicePage 
from base.enter_comp_page import EnterCompPage 
class Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)

        enterCompPage = EnterCompPage(Config.BASE_URL,self.driver)
        enterCompPage.enter_comp(Config.ENTER_COMP_INFO_YB)

    def test_set_attach(self):
        invoicePage = InvoicePage(self.driver,Config.BASE_URL,'input','专票')
        invoicePage.go_to_new_invoice_page()
        invoicePage.set_attach_special('测试')
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

if __name__ == '_main_':
    unittest.main()
        


