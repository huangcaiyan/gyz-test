from selenium import webdriver
import unittest
import time
from base.enter_comp_page import EnterCompPage
from config import Config 
from test_case.salary.salary_page import SalaryPage 

class StuffListSpec(unittest.TestCase):
    file_dir = './data/import_stuff_2_yb.xlsx'

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        enterCompPage = EnterCompPage(Config.BASE_URL,self.driver)
        enterCompPage.enter_comp(Config.ENTER_COMP_INFO_YB)


    def test_import_stuff(self):
        """员工管理－员工导入测试 """
        salaryPage = SalaryPage(self.driver)
        salaryPage.go_to_import_stuff_page()
        time.sleep(3)
        salaryPage.import_stuff(self.file_dir)
        time.sleep(4)
        c_url = self.driver.current_url
        self.assertEqual(c_url,Config.BASE_URL+'/app/salary/stuff-list')
