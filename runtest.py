import unittest,time
from HTMLTestRunner import HTMLTestRunner
from test_case.login.login_spec import LoginSpec

if __name__ == '__main__':
    testSuite = unittest.TestSuite()
    # testSuite.addTest(LoginSpec('test_login'))
    # testSuite.addTest(LoginSpec('test_login1'))
    # testSuite.addTest(LoginSpec('test_login2'))
    testSuite.addTest(LoginSpec('test_login3'))
    testSuite.addTest(LoginSpec('test_login4'))
    testSuite.addTest(LoginSpec('test_login5'))
    
    
    


    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './report/' + now + '_result.html'
    testReport = open(filename,'wb')
    runner = HTMLTestRunner(stream = testReport,title = "管有账测试报告",description='测试用例执行情况：')
    runner.run(testSuite)
    testReport.close()



