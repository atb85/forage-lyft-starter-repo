import unittest

from datetime import datetime

from components.batteries.nubbin_battery import NubbinBattery

class TestNubbin(unittest.TestCase) :
    
    def test_no_service(self) :
        bat = NubbinBattery(datetime.now(), datetime.now())
        self.assertFalse(bat.needs_service())

    def test_service(self) :
        bat = NubbinBattery(datetime.fromisoformat("2000-01-01"), datetime.fromisoformat("2004-01-02"))
        self.assertTrue(bat.needs_service())