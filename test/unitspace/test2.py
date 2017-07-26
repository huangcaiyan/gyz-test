from calculator import Count
import unittest

class TestCount(unittest.TestCase):
    
    def setUp(self):
        print ('Test start!')

    def test_add(self):
        j = Count(2,3)
        self.assertEqual(j.add(),5)

    def tearDown(self):
        print ('Test end!')

if __name__== '_main_':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(TestCount('test_add'))

    runner = unittest.TextTestRunner()
    runner.run(suite)
    # suite = unittest.TestLoader().loadTestsFromTestCase(TestCount)
    # test_result = unittest.TextTestRunner(verbosity=2).run(suite)
    # print('All case number')
    # print(test_result.testsRun)
    # print('Failed case number')
    # print(len(test_result.failures))
    # print('Failed case and reason')
    # print(test_result.failures)
    # for case, reason in test_result.failures:
    #     print case.id()
    #     print reason
