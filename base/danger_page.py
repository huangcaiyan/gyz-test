from base.public_page import PublicPage
from selenium import webdriver
from config import Config
class DangerPage:
    # class name为 text_danger
    text_danger_msg_elem= 'text-danger'
    # class 为 alert_danger
    alert_danger_msg_elem = '.alert_danger'

    alert_msgs = []

    def __init__(self,driver):
        self.driver = driver
        # self.driver= webdriver.Chrome()

    def get_danger_msg(self):
        publicPage = PublicPage(self.driver)
        login_url = Config.BASE_URL + '/login'
        if self.driver.current_url == login_url:
            danger_msg_elem = self.driver.find_element_by_css_selector(self.alert_danger_msg_elem)
        else:
            danger_msg_elem = self.driver.find_element_by_class_name(self.text_danger_msg_elem)
        publicPage.is_element_present(danger_msg_elem)
        alert_msg = self.danger_msg_elem.text
        print('The danger message is ',alert_msg)
        return alert_msg
            
            
    