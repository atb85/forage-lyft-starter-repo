from components.tyres.tyres import Tyres

class CarriganTyres(Tyres) :
    
    def __init__(self, wear) :
        self.wear : list[int] = wear

    def needs_service(self) :
        for wear_val in self.wear :
            if wear_val >= 0.9 :
                return True
        return False