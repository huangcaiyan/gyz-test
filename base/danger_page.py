from base.public_page import PublicPage
from selenium import webdriver
from config import Config


class DangerPage:
    # class 为 text_danger
    text_danger_msg_elem = '.text-danger'
    # class 为 alert_danger
    alert_danger_msg_elem = '.alert_danger'

    alert_msgs = []

    def __init__(self, driver):
        self.driver = driver
        self.driver = webdriver.Chrome()

# alert 框danger提示内容
    def get_alert_danger_msg(self):
        publicPage = PublicPage(self.driver)
        alert_danger_msg_loc = self.driver.find_element_by_class_name(
            self.alert_danger_msg_elem)
        publicPage.is_element_present(alert_danger_msg_loc)
        alert_danger_msg = self.alert_danger_msg_loc.text
        print('The alert danger message is ', alert_danger_msg)
        return alert_danger_msg

# 输入框下警示文字
    def get_text_danger_msg(self):
        publicPage = PublicPage(self.driver)
        text_danger_msg_loc = self.driver.find_element_by_css_selector(
            self.text_danger_msg_elem)
        publicPage.is_element_present(text_danger_msg_loc)
        text_danger_msg = self.text_danger_msg_loc.text
        print('The text danger message is ', text_danger_msg)
        return text_danger_msg




        
        

