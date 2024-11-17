import Block as bl
import ListeAktionen as la
from ListeBloecke import ListBlocks 
from ListeAktionen import ListeAktionen

class Aktion(ListeAktionen, ListBlocks):
    def __init__(self,zuWarten,position):
        self.warten = int(0)
        self.bewegt = int(0)
        self.zuWarten = int(zuWarten)
        self.position = int(position)
        pass
    
    def move(self,ownTime):
        end = self.zuWarten + self.position
        if self.zuWarten == 1:
            print("klein")
            while ListBlocks.checkStatusAt(self.position,ownTime) != True:
                if self.checkForKill(ownTime) == False:

                    return "kill"   
                self.warten = self.warten + int(1)
                ownTime = ownTime + 1
        else:
            print("groß")
            while ListBlocks.checkStatusFromTo(self.position,end,ownTime) != True :
                
                if self.checkForKill(ownTime) == False:

                    return "kill"
                self.warten = self.warten + int(1)
                ownTime = ownTime + 1
        self.bewegt = self.zuWarten
        return "moved"    
        # time = time + 1

#return True wenn der Block zerdrücks und False wenn nicht.
    def checkForKill(self,time):
        if self.position == 0:
            return True
        else:
            if ListBlocks.checkStatusAt(self.position-1,time) == False :
                return False
            else:
                return True
            
    def setBack(self):
        self.warten = 0
        self.bewegt = 0