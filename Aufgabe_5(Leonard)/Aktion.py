import Block as bl
import ListeBloecke as lb
import ListeAktionen as la

class Aktion:
    def __init__(self,zuWarten):
        self.warten = int(0)
        self.bewegt = int
        self.zuWarten = zuWarten
        pass
    
    def aktionAusführen(self, timeOld,position,zuWarten):
        
        while lb.checkStatusFromTo(position, zuWarten,time) != True:
            self . warten += 1
            time = timeOld + self.warten