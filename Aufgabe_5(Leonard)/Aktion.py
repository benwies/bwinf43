import Block as bl
from ListeBloecke import ListBlocks 
from ListeAktionen import ListeAktionen

class Aktion(ListeAktionen, ListBlocks):
    def __init__(self,zuWarten):
        self.warten = int(0)
        self.bewegt = int
        self.zuWarten = int(zuWarten)
        pass
    
    def move(self): 
        if ListBlocks.checkStatusFromTo(ListeAktionen.getPosition,self.zuWarten,ListeAktionen.getTime) == True:
            ListeAktionen.extendList()
            print("passt kann moven")
        else:
            print("kann nicht bewegen")
            self.warten = self.warten + 1