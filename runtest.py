import unittest
import time
from HTMLTestRunner import HTMLTestRunner
from test_case.login.login_spec import LoginSpec
# from test_case.invoice.record_input_invoice_spec import RecordInputInvoiceSpec
# from test_case.external.enter_comp_spec import EnterCompSpec
# from test_case.external.comp_list_spec import CompListSpec
from test_case.setting.spec.comp_billing_spec import CompBillingSpec
from test_case.salary.salary_spec import SalarySpec
# from test_case.invoice.input_invoice_spec import InputInvoiceSpec
from test_case.external.excel_read_spec import ExcelReadSpec
if __name__ == '__main__':
    testSuite = unittest.TestSuite()
    # 登录页面测试
    # testSuite.addTest(LoginSpec('test_login'))
    # testSuite.addTest(LoginSpec('test_login1'))
    # testSuite.addTest(LoginSpec('test_login2'))
    # testSuite.addTest(LoginSpec('test_login3'))
    # testSuite.addTest(LoginSpec('test_login4'))
    # testSuite.addTest(LoginSpec('test_login5'))

    # 进入公司测试
    # testSuite.addTest(EnterCompSpec('test_enter_comp'))

    # 帐套信息
    # testSuite.addTest(CompBillingSpec('test_edit_comp_info'))
    # testSuite.addTest(CompBillingSpec('test_comp_name_empty'))
    # testSuite.addTest(CompBillingSpec('test_legal_person_name_empty'))
    # testSuite.addTest(CompBillingSpec('test_tax_num_empty'))

    # 工资表
    # testSuite.addTest(SalarySpec('test_go_to_stuff_list_page'))
    # testSuite.addTest(SalarySpec('test_go_to_add_stuff_page'))
    # testSuite.addTest(SalarySpec('test_go_to_import_stuff_page'))
    # testSuite.addTest(SalarySpec('test_go_to_salary_list_page'))
    # testSuite.addTest(SalarySpec('test_go_to_labour_list_page'))
    # testSuite.addTest(SalarySpec('test_go_to_salary_record_page'))
    # testSuite.addTest(SalarySpec('test_go_to_labour_record_page'))

    # 发票
    # testSuite.addTest(InputInvoiceSpec('test_record_input_invoice'))

    # external
    testSuite.addTest(ExcelReadSpec('test_get_cel_value'))

    # testSuite.addTest(RecordInputInvoiceSpec('test1'))

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './report/' + now + '_result.html'
    testReport = open(filename, 'wb')
    runner = HTMLTestRunner(
        stream=testReport, title="管有账测试报告", description='测试用例执行情况：')
    runner.run(testSuite)
    testReport.close()
