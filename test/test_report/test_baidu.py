# -*- coding:utf-8 -*- 
from selenium import webdriver
import unittest
from HTMLTestRunner import HTMLTestRunner
import time

class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url = 'http:www.baidu.com'
    def test_baidu_search(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id('kw').send_keys('HTMLTestRunner')
        driver.find_element_by_id('su').click()
    def tearDown(self):
        self.driver.quit()
if __name__=='_main_':
    testunit = unittest.TestSuite()
    testunit.addTest(Baidu('test_baidu_search'))

    # 按照一定格式获取当前时间
    now = time.strftime('%Y-%m-%d %H_%M_%S')

    # 定义报告存放路径
    filename = '/Users/huangcaiyan/work/guanplus-test/test/test_report/' + now + 'result.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,title='百度搜索测试报告',description='用例执行情况：')
    runner.run(testunit)
    fp.close()
