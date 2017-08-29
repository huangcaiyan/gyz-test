from selenium import webdriver
import unittest
import time
from test_case.invoice.invoice_page import InvoicePage 
from base.enter_comp_page import EnterCompPage 
from base.public_page import PublicPage 
from config import Config
class DeductionSpec(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        enterCompPage = EnterCompPage(Config.BASE_URL,self.driver)
        enterCompPage.enter_comp(Config.ENTER_COMP_INFO_YB)


    # def test_import_identify_list(self):
    #     invoicePage = InvoicePage(self.driver)