from serviceable import Serviceable
from engines.engine import Engine
from batteries.battery import Battery

class Car(Serviceable) :
    
    def __init__(self, engine, battery):
        self.engine : Engine = engine
        self.battery : Battery = battery

    def needs_service(self):
        if (
            self.engine.needs_service() or 
            self.battery.needs_service()
            ) :
            return True
        else : 
            return False
    