from selenium import webdriver
import unittest
import time
from base.enter_comp_page import EnterCompPage
from base.public_page import PublicPage
from test_case.invoice.invoice_page import InvoicePage
from config import Config


class InputInvoiceSpec(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        enterCompPage = EnterCompPage(Config.BASE_URL, self.driver)
        enterCompPage.enter_comp(Config.ENTER_COMP_INFO_YB)

    def test_record_input_invoice(self):
        publicPage = PublicPage(self.driver)
        invoicePage = InvoicePage(self.driver, 'input')
        invoicePage.go_to_new_invoice_page(Config.BASE_URL)
        invoicePage.select_category(0, 1)
        time.sleep(4)

    def tearDown(self):
        self.driver.quit()


if __name__ == '_main_':
    unittest.main()
