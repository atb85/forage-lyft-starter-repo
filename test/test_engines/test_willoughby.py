import unittest

from components.engines.willoughby_engine import WilloughbyEngine

class TestWilloughby(unittest.TestCase) :
    
    def test_no_service(self) :
        eng = WilloughbyEngine(0, 59000)
        self.assertFalse(eng.needs_service())
    
    def test_needs_service(self) :
        eng = WilloughbyEngine(0, 60000)
        self.assertTrue(eng.needs_service())