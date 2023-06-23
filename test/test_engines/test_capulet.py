import unittest

from components.engines.capulet_engine import CapuletEngine

class TestCapulet(unittest.TestCase) :
    
    def test_no_service(self) :
        eng = CapuletEngine(0, 29000)
        self.assertFalse(eng.needs_service())
    
    def test_needs_service(self) :
        eng = CapuletEngine(0, 30000)
        self.assertTrue(eng.needs_service())