import xlwt
import xlrd
import unittest


class NameSpec(unittest.TestCase):

    def write_name(self):
        # 创建一个Wordbook对象，相当于创建了一个Excel文件
        book = xlwt.Workbook(encoding='utf-8')
        # 创建一个sheet对象，一个sheet对象对应Excel文件中的一张表格
        sheet = book.add_sheet('name_sheet', cell_overwrite_ok=True)
        # 向表sheet1中添加数据
        sheet.write(0, 0, 'englishname')
        sheet.write(1, 0, 'hcy')
        sheet.write(0, 1, '中文名')
        sheet.write(1, 1, '黄彩艳')

        # 最后，将以上操作保存到指定的Excel文件中
        book.save('./test_case/excel_read/name_data.xls')

    def test_name(self):
        # 打开指定路径中的xls文件，得到book对象
        xls_file = './test_case/excel_read/name_data.xls'
        # 打开指定文件
        book = xlrd.open_workbook(xls_file)
        # 通过sheet索引获得sheet对象
        sheet1 = book.sheet_by_index(0)
        # 获得指定索引的sheet名
        # sheet_name = book.sheet_names()[0]
        # print('sheet_name is ',sheet_name)
        # sheet1 = book.sheet_by_name(sheet_name)
        #  获得行数和列数
        # 总行数
        nrows = sheet1.nrows
        # 总列数
        ncols = sheet1.ncols
        # 遍历打印表中的内容
        for i in range(nrows):
            for j in range(ncols):
                cell_value = sheet1.cell_value(i, j)
                print(cell_value, end='\n')
            print(' ')
