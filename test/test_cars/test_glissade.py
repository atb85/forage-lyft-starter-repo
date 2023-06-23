from datetime import timedelta, datetime
import unittest

from car_factory import CarFactory

class TestGlissade(unittest.TestCase):
    def test_no_service_should_be_called(self) :
        glissade = CarFactory.create_glissade(datetime.now(), datetime.now() - timedelta(days=800), 59000, 0)
        self.assertEqual(glissade.needs_service(), False, "shouldn't need service")

    def test_battery_service(self) :
        glissade = CarFactory.create_glissade(datetime.now(), datetime.now() - timedelta(days= 1200), 0, 0)
        self.assertEqual(glissade.needs_service(), True, "should need service")

    def test_engine_service(self) :
        glissade = CarFactory.create_glissade(datetime.now(), datetime.now(), 61000, 0)
        self.assertEqual(glissade.needs_service(), True, "should need service")