from selenium import webdriver
import unittest
import xlrd
import time
from xlutils.copy import copy
from selenium.webdriver.common.by import By


class LoginSpec(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.baset_url = 'https://firms.guanplus.com'
        time.sleep(3)

    def test_loginin(self):

        result_list = []
        s = u'登录成功'
        f = u'登录失败'
        driver = self.driver
        driver.get(self.baset_url)
        login_list = self.get_login_dict()
        print('login_list =>',login_list)

        for u, p in login_list:
            username_text = self.driver.find_element_by_id('usernameInput')
            username_text.clear()
            username_text.send_keys(u)
            password_text = self.driver.find_element_by_id('passwordInput')
            password_text.clear()
            password_text.send_keys(p)
            self.driver.find_element_by_id('loginButton').click()
            time.sleep(3)
        if driver.current_url = self.baset_url + '/app/company-list':
            result_list.append(s)
            result_list.append(driver.current_url)
            self.

    def write_data(self,result):
        rb = xlrd.open_workbook('./test_case/excel_read/result.xls')
        wb = copy(rb)
        wbk = wb.get_sheet(0)
        for i in range(len(wbk))

        # else:
        #     print ('failed')
            # result_list.append('failed')
            # self.test_w

    # def test_write_data(self,result):
    #     rb = xlrd.open_workbook('.f.xls')
    #     wb = copy(rb)
    #     wbk = wb.get_sheet(0)
    #     for i in range(len(result)):
    #         wbk.wri

    def tearDown(self):
        self.driver.quit()


if __name__ == '_main_':
    unittest.main()
