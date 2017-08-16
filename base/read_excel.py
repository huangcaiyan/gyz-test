import xlrd
import xlwt
from datetime import date, datetime


class ReadExcel(object):
    def __init__(self,file_dir):
        self.file_dir = file_dir

# 获取整行内容
    def get_row_value(self,file_dir,sheet_name,row_num):
        workbook = xlrd.open_workbook(file_dir)
        sheet = workbook.sheet_by_name(sheet_name)
        return sheet.row_values(row_num)

# 获取整列内容
    def get_col_value(self,file_dir,sheet_name,col_num):
        workbook = xlrd.open_workbook(file_dir)
        sheet = workbook.sheet_by_name(sheet_name)
        return sheet.col_values(col_num)

# 获取单元格内容
    def get_cel_value(self,file_dir,sheet_name,row_num,col_num):
        workbook = xlrd.open_workbook(file_dir)
        sheet = workbook.sheet_name(sheet_name)
        return sheet.cell(row_num,col_num).value


   

