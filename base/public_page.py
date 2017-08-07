from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

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
            self.driver.get_element_by_xpath(elem_loc)
        except NoSuchElementException as e:
            return '————————————未找到元素不存在 ！————————————'
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
    def select_date(self, day):
        pre_button = self.driver.find_element_by_xpath(self.pre_button_xpath)
        next_button = self.driver.find_element_by_xpath(self.next_button_xpath)
        if pre_button:
            return self.driver.find_element_by_link_text(day).click()
        else:
            return '————————————选择日历失败 ！———————————— '

    # 下拉选择
    def select_dropdown_item(self, item_name):
        try:
            item_link_text_loc = self.driver.find_element_by_link_text(
                itme_name)
            if item_link_text_loc:
                return item_link_text_loc.click()
            else:
                return '————————————下拉选择失败 ！————————————'
