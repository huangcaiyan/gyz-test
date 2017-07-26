import unittest
from module import Calculator

class ModuleTest(unittest.TestCase):

    def setUp(self):
        self.cal = Calculator(8,4)
        print 'test start!'
     
    def tearDown(self):
        pass
        
    
    def test_add(self):
        self.cal.add()
        self.assertEqual(result,12)

    def test_sub(self):
        self.cal.sub()
        self.assertEqual(result,5,msg='your answer is wrong!')

    def test_mul(self):
        self.cal.mul()
        self.assertEqual(result,32)

    def test_div(self):
        self.cal.div()
        self.assertEqual(result,2)

    if __name__=="_main_":
        unittest.main()
        # suite = unittest.TestSuite()
        # suite.addTest(ModuleTest("test_add"))
        # suite.addTest(ModuleTest("test_sub"))

        # runner = unittest.TextTestRunner()
        # runner.run(suite)