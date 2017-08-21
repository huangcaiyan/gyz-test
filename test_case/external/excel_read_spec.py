from selenium import webdriver
import time
import unittest
from base.read_excel import ReadExcel


class ExcelReadSpec(unittest.TestCase):

    def setUp(self):
        pass

    def test_get_cel_value(self):
        readExcel = ReadExcel('/Users/huangcaiyan/work/guanplus-test/data/login_data.xlsx')
        readExcel.get_cel_value('sheet1', 1, 0)
        print (str(readExcel.get_cel_value('sheet1', 1, 0)).split('.')[0])

    def tearDown(self):
        pass


if __name__ == '_main_':
    unittest.main()
