from base.public_page import PublicPage
class DangerPage:
    danger_msg_classname = 'text-danger'
    alert_msgs = []

    def __init__(self,driver):
        self.driver = driver

    def get_danger_msg(self):
        publicPage = PublicPage(self.driver)
        danger_msg_elem = self.driver.find_element_by_class_name(self.danger_msg_classname)
        publicPage.is_element_present(danger_msg_elem)
        alert_msg = self.danger_msg_elem.text
        print('The danger message is ',alert_msg)
        return alert_msg



