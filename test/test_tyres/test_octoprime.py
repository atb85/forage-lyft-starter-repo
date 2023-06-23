import unittest

from components.tyres.octoprime_tyres import OctoprimeTyres


class TestCarrigan(unittest.TestCase) :
    
    def test_should_not_need_service(self) : 
        tyres = OctoprimeTyres([1, 1, 0.9, 0])
        self.assertFalse(tyres.needs_service())
    
    def test_should_need_service(self) :
        tyres = OctoprimeTyres([0.9, 0.9, 0.9, 0.4])
        self.assertTrue(tyres.needs_service())