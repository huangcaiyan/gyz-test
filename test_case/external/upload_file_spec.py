from selenium import webdriver
import time
import unittest
from base.upload_file_page import UploadFilePage
from base.enter_comp_page import EnterCompPage
from config import Config


class UploadFileSpec(unittest.TestCase):
    file_dir = '/Users/huangcaiyan/work/guanplus-test/data/beginning_period_data.xlsx'

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        enterCompPage = EnterCompPage(Config.BASE_URL, self.driver)
        enterCompPage.enter_comp(Config.ENTER_COMP_INFO)
        time.sleep(2)

    def test_upload_file(self):
        uploadFilePage = UploadFilePage(self.driver, self.file_dir)
        self.driver.get(Config.BASE_URL + '/app/finance/import')
        time.sleep(2)
        uploadFilePage.upload_file_qichu()
        time.sleep(10)

    def tearDown(self):
        self.driver.quit()
        pass


if __name__ == '_main_':
    unittest.main()






