category_index = [0, 1]
input_invoice_general_data = [
    '普票',
    '(个)其他',
    category_index,
    '销售部门',
    '1.5%',
    '123',
    '普票－其他－劳务费－1.5%'
]

output_invoice_data = [
    '普票',
    '税控自开',
    '(个)内部代表',
    '00000010',
    [0, 0],
    '管理部门',
    '17%',
    '234',
    '普票－内部代表－商品销售－17%'
]

input_invoice_special_data = [
    '专票',
    '(个)其他',
    '00000020',
    [0, 0],
    '管理部门',
    '5%',
    '其他',
    '345',
    '专票－其他－福利费－5%'
]
