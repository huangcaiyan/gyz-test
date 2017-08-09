from selenium import webdriver

class CompBillingPage:
    edit_link_text = '编辑'
    comp_name_name = 'name'
    legal_person_name_name = 'legalPersonName'

    def __init__(self,driver):
        self.driver = webdriver.Chrome()
        self.driver = driver
        # location
        # 编辑
        edit_link_loc = self.driver.find_element_by_link_text('编辑')
        # 公司名称
        comp_name_loc = self.driver.find_element_by_name('name')
        # 法定代表人
        legal_person_name_loc = self.driver.find_element_by_name('legalPersonName')
        # 省 下拉
        priv_dropdown_loc = self.driver.find_element_by_name('province')
        # 市 下拉
        city_dropdown_loc = self.driver.find_element_by_name('city')
        # 区 下拉
        dist_dropdown_loc = self.driver.find_element_by_name('district')
        # self.driver.find_element_by_link_text(priv_name)
        # 详细地址
        addr_input_loc = self.driver.find_element_by_name('address')
        self.driver.find_element_by_name('taxNumber')
        # 性质下拉
        self.driver.find_element_by_name('industry')
        # 启用帐套日期
        self.driver.find_element_by_name('serviceDeadline')


