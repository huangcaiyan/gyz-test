from selenium import webdriver
import time
from public_page import PublicPage
from test_case.login.login_page import LoginPage


class EnterCompPage:
    publicPage = PublicPage(self.driver)
    loginPage = LoginPage(self.driver,self.url)

    # location
    create_comp_xpath = '//*[@id="body"]/company-list/div[1]/div[3]/div[2]/button[1]'

    
    def __init__(self,driver):
        # self.driver = driver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(ENTER_COMP_INFO[0])
        self.enter_comp(ENTER_COMP_INFO[1])

    # comp_name 公司名称
    def click_comp_name(comp_name):
        self.driver.find_element_by_link_text(comp_name)
        enter_status = self.publicPage.is_element_present(self.create_comp_xpath)
        if enter_status:
            print ('————————————进入公司失败 ！————————————')
            exit()

    # comp_json 用户名、密码、公司名
    def enter_comp(self,ENTER_COMP_INFO):
        self.loginPage.login(ENTER_COMP_INFO[0])
        self.username= self.loginPage.username_id
        login_status = self.publicPage.is_element_present(self.username)
        if login_status:
            print '————————————登录失败 ！————————————'
        else:
            self.click_comp_name(comp_json[2])
            
       

      
        
        
        
