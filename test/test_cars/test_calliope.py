from datetime import datetime, timedelta
import unittest

from car_factory import CarFactory


class TestCalliope(unittest.TestCase) :
    def test_no_service_should_be_called(self) :
        calliope = CarFactory.create_calliope(datetime.now(), datetime.now() - timedelta(days=800), 29000, 0)
        self.assertEqual(calliope.needs_service(), False, "shouldn't need service")

    def test_battery_service(self) :
        calliope = CarFactory.create_calliope(datetime.now(), datetime.now() - timedelta(days=1200), 0, 0)
        self.assertEqual(calliope.needs_service(), True, "should need service")

    def test_engine_service(self) :
        calliope = CarFactory.create_calliope(datetime.now(), datetime.now(), 31000, 0)
        self.assertEqual(calliope.needs_service(), True, "should need service")