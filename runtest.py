import unittest
import time
from HTMLTestRunner import HTMLTestRunner
from test_case.login.login_spec import LoginSpec
# from test_case.invoice.record_input_invoice_spec import RecordInputInvoiceSpec
# from test_case.external.enter_comp_spec import EnterCompSpec
# from test_case.external.comp_list_spec import CompListSpec
from test_case.setting.spec.comp_billing_spec import CompBillingSpec
from test_case.salary.salary_spec import SalarySpec
from test_case.salary.stuff_list_spec import StuffListSpec 
from test_case.invoice.input_invoice_spec import InputInvoiceSpec
from test_case.external.read_excel_spec import ReadExcelSpec
from test_case.external.upload_file_spec import UploadFileSpec
from test_case.external.beginning_period.beginning_period_spec import BeginningPeriodSpec 
from test_case.invoice.output_invoice_spec import OutputInvoiceSpec 
from test_case.invoice.test import Test 
from test_case.fixed_assets.fixed_spec import FixedSpec 

if __name__ == '__main__':
    testSuite = unittest.TestSuite()
    # 登录页面测试
    # testSuite.addTest(LoginSpec('test_login'))
    # testSuite.addTest(LoginSpec('test_login1'))
    # testSuite.addTest(LoginSpec('test_login2'))
    # testSuite.addTest(LoginSpec('test_login3'))
    # testSuite.addTest(LoginSpec('test_login4'))
    # testSuite.addTest(LoginSpec('test_login5'))
    # testSuite.addTest(LoginSpec('test_excel_login'))

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
    # testSuite.addTest(StuffListSpec('test_import_stuff'))
    

    # 发票
    # 收票
    # testSuite.addTest(InputInvoiceSpec('test_record_input_invoice'))
    # testSuite.addTest(InputInvoiceSpec('test_output'))
    # testSuite.addTest(InputInvoiceSpec('test_type_input_invoice_special'))
    # testSuite.addTest(InputInvoiceSpec('test_new_raw'))
    # testSuite.addTest(InputInvoiceSpec('test'))
    # testSuite.addTest(Test('test_set_attach'))
    


    # 开票
    # testSuite.addTest(OutputInvoiceSpec('test_import_output_invoice'))

    # external
    # testSuite.addTest(ReadExcelSpec('test_get_cel_value'))
    # testSuite.addTest(ReadExcelSpec('test_get_value_in_order'))
    # testSuite.addTest(ReadExcelSpec('test'))
    # testSuite.addTest(UploadFileSpec('test_upload_file'))
    # testSuite.addTest(BeginningPeriodSpec('test_import_beginning_data'))
    # testSuite.addTest(BeginningPeriodSpec('test_distribute_bank'))
    
    # 固定资产
    # 记固定资产
    testSuite.addTest(FixedSpec('test_select_invoice_type'))


    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './report/' + now + '_result.html'
    testReport = open(filename, 'wb')
    runner = HTMLTestRunner(
        stream=testReport, title="管有账测试报告", description='测试用例执行情况：')
    runner.run(testSuite)
    testReport.close()
