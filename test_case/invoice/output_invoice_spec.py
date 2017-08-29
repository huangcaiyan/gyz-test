from selenium import webdriver
import time
import unittest
from base.enter_comp_page import EnterCompPage
from config import Config
from base.upload_file_page import UploadFilePage
from test_case.invoice.invoice_page import InvoicePage
'''
创建于20170829二
@author:caicai
开票测试
'''

class OutputInvoiceSpec(unittest.TestCase):
    # 开票导入文件
    file_dir = '/Users/huangcaiyan/work/guanplus-test/data/import_output_invoice_data_yb.xlsx'

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)

        enterCompPage = EnterCompPage(Config.BASE_URL, self.driver)
        enterCompPage.enter_comp(Config.ENTER_COMP_INFO_YB)

    def test_import_output_invoice(self):
        """开票－开票导入测试 """
        invoicePage = InvoicePage(self.driver, Config.BASE_URL, '', '')
        invoicePage.go_to_import_invoice_page()
        uploadFilePage = UploadFilePage(self.driver, self.file_dir)
        uploadFilePage.upload_file()
        time.sleep(5)
        self.driver.get(Config.BASE_URL + '/app/invoice/output-invoice')
        time.sleep(5)
        table_sum = invoicePage.get_table_sum()
        self.assertEqual(table_sum, '21,000.00')

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()


if __name__ == '_main_':
    unittest.main()
