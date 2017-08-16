import xlrd
import xlwt
from datetime import date, datetime


def read_excel():
    # 打开文件
    workbook = xlrd.open_workbook(r'/Users/huangcaiyan/work/guanplus-test/data/login_data.xlsx')
    # 获取所有sheet
    print (workbook.sheet_names())  # [u'sheet1', u'sheet2']
    sheet1_name = workbook.sheet_names()[0]

    # 根据sheet索引或者名称获取sheet内容
    sheet1 = workbook.sheet_by_index(0)  # sheet索引从0开始
    sheet1 = workbook.sheet_by_name('sheet1')

    # sheet的名称，行数，列数
    print (sheet1.name, sheet1.nrows, sheet1.ncols)

    # 获取整行和整列的值（数组）
    rows = sheet1.row_values(1)  # 获取第二行内容
    cols = sheet1.col_values(0)  # 获取第一列内容
    print (rows)
    print (cols)

    # 获取单元格内容
    print (sheet1.cell(1, 0).value)
    print (sheet1.cell_value(1, 0))
    print (sheet1.row(1)[0].value)

    # 获取单元格内容的数据类型
    print (sheet1.cell(1, 0).ctype)


if __name__ == '__main__':
    read_excel()
