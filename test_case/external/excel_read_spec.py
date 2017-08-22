from selenium import webdriver
import time
import unittest
from base.read_excel import ReadExcel


class ExcelReadSpec(unittest.TestCase):

    def setUp(self):
        pass

    def test_get_cel_value(self):
        readExcel = ReadExcel(
            '/Users/huangcaiyan/work/guanplus-test/data/login_data.xlsx')
        cell_value = readExcel.get_cel_value('sheet1', 1, 0)
        print (cell_value)

    def test_get_value_in_order(self):
        readExcel = ReadExcel(
            '/Users/huangcaiyan/work/guanplus-test/data/login_data.xlsx')
        values = readExcel.get_value_in_order(1)
        print(values)

    def test(self):
        readExcel = ReadExcel(
            '/Users/huangcaiyan/work/guanplus-test/data/login_data.xlsx')
        names = readExcel.get_sheet_name()
        sheet_1 = readExcel.go_to_sheet_page(0)
        sheet_2= readExcel.go_to_sheet_page1(0)
        sheet_3 = readExcel.go_to_sheet_page2('sheet2')
        
        
        
        print(names)
        print(sheet_1)
        print(sheet_2)
        print(sheet_3)
        
        
        

    def tearDown(self):
        pass


if __name__ == '_main_':
    unittest.main()
