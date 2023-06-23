from abc import ABC, abstractmethod

class Tyres(ABC) :
    
    @abstractmethod
    def needs_service() :
        pass