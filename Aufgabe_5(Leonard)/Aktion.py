import Block as bl
import ListeAktionen as la
from ListeBloecke import ListBlocks 
from ListeAktionen import ListeAktionen

class Aktion(ListeAktionen, ListBlocks):
    def __init__(self,zuWarten,position):
        #wartenist mind 1 da Türen Intervall < 0 ist und sonst die Rechnung nicht Fuunktioniert da eine gweisse Grundzeit gegeben werden muss
        self.warten = int(0)
        self.bewegt = int(0)
        self.zuWarten = int(zuWarten)
        self.position = int(position)
        pass
    
    def move(self,time,liste):
        end = self.zuWarten+self.position
        while ListBlocks.checkStatusFromTo(self.position,end,time) != True :
            self.warten = self.warten + int(1)
            time = time + 1
        self.bewegt = self.zuWarten    
        # time = time + 1

        