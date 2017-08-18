import time
from base.public_page import PublicPage


class SalaryPage:

    # element loc
    # 员工管理
    stuff_list_url = '/app/salary/stuff-list'
    stuff_list_xpath = '//*[@id="body"]/stuff-list/div[2]/div/div/ol/li[3]/button[1]'

# 添加员工
    add_stuff_url = '/app/salary/stuff'
    add_stuff_xpath = '//*[@id="body"]/stuff/div[3]/div[1]/span'
# 导入员工
    import_stuff_url = '/app/salary/stuff-import'
    import_stuff_xpath = '//*[@id="body"]/stuff-import/div[2]/div/div[2]/upload-attachments/div/div/span/label'
# 工资表
    salary_list_url = '/app/salary/salary-sheet/salary'
    salary_list_xpath = '//*[@id="body"]/salary/salary-sheet/div[2]/div/div/div[2]/div/div/div/table/thead/tr[1]/th[1]'
# 劳务表
    labour_list_url = '/app/salary/salary-sheet/labour'
    labour_list_xpath = '//*[@id="body"]/salary/labour-sheet/div[2]/div/div/div[2]/div/div/div/table/thead/tr/th[1]'
# 工资发放记录
    salary_record_url = '/app/salary/salary-record/salary'
    salary_record_xpath = '//*[@id="body"]/salary-router-record/salary-record/div/div/div/div[2]/div/div/div/table/thead/tr[1]/th[1]'
# 劳务发放记录
    labour_record_url = '/app/salary/salary-record/labour'
    labour_record_xpath = '//*[@id="body"]/salary-router-record/labour-record/div/div/div/div[2]/div/div/div/table/thead/tr/th[1]'

    def __init__(self, driver,salary_item):
        self.driver = driver
        self.salary_item = salary_item

# 去 员工管理页面

    def go_to_stuff_list_page(self, base_url):
        publicPage = PublicPage(self.driver)
        self.driver.get(base_url + self.stuff_list_url)
        time.sleep(3)
        stuff_list_loc = self.driver.find_element_by_xpath(
            self.stuff_list_xpath)
        publicPage.is_element_present(stuff_list_loc)

# 去 添加员工页面
    def go_to_add_stuff_page(self, base_url):
        publicPage = PublicPage(self.driver)
        self.driver.get(base_url + self.add_stuff_url)
        time.sleep(3)
        add_stuff_loc = self.driver.find_element_by_xpath(
            self.add_stuff_xpath)
        publicPage.is_element_present(add_stuff_loc)

# 去 员工导入页面
    def go_to_import_stuff_page(self, base_url):
        publicPage = PublicPage(self.driver)
        self.driver.get(base_url + self.import_stuff_url)
        time.sleep(3)
        import_stuff_loc = self.driver.find_element_by_xpath(
            self.import_stuff_xpath)
        publicPage.is_element_present(import_stuff_loc)

# 去 工资表页面
    def go_to_salary_list_page(self, base_url):
        publicPage = PublicPage(self.driver)
        self.driver.get(base_url + self.salary_list_url)
        time.sleep(3)
        salary_list_loc = self.driver.find_element_by_xpath(
            self.salary_list_xpath)
        publicPage.is_element_present(salary_list_loc)

# 去 劳务表页面
    def go_to_labour_list_page(self, base_url):
        publicPage = PublicPage(self.driver)
        self.driver.get(base_url + self.labour_list_url)
        time.sleep(3)
        labour_list_loc = self.driver.find_element_by_xpath(
            self.labour_list_xpath)
        publicPage.is_element_present(labour_list_loc)

# 去 工资发放记录页面
    def go_to_salary_record_page(self, base_url):
        publicPage = PublicPage(self.driver)
        self.driver.get(base_url + self.salary_record_url)
        time.sleep(3)
        salary_record_loc = self.driver.find_element_by_xpath(
            self.salary_record_xpath)
        publicPage.is_element_present(salary_record_loc)

# 去 劳务发放记录页面
    def go_to_labour_record_page(self, base_url):
        publicPage = PublicPage(self.driver)
        self.driver.get(base_url + self.labour_record_url)
        time.sleep(3)
        labour_record_loc = self.driver.find_element_by_xpath(
            self.labour_record_xpath)
        publicPage.is_element_present(labour_record_loc)
