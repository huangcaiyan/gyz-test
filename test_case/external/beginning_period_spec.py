from selenium import webdriver
import unittest
import time
from base.upload_file_page import UploadFilePage
from base.enter_comp_page import EnterCompPage
from config import Config
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from base.public_page import PublicPage
from test_case.external.beginning_period_elem import *
from base.read_excel import ReadExcel
from test_case.external.beginning_period_page import BeginningPeriodPage


class BeginningPeriodSpec(unittest.TestCase):
    file_dir = '/Users/huangcaiyan/work/guanplus-test/data/beginning_period_data.xlsx'
    bank_dir = '/Users/huangcaiyan/work/guanplus-test/data/bank_distribute_data.xlsx'

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        enterCompPage = EnterCompPage(Config.BASE_URL, self.driver)
        enterCompPage.enter_comp(Config.ENTER_COMP_INFO_YB)

    def test_import_beginning_data(self):
        publicPage = PublicPage(self.driver)
        self.driver.get(Config.BASE_URL + '/app/finance/import')
        uploadFilePage = UploadFilePage(self.driver, self.file_dir)
        uploadFilePage.upload_file_qichu()
        self.driver.get(Config.BASE_URL + '/app/finance/beginningPeriod')
        time.sleep(3)
        debit_sum_loc = self.driver.find_element_by_xpath(debit_sum_elem)
        publicPage.get_value(debit_sum_loc)
        self.assertEqual(debit_sum, '159600.00')

    def test_distribute_bank(self):
        publicPage = PublicPage(self.driver)
        readExcel = ReadExcel(self.bank_dir)
        page = BeginningPeriodPage(self.driver)
        page.open_bank_distribute()
        value = readExcel.get_value_in_order(0)
        for bank_info in value:
            page.distribute_bank(bank_info)
            time.sleep(2)

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()


if __name__ == '_main_':
    unittest.main()
