from selenium import webdriver
import time
from base.public_page import PublicPage
import logging


class CompBillingPage:

    # element loc
    # 编辑
    edit_xpath = '//*[@id="body"]/setting/div[2]/div/gpw-company-billing/div/div/span[2]/a'
# 公司名称
    comp_name_name = 'name'
    comp_name_text_id = 'companyName'
# 法定代表人
    legal_person_name_name = 'legalPersonName'
 # 注册资本
    registered_capital_name = 'registeredCapital'
# 省 下拉
    priv_dropdown_name = 'province'
# 市 下拉
    city_dropdown_name = 'city'
# 区 下拉
    dist_dropdown_name = 'district'
# 详细地址
    addr_input_name = 'address'
# 成立日期calender
    begin_date_calen_xpath = '//*[@id="form"]/div[5]/div/p-calendar'
    begin_date_dele_xpath = '//*[@id="form"]/div[5]/div[1]/p-calendar/span/span[1]'
# 纳税人识别号
    tax_number_name = 'taxNumber'
# 行业dropdown
    industry_dropdown_name = 'industry'
# 服务截止日期
    service_deadline_xpath = '//*[@id="form"]/div[10]/div/p-calendar/span/span[2]'
# 保存按钮
    save_css = '.btn-primary'
# 取消按钮
    cancel_css = '.btn-secondar'

    def __init__(self, driver):
        # self.driver = webdriver.Chrome()
        self.driver = driver

# 将光标移动刀元素处
    def billing_public(self, elem_loc):
        self.driver.execute_script('arguments[0].scrollIntoView();', elem_loc)

# 点击编辑
    def click_edit(self):
        try:
            publicPage = PublicPage(self.driver)
            edit_loc = self.driver.find_element_by_xpath(self.edit_xpath)
            publicPage.scroll_to_elem(edit_loc)
            return edit_loc.click()
        except Exception as e:
            logging.error('there was an exception %s', str(e))

# 设置公司名
    def set_comp_name(self, comp_name):
        try:
            comp_name_loc = self.driver.find_element_by_name(
                self.comp_name_name)
            comp_name_loc.clear()
            comp_name_loc.send_keys(comp_name)
            time.sleep(1)
        except Exception as e:
            logging.error('there was an exception %s', str(e))

# 获取公司名
    def get_comp_name(self):
        comp_name_loc = self.driver.find_element_by_id(self.comp_name_text_id)
        return comp_name_loc.text

# 法定代表人
    def set_legal_person_name(self, legal_person_name):
        try:
            legal_person_name_loc = self.driver.find_element_by_name(
                self.legal_person_name_name)
            legal_person_name_loc.clear()
            legal_person_name_loc.send_keys(legal_person_name)
            time.sleep(1)
        except Exception as e:
            logging.error('there was an exception %s', str(e))

# 注册资本
    def set_registered_capital(self, registered_num):
        try:
            registered_capital_loc = self.driver.find_element_by_name(
                self.registered_capital_name)
            registered_capital_loc.clear()
            registered_capital_loc.send_keys(registered_num)
            time.sleep(1)
        except Exception as e:
            logging.error('there was an exception %s', str(e))

# 省份
    def select_prov(self, prov_name):
        try:
            self.driver.find_element_by_name(self.priv_dropdown_name).click()
            prov_name_loc = self.driver.find_element_by_link_text(prov_name)
            publicPage = PublicPage(self.driver)
            publicPage.scroll_to_elem(prov_name_loc)
            time.sleep(1)
            return prov_name_loc.click()
        except Exception as e:
            logging.error('there was an exception %s', str(e))


# 市
    def select_city(self, city_name):
        try:
            self.driver.find_element_by_name(self.city_dropdown_name).click()
            city_name_loc = self.driver.find_element_by_link_text(city_name)
            publicPage = PublicPage(self.driver)
            publicPage.scroll_to_elem(city_name_loc)
            time.sleep(1)
            return city_name_loc.click()
        except Exception as e:
            logging.error('there was an exception %s', str(e))


# 区
    def select_distr(self, distr_name):
        try:
            self.driver.find_element_by_name(self.dist_dropdown_name).click()
            distr_name_loc = self.driver.find_element_by_link_text(distr_name)
            publicPage = PublicPage(self.driver)
            publicPage.scroll_to_elem(distr_name_loc)
            time.sleep(1)
            return distr_name_loc.click()
        except Exception as e:
            logging.error('there was an exception %s', str(e))


# 详细地址
    def set_address(self, address_name):
        try:
            publicPage = PublicPage(self.driver)
            address_name_loc = self.driver.find_element_by_name(
                self.addr_input_name)
            address_name_loc.clear()
            address_name_loc.send_keys(address_name)
        except Exception as e:
            logging.error('there was an exception %s', str(e))


# 成立日期
    def select_begin_date(self, day):
        try:
            publicPage = PublicPage(self.driver)
            publicPage.select_date(self.begin_date_calen_xpath, day)
            time.sleep(1)
        except Exception as e:
            logging.error('there was an exception %s', str(e))

# 删除成立日期
    def dele_begin_date(self):
        try:
            publicPage = PublicPage(self.driver)
            date_loc = self.driver.find_element_by_xpath(
                self.begin_date_dele_xpath)
            publicPage.scroll_to_elem(date_loc)
            date_loc.click()
        except Exception as e:
            logging.error('There was an exception %s', str(e))

# 纳税人识别号
    def set_tax_num(self, num):
        try:
            tax_num_loc = self.driver.find_element_by_name(
                self.tax_number_name)
            tax_num_loc.clear()
            tax_num_loc.send_keys(num)
            time.sleep(1)
        except Exception as e:
            logging.error('there was an exception %s', str(e))

# 行业
    def select_industry(self, indus_name):
        try:
            publicPage = PublicPage(self.driver)
            indust_loc = self.driver.find_element_by_name(
                self.industry_dropdown_name)
            publicPage.select_dropdown_item(indust_loc, indus_name)
            time.sleep(1)
        except Exception as e:
            logging.error('there was an exception %s', str(e))

# 服务截止日期
    def select_service_deadline(self, day):
        try:
            publicPage = PublicPage(self.driver)
            publicPage.select_date(self.service_deadline_xpath, day)
            time.sleep(1)
        except Exception as e:
            logging.error('there was an exception %s', str(e))

# 保存
    def save(self):
        try:
            publicPage = PublicPage(self.driver)
            save_button = self.driver.find_element_by_css_selector(
                self.save_css)
            publicPage.scroll_to_elem(save_button)
            return save_button.click()
        except Exception as e:
            logging.error('there was an exception %s', str(e))

# 取消
    def cancel(self):
        try:
            publicPage = PublicPage(self.driver)
            cancel_button = self.driver.find_element_by_css_selector(
                self.cancel_css)
            publicPage.scroll_to_elem(cancel_button)
            return cancel_button.click()
        except Exception as e:
            logging.error('there was an exception %s', str(e))

# 修改公司信息
    def modify_comp_info(self, comp_info):
        self.click_edit()
        time.sleep(2)
        self.set_comp_name(comp_info[0])
        self.set_legal_person_name(comp_info[1])
        self.set_registered_capital(comp_info[2])
        self.select_prov(comp_info[3])
        self.select_city(comp_info[4])
        self.select_distr(comp_info[5])
        self.set_address(comp_info[6])
        self.select_begin_date(comp_info[7])
        self.set_tax_num(comp_info[8])
        self.select_industry(comp_info[9])
        self.select_service_deadline(comp_info[10])
        self.save()
        time.sleep(2)
