import unittest

from components.engines.sternman_engine import SternmanEngine

class TestSternman(unittest.TestCase) :
    
    def test_no_service(self) :
        eng = SternmanEngine(False)
        self.assertFalse(eng.needs_service())

    def test_service(self) :
        eng = SternmanEngine(True) 
        self.assertTrue(eng.needs_service())