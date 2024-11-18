
import Block as bl


class ListBlocks:        
    listOfBlocks = []

    def __init__(self) -> None:
        pass



    def addBlock(self,interval):
        block = bl.Block(interval)
        self.listOfBlocks.append(block)


    @classmethod
    def checkStatusFromTo(self,start,end,time):
        # if time == 0:
        #     return False
        x = end  - start
        for i in range(x):
            if self.listOfBlocks[start + i].checkStatues(int(time)) == False:
                
                return False
        return True
    
    
    @classmethod
    def checkStatusAt(self,position,time):
        return self.listOfBlocks[position].checkStatues(time)
            
        
    def printList(self):
        for i in range(len(self.listOfBlocks)):
            print(self.listOfBlocks[i].interval)
    