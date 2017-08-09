import unittest,time
from HTMLTestRunner import HTMLTestRunner
# from test_case.login.login_spec import LoginSpec
# from test_case.invoice.record_input_invoice_spec import RecordInputInvoiceSpec
from test_case.external.comp_list_spec import CompListSpec 
from test_case.setting.spec.comp_billing_spec import CompBillingSpec
if __name__ == '__main__':
    testSuite = unittest.TestSuite()
    # testSuite.addTest(LoginSpec('test_login'))
    # testSuite.addTest(LoginSpec('test_login1'))
    # testSuite.addTest(LoginSpec('test_login2'))
    # testSuite.addTest(LoginSpec('test_login3'))
    # testSuite.addTest(LoginSpec('test_login4'))
    # testSuite.addTest(LoginSpec('test_login5'))
    # testSuite.addTest(CompListSpec('test_enter_comp1'))
    testSuite.addTest(CompBillingSpec('test_enter_comp'))
    

    # testSuite.addTest(RecordInputInvoiceSpec('test1'))
    
    
    
    
    


    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './report/' + now + '_result.html'
    testReport = open(filename,'wb')
    runner = HTMLTestRunner(stream = testReport,title = "管有账测试报告",description='测试用例执行情况：')
    runner.run(testSuite)
    testReport.close()



