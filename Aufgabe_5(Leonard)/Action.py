from dasAegiptischeGrabmal import listOfBlocks
import Block

class Action():
    def __init__(self):
        self.position = int
        self.waited = int
        self.moved = int
        self.waitDoors = int(1)
        
    def moving(self):
        if (self.nextOpen() >= self.waitDoors):
            movedTo = self.position + self.nextOpen()
            return(movedTo)
    
    def nextOpen(self):
        open = int(0)
        for i in range(listOfBlocks.length() - self.position):
            if listOfBlocks[self.position + i].closed == False:
                open += 1
            else:
                return(open)
            
            