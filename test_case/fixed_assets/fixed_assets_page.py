from selenium import webdriver
import time
from base.public_page import PublicPage
from config import Config


# 记录固定资产
# 创建于2017-8-28-二
class FixedAssetsPage(object):
    # 页面公用xpath
    base_xpath = '//*[@id="body"]/app-assets-tab/app-'

    # fixed_type(fixed:固定资产,intangible:无形资产)
    def __init__(self, driver, fixed_type):
        # self.driver = webdriver.Chrome()
        self.driver = driver
        self.fixed_type = fixed_type

    # 去记固定／无形资产页面
    def go_to_record_page(self):
        page_url = Config.BASE_URL + '/app/fixed-assets/detail/' + self.fixed_type
        self.driver.get(page_url)
        time.sleep(3)

    # 去固定资产列表页面
    def go_to_fixed_list_page(self):
        page_url = Config.BASE_URL + '/app/fixed-assets/list'
        self.driver.get(page_url)
        time.sleep(3)        

    # 去无形资产列表页面
    def go_to_intangible_list_page(self):
        page_url = Config.BASE_URL + '/app/fixed-assets/intangible-list'
        self.driver.get(page_url)
        time.sleep(3)        

    # 选择发票类型
    # fixed_type(fixed:固定资产,intangible:无形资产)
    def select_invoice_type(self, invoice_type_name):
        try:
            publicPage = PublicPage(self.driver)
            drop_elem = self.base_xpath + self.fixed_type + '/div/div[2]/div[1]/div[2]/div/ng-select'
            drop_loc = self.driver.find_element_by_xpath(drop_elem)
            publicPage.select_dropdown_item(drop_loc, invoice_type_name)
        except Exception as e:
            print(
                '[FixedAssetsPage] There was an exception when select_invoice_type %s',
                str(e))

    # 选择部门性质
    # department:部门名称
    def select_department(self, department):
        try:
            publicPage = PublicPage(self.driver)
            drop_elem = self.base_xpath+ self.fixed_type + '/div/div[2]/div[1]/div[3]/div/ng-select'
            drop_loc = self.driver.find_element_by_xpath(drop_elem)
            publicPage.select_dropdown_item(depart_drop_elem)
        except Exception as e:
            print(
                '[FixedAssetsPage] There was an exception when select_department %s',
                str(e))

    # 选择对方信息
    # contact：往来名称
    def select_contact(self, contact):
        try:
            publicPage = PublicPage(self.driver)
            drop_elem = self.base_xpath+self.fixed_type+'/div/div[2]/div[1]/div[4]/div/ng-select'
            drop_loc = self.driver.find_element_by_xpath(drop_elem)
            publicPage.select_dropdown_item(drop_loc, contact)
        except Exception as e:
            print(
                '[FixedAssetsPage] There was an exception when select_contact %s',
                str(e))

    # 收支发票号
    # invoice_num：发票号
    def set_invoice_num(self,invoice_num):
        try:
            publicPage = PublicPage(self.driver)
            input_elem = self.base_xpath+self.fixed_type+'/div/div[2]/div[2]/div[1]/div/input'
            input_loc = self.driver.find_element_by_xpath(input_elem)
            publicPage.set_value(invoice_num_loc,invoice_num)
        except Exception as e:
            print('[FixedAssetsPage] There was an exception when set_invoice_type %s',str(e))

    # 税率
    # tax：税率
    def select_tax(self,tax):
        try:
            publicPage = PublicPage(self.driver)
            drop_elem = self.base_xpath+self.fixed_type+'/div/div[2]/div[2]/div[2]/div/ng-select'
            drop_loc = self.driver.find_element_by_xpath(drop_elem)
            publicPage.select_dropdown_item(drop_loc,tax)
        except Exception as e:
            print('[FixedAssetsPage] There was an exception when select_tax %s',str(e))

    def select_input_tax_category(self,input_tax_category):
        try:
            publicPage = PublicPage(self.driver)
            drop_elem = self.base_xpath+self.fixed_type+'/div/div[2]/div[2]/div[3]/div/ng-select'
            drop_loc = self.driver.find_element_by_xpath(drop_elem)
            publicPage.select_dropdown_item(drop_elem,input_tax_category)
        except Exception as e:
            print('[FixedAssetsPage] There was an exception when select_input_tax_category %s',str(e))
    # 名称
    def set_name(self, name):
        try:
            publicPage = PublicPage(self.driver)
            input_elem = self.base_xpath+self.fixed_type+'/div/div[2]/div[3]/div/table/tbody/tr/td[1]/div/input'
            input_loc = self.driver.find_element_by_xpath(input_elem)
            publicPage.set_value(input_loc, name)
        except Exception as e:
            print(
                '[FixedAssetsPage] There was an exception when set_fixed_name %s',
                str(e))

    # 选择分类
    def select_fixed_type(self):
        try:
            publicPage = PublicPage(self.driver)
            drop_elem = self.base_xpath+self.fixed_type+'/div/div[2]/div[3]/div/table/tbody/tr/td[2]/ng-select'
            drop_loc = self.driver.find_element_by_xpath(drop_elem)
            publicPage.select_dropdown_item(drop_loc,fixed_type)
        except Exception as e:
            print(
                '[FixedAssetsPage] There was an exception when select_fixed_type %s',
                str(e))

    # 数量
    def set_num(self, num):
        try:
            publicPage = PublicPage(self.driver)
            input_elem = self.base_xpath+self.fixed_type+'/div/div[2]/div[3]/div/table/tbody/tr/td[3]/input'
            input_loc = self.driver.find_element_by_xpath(input_elem)
            publicPage.set_value(input_loc,num)
        except Exception as e:
            print(
                '[FixedAssetsPage] There was an exception when set_fixed_num %s',
                str(e))

    # 总金额
    def set_sum(self, sum):
        try:
            publicPage = PublicPage(self.driver)
            input_elem = self.base_xpath+self.fixed_type+'/div/div[2]/div[3]/div/table/tbody/tr/td[4]/ng2-numeric-input/div/div[1]/input[1]'
            input_loc = self.driver.find_element_by_xpath(input_elem)
            publicPage.set_value(input_loc, sum)
        except Exception as e:
            print(
                '[FixedAssetsPage] There was an exception when set_fixed_sum %s',
                str(e))

    # 备注
    def set_attach(self, attach):
        try:
            publicPage = PublicPage(self)
            input_elem = self.base_xpath+self.fixed_type+'/div/div[2]/div[3]/div/table/tbody/tr/td[5]/input'
            input_loc = self.driver.find_element_by_xpath(input_elem)
            publicPage.set_value(input_loc, attach)
        except Exception as e:
            print(
                '[FixedAssetsPage] There was an exception when set_fixed_attach %s',
                str(e))

    def save_and_new(self):
        try:
            publicPage = PublicPage(self.driver)
            btn_elem = self.base_xpath+self.fixed_type+'/div/div[2]/div[8]/div/span/button[1]'
            btn_loc = self.driver.find_element_by_xpath(btn_elem)
            publicPage.click_elem(btn_loc)
        except Exception as e:
            print(
                '[FixedAssetsPage] There was an exception when save_and_new %s',
                str(e))

    def save(self):
        try:
            publicPage = PublicPage(self.driver)
            btn_elem = self.base_xpath+self.fixed_type+'/div/div[2]/div[8]/div/span/button[2]'
            btn_loc = self.driver.find_element_by_xpath(btn_elem)
            publicPage.click_elem(btn_loc)
        except Exception as e:
            print(
                '[FixedAssetsPage] There was an exception when fixed_save %s',
                str(e))

    def cancel(self):
        try:
            publicPage = PublicPage(self.driver)
            btn_elem = self.base_xpath+self.fixed_type+'/div/div[2]/div[8]/div/span/button[3]'
            btn_loc = self.driver.find_element_by_xpath(btn_elem)
            publicPage.click_elem(btn_loc)

        except Exception as e:
             print(
                '[FixedAssetsPage] There was an exception when fixed_save %s',
                str(e))
