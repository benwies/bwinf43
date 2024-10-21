import Block as bl
import ListeBloecke as lb

class Aktion:
    def __init__(self,zuWarten):
        self.warten = int
        self.bewegt = int
        self.zuWarten = zuWarten
        pass
    
    def aktionAusführen(self, time,position,zuWarten):
        
        if lb.checkStatusFromTo(position, zuWarten) == True:
            self.bewegt = self.zuWarten
            return True