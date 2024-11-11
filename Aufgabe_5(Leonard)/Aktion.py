import Block as bl
import ListeAktionen as la
from ListeBloecke import ListBlocks 
from ListeAktionen import ListeAktionen

class Aktion(ListeAktionen, ListBlocks):
    def __init__(self,zuWarten,position):
        
        self.warten = int(0)
        self.bewegt = int
        self.zuWarten = int(zuWarten)
        self.position = int(position)
        pass
    
    def move(self,time,liste):
        end = self.zuWarten+self.position
        while ListBlocks.checkStatusFromTo(self.position,end,time):
            pass
        