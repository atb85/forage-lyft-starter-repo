from datetime import datetime, timedelta
import unittest

from car_factory import CarFactory

class TestPalindrome(unittest.TestCase):
    def test_no_service_should_be_called(self) :
        palindrome = CarFactory.create_palindrome(datetime.now(), datetime.now() - timedelta(days=800), False)
        self.assertEqual(palindrome.needs_service(), False, "shouldn't need service")

    def test_battery_service(self) :
        palindrome = CarFactory.create_palindrome(datetime.now(), datetime.now() - timedelta(days=1200), False)
        self.assertEqual(palindrome.needs_service(), True, "should need service")

    def test_engine_service(self) :
        palindrome = CarFactory.create_palindrome(datetime.now(), datetime.now(), True)
        self.assertEqual(palindrome.needs_service(), True, "should need service")