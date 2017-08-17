from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import time
import random
import logging
# from selenium import webdriver


class PublicPage:

 # location
    pre_button_xpath = '//*[@id="ui-datepicker-div"]/div/a[1]'
    next_button_xpath = '//*[@id="ui-datepicker-div"]/div/a[2]'

    def __init__(self, driver):
        self.driver = driver

 # 判断元素是否显示
    def is_element_present(self, elem_loc):
        try:
            self.driver.find_element_by_xpath(elem_loc)
        except NoSuchElementException as e:
            return e
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
    def select_date(self, calen_xpath, day):
        self.driver.find_element_by_xpath(calen_xpath).click()
        pre_button = self.driver.find_element_by_xpath(self.pre_button_xpath)
        next_button = self.driver.find_element_by_xpath(self.next_button_xpath)
        time.sleep(2)
        if pre_button:
            return self.driver.find_element_by_link_text(day).click()
        else:
            return False
# 删除日历
    def delete_date(self):
        del_loc = self.driver.find_element_by_css_selector('.fa-remove')
        self.scroll_to_elem(del_loc)
        return del_loc.click()

# 随机数
    def random_num(self, num):
        return random.randrange(0, num)

# 点击事件
    def click_elem(self, elem_loc):
        return elem_loc.click()

# 将光标定位到元素处
    def scroll_to_elem(self, elem_loc):
        return self.driver.execute_script('arguments[0].scrollIntoView();', elem_loc)


# 将光标定位到页面顶部
    def scroll_to_top(self):
        return self.driver.execute_script('scroll(0,-250)')

# 将光标定位到页面底部
    def scroll_to_bottom(self):
        return self.driver.execute_script('scroll(0,document.body.scrollHeight)')
        # return self.driver.execute_script('scroll(0,-250)')

# 选择下拉项
    def select_dropdown_item(self, drop_loc, item_name):
        drop_loc.click()
        time.sleep(1)
        itme_loc = self.driver.find_element_by_link_text(item_name)
        self.scroll_to_elem(itme_loc)
        return itme_loc.click()

# alet
    def get_alert_msg(self):
        alert_msg_array = []
        alert_loc = self.driver.find_element_by_tag_name('alert')
        alert_msg = alert_loc.text
        print('alert_msg type=>',alert_msg)
        alert_msg_array = alert_msg.spilt('\n')
        print('The alert message is ', alert_msg_array[2])
        close_loc = self.driver.find_element_by_css_selector('.close')
        close_loc.click()
        return alert_msg_array[2]

    def get_danger_msg(self):
        try:
            danger_loc = self.driver.find_element_by_css_selector(
                '.text-danger')
            self.scroll_to_elem(danger_loc)
            danger_msg = danger_loc.text
            print('The danger message is ', danger_msg)
            return danger_msg
        except Exception as e:
            logging.error('There are an exception %s', str(e))
