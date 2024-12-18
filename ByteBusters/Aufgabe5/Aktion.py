from ListeBloecke import ListBlocks 

class Aktion():
    def __init__(self,zuWarten,position):
        self.warten = int(0)
        self.bewegt = int(0)
        self.zuWarten = int(zuWarten)
        self.position = int(position)
        pass
    
    def move(self,ownTime):
        
        if self.zuWarten == 1:
            while ListBlocks.checkStatusAt(self.position,ownTime) != True:
                if self.checkForKill(ownTime) == True:

                    return "kill"   
                self.warten = self.warten + int(1)
                ownTime = ownTime + 1
        else:
            end = self.zuWarten + self.position
            while ListBlocks.checkStatusFromTo(self.position,end,ownTime) != True :
                
                if self.checkForKill(ownTime) == True:

                    return "kill"
                self.warten = self.warten + int(1)
                ownTime = ownTime + 1
        self.bewegt = self.zuWarten
        return "bewegt"    
    
#return True wenn der Block zerdrücks und False wenn nicht.
    def checkForKill(self,time):
        if self.position == 0:
            return False
        else:
            if ListBlocks.checkStatusAt(self.position-1,time) == True :
                return False
            else:
                return True
            
    def setBack(self):
        self.warten = 0
        self.bewegt = 0