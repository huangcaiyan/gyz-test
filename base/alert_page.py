from selenium import webdriver
class AlertPage:
    alert_msg_tagname = 'alert'    
    alert_info_array =[]
    
    def __init__(self,driver):
        self.driver = driver

    # 获取带alert标签的信息内容    
    def get_alert_msg(self):
        self.alert_msg_elem = self.driver.find_element_by_tag_name(self.alert_msg_tagname)
        self.alert_msg = self.alert_msg_elem.text
        alert_info_array = self.alert_msg.split('\n')
        print('the alert message is ',alert_info_array[2])
        return alert_info_array[2]

    
        
        






