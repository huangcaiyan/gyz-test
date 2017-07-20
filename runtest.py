import unittest
_star_dir = './'
discover = unittest.defaultTestLoader.discover(start_dir = star_dir,pattern='test*.py',top_level_dir=None)

if __name__=='_main_':
    runner =unittest.TextTestRunner()
    runner.run(discover)