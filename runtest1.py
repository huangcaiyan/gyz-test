import unittest,time
from HTMLTestRunner import HTMLTestRunner

test_dir = './test_case/spec'
def createsuite():
    testunit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(test_dir,pattern='*_spec.py')
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTest(test_case)
            print(testunit)
    return testunit

now = time.strftime("%Y-%m-%d %H_%M_%S")
filename = './report/'+now + '_result.html'
fp = open(filename,'wb')

runner = HTMLTestRunner(stream=fp,title=u'测试报告',description=u'用例执行情况：')
runner.run(createsuite())
fp.close()