from selenium import webdriver
import time
import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../../'))
from test_case.setting.page.setting_page import SettingPage
from base.enter_comp_page import EnterCompPage
from config import Config
from base.public_page import PublicPage
from test_case.setting.page.comp_billing_page import CompBillingPage
from data.comp_billing_data import CompBillingData
from base.alert_page import AlertPage
from base.danger_page import DangerPage


class CompBillingSpec(unittest.TestCase):
    """
    帐套页面测试
    """
    billing_page_url = Config.BASE_URL + '/app/setting/company-billing'

    def setUp(self):
        """ 进入公司 """
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        enterCompPage = EnterCompPage(Config.BASE_URL, self.driver)
        enterCompPage.enter_comp(Config.ENTER_COMP_INFO)
        c_comp_name = enterCompPage.get_comp_name(Config.ENTER_COMP_INFO[1])
        if c_comp_name == Config.ENTER_COMP_INFO[1]:
            self.driver.get(self.billing_page_url)
            time.sleep(3)
            print('————————————进入公司成功 ！————————————')
        else:
            print('————————————进入公司失败 ！————————————')

    def test_edit_comp_info(self):
        """ 编辑帐套信息测试"""
        publicPage = PublicPage(self.driver)
        alertPage = AlertPage(self.driver)
        page = CompBillingPage(self.driver)
        page.modify_comp_info(CompBillingData.MODIFY_COMP_INFO)
        alertPage.get_alert_msg()
        comp_name = page.get_comp_name()
        self.assertEqual(comp_name, CompBillingData.MODIFY_COMP_INFO[0])
# 空校验
    def test_comp_name_empty(self):
        """ 编辑帐套－公司名不能为空"""
        publicPage = PublicPage(self.driver)
        dangerPage = DangerPage(self.driver)
        page = CompBillingPage(self.driver)
        page.click_edit()
        page.set_comp_name(' ')
        page.save()
        danger_msg = dangerPage.get_danger_msg()
        self.assertEqual(danger_msg, '请填写公司名称')

    def test_legal_person_name_empty(self):
        """ 编辑帐套－法定代表人不能为空"""
        publicPage = PublicPage(self.driver)
        dangerPage = DangerPage(self.driver)
        page = CompBillingPage(self.driver)
        page.click_edit()        
        page.set_legal_person_name('')
        page.save()
        danger_msg = dangerPage.get_danger_msg()
        self.assertEqual(danger_msg, '请填写法定代表人')

    def test_tax_num_empty(self):
        """ 编辑帐套－纳税人识别号不能为空"""
        publicPage = PublicPage(self.driver)
        dangerPage = DangerPage(self.driver)
        page = CompBillingPage(self.driver)
        page.click_edit()        
        page.set_tax_num('')
        page.save()
        danger_msg = dangerPage.get_danger_msg()
        self.assertEqual(danger_msg, '请填写纳税人识别号')

    def test_begin_date_empty(self):
        """ 编辑帐套－成立日期不能为空"""
        publicPage = PublicPage(self.driver)
        dangerPage = DangerPage(self.driver)
        page = CompBillingPage(self.driver)
        page.click_edit()        
        publicPage.delete_date()
        page.save()
        danger_msg = dangerPage.get_danger_msg()
        self.assertEqual(danger_msg, '请填写纳税人识别号')


    def tearDown(self):
        # page = CompBillingPage(self.driver)
        # compBillingData = CompBillingData()
        # page.modify_comp_info(compBillingData.RESET_COMP_INFO)
        self.driver.quit()


if __name__ == '_main_':
    unittest.main()
