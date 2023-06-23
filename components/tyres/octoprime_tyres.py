from components.tyres.tyres import Tyres

class OctoprimeTyres(Tyres) :
    
    def __init__(self, wear) :
        self.wear : list[int] = wear

    def needs_service(self) :
        return sum(self.wear) >= 3.0