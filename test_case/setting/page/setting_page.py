import time
from base.public_page import PublicPage


class SettingPage:

    # 元素定位
    base_url = 'https:firms.guanplus.com'
    comp_billing_linktext = '账套信息'
    
    publicPage = PublicPage()


    def _init_(self, driver, setting_item):
        self.driver = driver
        self.setting_item = setting_item

    # 去帐套信息页面（管理员角色）
    def go_to_setting_page(self, base_url):
        self.driver.get(self.base_url + 'app/setting/company-billing')
        time.sleep(5)
        comp_billing_elem = self.driver.find_element_by_link_text(self.comp_billing_linktext)
        # publicPage = PublicPage()
        self.publicPage.is_element_present(comp_billing_elem)

    # 去 帐套信息／往来信息／用户管理／股东／税率设置页面
    def go_to_setting_name_page(self, setting_name):
        self.driver.find_element_by_link_text(setting_name).click()
        time.sleep(2)
        self.publicPage.is_element_present(setting_name)

    def go_to_setting_item_page(self,item_url,item_name):
        self.driver.get(self.base_url + item_url)
        self.publicPage.is_element_present(item_name)



