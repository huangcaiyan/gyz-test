import time
from base.public_page import PublicPage


class SettingPage:
    # element loc
    # 页面url
    comp_billing_url = 'app/setting/company-billing'
    contact_url = '/app/setting/contact'
    mutil_user_url = '/app/setting/multi-user'
    partner_set_url = '/app/setting/partner-set'
    tax_rate_url = '/app/setting/tax-rate'
# 页面元素
    comp_billing_xpath = '//*[@id="body"]/setting/div[2]/div/gpw-company-billing/div/div/span[1]'
    contact_xpath = '//*[@id="addContactButton"]'
    multi_user_xpath = '//*[@id="body"]/setting/div[2]/div/gpw-multi-user/div/table/thead/tr/th[4]'
    partner_set_xpath = '//*[@id="body"]/setting/div[2]/div/app-partner-set/div[1]/div/button'
    tax_rate_xpath = '//*[@id="taxRatePage"]/span'

    def _init_(self, driver, setting_item):
        self.driver = driver
        self.setting_item = setting_item

# 去帐套信息页面（管理员角色）
    def go_to_setting_page(self, base_url):
        publicPage = PublicPage(self.driver)
        self.driver.get(base_url + self.comp_billing_url)
        time.sleep(3)
        comp_billing_loc = self.driver.find_element_by_xpath(
            self.comp_billing_xpath)

# 去往来信息页面
    def go_to_contact_page(self, base_url):
        publicPage = PublicPage(self.driver)
        self.driver.get(base_url + self.contact_url)
        time.sleep(3)
        add_loc = self.driver.find_element_by_xpath(self.contact_xpath)
        publicPage.is_element_present(add_loc)

# 去用户管理页面
    def go_to_mutil_user_page(self, base_url):
        publicPage = PublicPage(self.driver)
        self.driver.get(base_url + self.mutil_user_url)
        time.sleep(3)
        start_loc = self.driver.find_element_by_xpath(self.multi_user_xpath)
        publicPage.is_element_present(start_loc)

# 去股东页面
    def go_to_partner_set_page(self, base_url):
        publicPage = PublicPage(self.driver)
        self.driver.get(base_url + self.partner_set_url)
        time.sleep(3)
        add_loc = self.driver.find_element_by_xpath(self.partner_set_url)
        publicPage.is_element_present(start_loc)

# 去税率设置页面
    def go_to_tax_rete_page(self, base_url):
        publicPage = PublicPage(self.driver)
        self.driver.get(base_url + self.tax_rate_url)
        time.sleep(3)
        tax_loc = self.driver.find_element_by_xpath(self.tax_rate_url)
        publicPage.is_element_present(tax_loc)
