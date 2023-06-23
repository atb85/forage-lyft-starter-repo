import unittest

from datetime import datetime, timedelta

from car_factory import CarFactory

class TestRorschach(unittest.TestCase):
    def test_no_service_should_be_called(self) :
        rorschach = CarFactory.create_rorschach(datetime.now(), datetime.now() - timedelta(days=1000), 59000, 0)
        self.assertEqual(rorschach.needs_service(), False, "shouldn't need service")

    def test_battery_service(self) :
        rorschach = CarFactory.create_rorschach(datetime.now(), datetime.now() - timedelta(days= 1600), 0, 0)
        self.assertEqual(rorschach.needs_service(), True, "should need service")

    def test_engine_service(self) :
        rorschach = CarFactory.create_rorschach(datetime.now(), datetime.now(), 61000, 0)
        self.assertEqual(rorschach.needs_service(), True, "should need service")