from selenium import webdriver
import time
import unittest
from base.public_page import PublicPage


class UploadFilePage(object):
    def __init__(self, driver, file_dir):
        # self.driver = webdriver.Chrome()
        self.driver = driver
        self.file_dir = file_dir

    def upload_file_qichu(self):
        publicPage = PublicPage(self.driver)
        upload_btn_loc = self.driver.find_element_by_id('fileUploadBtn')
        # publicPage.is_element_prensent(upload_btn_loc)
        # # upload_btn_loc.click()
        publicPage.is_element_present(upload_btn_loc)
        upload_btn_loc.send_keys(self.file_dir)
        # publicPage.set_value(upload_btn_loc, self.file_dir)
        time.sleep(5)


if __name__ == '_main_':
    unittest.main()
