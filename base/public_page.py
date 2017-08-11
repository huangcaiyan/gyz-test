from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import time
import random
# from selenium import webdriver


class PublicPage:

    # location
    pre_button_xpath = '//*[@id="ui-datepicker-div"]/div/a[1]/span'
    next_button_xpath = '//*[@id="ui-datepicker-div"]/div/a[2]/span'

    def __init__(self, driver):
        self.driver = driver

    # 判断元素是否显示
    def is_element_present(self, elem_loc):
        try:
            self.driver.find_element_by_xpath(elem_loc)
        except NoSuchElementException as e:
            return False
        return True

    # 判断alert框是否出现
    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    # 关闭alert框，且获取alert内容
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    # 日历
    def select_date(self,calen_xpath, day):
        pre_button = self.driver.find_element_by_xpath(self.pre_button_xpath)
        next_button = self.driver.find_element_by_xpath(self.next_button_xpath)
        self.driver.find_element_by_xpath(calen_xpath).click()
        time.sleep(2)
        if pre_button:
            return self.driver.find_element_by_link_text(day).click()
        else:
            return False

    # 随机数
    def random_num(self,num):
        return random.randrange(0,num)

    # 点击事件
    def click_elem(self,elem_loc):
        elem_loc.click()

        
        



