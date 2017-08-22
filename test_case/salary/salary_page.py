import time
from base.public_page import PublicPage
from test_case.salary.salary_elem import *


class SalaryPage:

    def __init__(self, driver):
        self.driver = driver
        # self.salary_item = salary_item

# 去 员工管理页面
# stuff_list_elem:页面元素xpath
    def go_to_stuff_list_page(self, base_url):
        publicPage = PublicPage(self.driver)
        self.driver.get(base_url + stuff_list_url)
        time.sleep(3)
        stuff_list_loc = self.driver.find_element_by_xpath(stuff_list_elem)
        publicPage.is_element_present(stuff_list_loc)

# 去 添加员工页面
# add_stuff_elem:页面元素xpath
    def go_to_add_stuff_page(self, base_url):
        publicPage = PublicPage(self.driver)
        self.driver.get(base_url + add_stuff_url)
        time.sleep(3)
        add_stuff_loc = self.driver.find_element_by_xpath(add_stuff_elem)
        publicPage.is_element_present(add_stuff_loc)

# 去 员工导入页面
# import_stuff_elem:页面元素xpath
    def go_to_import_stuff_page(self, base_url):
        publicPage = PublicPage(self.driver)
        self.driver.get(base_url + import_stuff_url)
        time.sleep(3)
        import_stuff_loc = self.driver.find_element_by_xpath(import_stuff_elem)
        publicPage.is_element_present(import_stuff_loc)

# 去 工资表页面
# salary_list_elem:页面元素xpath
    def go_to_salary_list_page(self, base_url):
        publicPage = PublicPage(self.driver)
        self.driver.get(base_url + salary_list_url)
        time.sleep(3)
        salary_list_loc = self.driver.find_element_by_xpath(salary_list_elem)
        publicPage.is_element_present(salary_list_loc)

# 去 劳务表页面
# labour_list_elem:页面元素xpath
    def go_to_labour_list_page(self, base_url):
        publicPage = PublicPage(self.driver)
        self.driver.get(base_url + labour_list_url)
        time.sleep(3)
        labour_list_loc = self.driver.find_element_by_xpath(labour_list_elem)
        publicPage.is_element_present(labour_list_loc)

# 去 工资发放记录页面
# salary_record_elem:页面元素xpath
    def go_to_salary_record_page(self, base_url):
        publicPage = PublicPage(self.driver)
        self.driver.get(base_url + salary_record_url)
        time.sleep(3)
        salary_record_loc = self.driver.find_element_by_xpath(
            salary_record_elem)
        publicPage.is_element_present(salary_record_loc)

# 去 劳务发放记录页面
# labour_record_elem:页面元素xpath
    def go_to_labour_record_page(self, base_url):
        publicPage = PublicPage(self.driver)
        self.driver.get(base_url + labour_record_url)
        time.sleep(3)
        labour_record_loc = self.driver.find_element_by_xpath(
            labour_record_elem)
        publicPage.is_element_present(labour_record_loc)
