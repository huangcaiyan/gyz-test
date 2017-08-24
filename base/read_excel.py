import xlrd
import xlwt
from datetime import date, datetime


class ReadExcel(object):
    def __init__(self, file_dir):
        self.file_dir = file_dir

# 获取整行内容
    def get_row_value(self, sheet_name, row_num):
        workbook = xlrd.open_workbook(self.file_dir)
        sheet = workbook.sheet_by_name(sheet_name)
        return sheet.row_values(row_num)

# 获取整列内容
    def get_col_value(self, sheet_name, col_num):
        workbook = xlrd.open_workbook(self.file_dir)
        sheet = workbook.sheet_by_name(sheet_name)
        return sheet.col_values(col_num)


# 获取单元格内容sheet_name：sheet名称;row_num:行次;col_num:列次;
    def get_cel_value(self, sheet_name, row_num, col_num):
        workbook = xlrd.open_workbook(self.file_dir)
        sheet = workbook.sheet_by_name(sheet_name)
        sheet_value = sheet.cell(row_num, col_num).value
        # return str(sheet_value).split('.')[0]
        return str(int(sheet_value))

# 获取所有sheets
    def get_sheets(self):
        workbook = xlrd.open_workbook(self.file_dir)
        return workbook.sheets()

# 顺序获取所有excel值
    def get_value_in_order(self, sheet_index):
        sheets = self.get_sheets()
        print(sheets)
        values = []
        s = sheets[sheet_index]
        print('s=',s)
        for row in range(s.nrows):
            if row != 0:
                col_value = []
                for col in range(s.ncols):
                    value = (str(s.cell(row, col).value))
                    col_value.append(value)
        print('values=>',values)
        print('values=>',values[2])
        return values

    def get_value_in_order1(self, sheet_index):
        sheets = self.get_sheets()
        print(sheets)
        values = []
        s = sheets[sheet_index]
        print('s=',s)
        for row in range(s.nrows):
            if row != 0:            
                raw_value = s.row_values(row)
                values.append(raw_value)
        print('values=>',values)
        print('values=>',values[2])
        return values

    def get_array(self, sheet_index):
        values = self.get_value_in_order(self, sheet_index)
        v_len = values.__len__
        for array in range(v_len):
            print (array)


# 获取excel sheet 名称
    def get_sheet_name(self):
        workbook = xlrd.open_workbook(self.file_dir)
        names = workbook.sheet_names()
        return names

    def go_to_sheet_page(self, sheet_num):
        workbook = xlrd.open_workbook(self.file_dir)
        names = workbook.sheet_names()
        return names[sheet_num]

    def go_to_sheet_page1(self, sheet_num):
        workbook = xlrd.open_workbook(self.file_dir)
        sheet = workbook.sheet_by_index(sheet_num)
        return sheet

    def go_to_sheet_page2(self, sheet_name):
        workbook = xlrd.open_workbook(self.file_dir)
        sheet = workbook.sheet_by_name(sheet_name)
        return sheet
