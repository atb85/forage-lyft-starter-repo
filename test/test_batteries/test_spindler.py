import unittest

from datetime import datetime

from components.batteries.spindler_battery import SpindlerBattery

class TestSpindler(unittest.TestCase) :
    
    def test_no_service(self) :
        bat = SpindlerBattery(datetime.now(), datetime.now())
        self.assertFalse(bat.needs_service())

    def test_service(self) :
        bat = SpindlerBattery(datetime.fromisoformat("2000-01-01"), datetime.fromisoformat("2003-01-02"))
        self.assertTrue(bat.needs_service())