from car import Car

from components.engines.capulet_engine import CapuletEngine
from components.engines.sternman_engine import SternmanEngine
from components.engines.willoughby_engine import WilloughbyEngine

from components.batteries.nubbin_battery import NubbinBattery
from components.batteries.spindler_battery import SpindlerBattery

class CarFactory :
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage) : 
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)
     
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage) : 
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(battery, engine)
    
    def create_palindrome(current_date, last_service_date, warning_light_on) : 
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)
    
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage) : 
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)
    
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage) : 
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)
    
    