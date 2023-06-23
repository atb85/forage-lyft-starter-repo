from components.batteries.battery import Battery


class NubbinBattery(Battery) :
    def __init__(self, last_service_date, current_date) :
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        date_difference = self.current_date - self.last_service_date
        return (date_difference.days >= 365*4)