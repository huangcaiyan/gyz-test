from selenium import webdriver
import time
import unittest
from test_case.salary.salary_page import SalaryPage
from base.enter_comp_page import EnterCompPage
from config import Config


class SalarySpec(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        enterCompPage = EnterCompPage(Config.BASE_URL, self.driver)
        enterCompPage.enter_comp(Config.ENTER_COMP_INFO_YB)
#

    def test_go_to_stuff_list_page(self):
        """测试 去员工管理页面"""
        page = SalaryPage(self.driver)
        page.go_to_stuff_list_page(Config.BASE_URL)
        c_url = self.driver.current_url
        print('员工管理页面url＝', c_url)
        self.assertEqual(c_url, Config.BASE_URL + page.stuff_list_url)

    def test_go_to_add_stuff_page(self):
        """测试 去添加员工页面"""
        page = SalaryPage(self.driver)
        page.go_to_add_stuff_page(Config.BASE_URL)
        c_url = self.driver.current_url
        print('添加员工页面url＝', c_url)
        self.assertEqual(c_url, Config.BASE_URL + page.stuadd_stuff_url)

    def test_go_to_import_stuff_page(self):
        """测试 去导入员工页面"""
        page = SalaryPage(self.driver)
        page.go_to_import_stuff_page(Config.BASE_URL)
        c_url = self.driver.current_url
        print('导入员工页面url', c_url)
        self.assertEqual(c_url, Config.BASE_URL + page.import_stuff_url)

    def test_go_to_salary_list_page(self):
        """测试 去工资表页面"""
        page = SalaryPage(self.driver)
        page.go_to_salary_list_page(Config.BASE_URL)
        c_url = self.driver.current_url
        print('工资表页面url＝', c_url)
        self.assertEqual(c_url, Config.BASE_URL + page.salary_list_url)

    def test_go_to_labour_list_page(self):
        """测试 去劳务表页面"""
        page = SalaryPage(self.driver)
        page.go_to_labour_list_page(Config.BASE_URL)
        c_url = self.driver.current_url
        print('劳务表页面url＝', c_url)
        self.assertEqual(c_url, Config.BASE_URL + page.labour_list_url)

    def test_go_to_salary_record_page(self):
        """测试 去工资发放记录页面"""
        page = SalaryPage(self.driver)
        page.go_to_salary_record_page(Config.BASE_URL)
        c_url = self.driver.current_url
        print('工资发放记录页面url＝', c_url)
        self.assertEqual(c_url, Config.BASE_URL + page.salary_record_url)

    def test_go_to_labour_record_page(self):
        """测试 去劳务发放记录页面"""
        page = SalaryPage(self.driver)
        page.go_to_labour_record_page(Config.BASE_URL)
        c_url = self.driver.current_url
        print('劳务发放记录页面url＝', c_url)
        self.assertEqual(c_url, Config.BASE_URL + page.labour_record_url)

    def tearDown(self):
        self.driver.quit()


if __name__ == '_main_':
    unittest.main()
