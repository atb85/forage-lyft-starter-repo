import unittest

loader = unittest.TestLoader()
tests = loader.discover(start_dir="test", pattern="test_*.py")
unittest.TextTestRunner().run(tests)
