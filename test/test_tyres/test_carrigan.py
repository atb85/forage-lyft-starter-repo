import unittest

from components.tyres.carrigan_tyres import CarriganTyres

class TestCarrigan(unittest.TestCase) :
    
    def test_should_not_need_service(self) : 
        tyres = CarriganTyres([0.8 ,0.8 ,0.8 ,0.8])
        self.assertFalse(tyres.needs_service())
    
    def test_should_need_service(self) :
        tyres = CarriganTyres([0, 0, 0.91, 0])
        self.assertTrue(tyres.needs_service())
