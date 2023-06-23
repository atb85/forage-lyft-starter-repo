import unittest

from datetime import datetime
from datetime import timedelta

from car_factory import CarFactory


class TestCalliope(unittest.TestCase) :
    def test_no_service_should_be_called(self) :
        calliope = CarFactory.create_calliope(datetime.now(), datetime.now() - timedelta(days=500), 29000, 0)
        self.assertEqual(calliope.needs_service(), False, "shouldn't need service")

    def test_battery_service(self) :
        calliope = CarFactory.create_calliope(datetime.now(), datetime.now() - timedelta(days=800), 0, 0)
        self.assertEqual(calliope.needs_service(), True, "should need service")

    def test_engine_service(self) :
        calliope = CarFactory.create_calliope(datetime.now(), datetime.now(), 31000, 0)
        self.assertEqual(calliope.needs_service(), True, "should need service")

class TestGlissade(unittest.TestCase):
    def test_no_service_should_be_called(self) :
        glissade = CarFactory.create_glissade(datetime.now(), datetime.now() - timedelta(days=500), 59000, 0)
        self.assertEqual(glissade.needs_service(), False, "shouldn't need service")

    def test_battery_service(self) :
        glissade = CarFactory.create_glissade(datetime.now(), datetime.now() - timedelta(days= 800), 0, 0)
        self.assertEqual(glissade.needs_service(), True, "should need service")

    def test_engine_service(self) :
        glissade = CarFactory.create_glissade(datetime.now(), datetime.now(), 61000, 0)
        self.assertEqual(glissade.needs_service(), True, "should need service")

class TestPalindrome(unittest.TestCase):
    def test_no_service_should_be_called(self) :
        palindrome = CarFactory.create_palindrome(datetime.now(), datetime.now() - timedelta(days=500), False)
        self.assertEqual(palindrome.needs_service(), False, "shouldn't need service")

    def test_battery_service(self) :
        palindrome = CarFactory.create_palindrome(datetime.now(), datetime.now() - timedelta(days=800), False)
        self.assertEqual(palindrome.needs_service(), True, "should need service")

    def test_engine_service(self) :
        palindrome = CarFactory.create_palindrome(datetime.now(), datetime.now(), True)
        self.assertEqual(palindrome.needs_service(), True, "should need service")

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

class TestThovex(unittest.TestCase):
    def test_no_service_should_be_called(self) :
        rorschach = CarFactory.create_rorschach(datetime.now(), datetime.now() - timedelta(days=1000), 29000, 0)
        self.assertEqual(rorschach.needs_service(), False, "shouldn't need service")

    def test_battery_service(self) :
        rorschach = CarFactory.create_rorschach(datetime.now(), datetime.now() - timedelta(days= 1600), 0, 0)
        self.assertEqual(rorschach.needs_service(), True, "should need service")

    def test_engine_service(self) :
        rorschach = CarFactory.create_rorschach(datetime.now(), datetime.now(), 61000, 0)
        self.assertEqual(rorschach.needs_service(), True, "should need service")


if __name__ == '__main__':
   unittest.main()
