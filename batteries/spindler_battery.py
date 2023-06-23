from datetime import date
from datetime import timedelta

from batteries.battery import Battery

class SpindlerBattery(Battery) :
    def __init__(self, last_service_date, current_date) :
        self.last_service_date : date = last_service_date
        self.current_date : date = current_date

    def needs_service(self):
        date_diff : timedelta = self.current_date - self.last_service_date
        return (date_diff.days >= 365*2)