import keyboard
import Block as bl


class ListBlocks:        
    listOfBlocks = []

    def __init__(self) -> None:
        pass

# hier werden die einzelnen Intzervalle für die Blöcke eingegeben und ein Objekt Block wird erstellt mit dem jeweiligen Intervall als Variable
    def inputBlocks(self):
        userInput = -1
        print("Bitte geben sie  Steinblock Intervalle ein falls fertig geben sie fertig ein ")
        while (userInput != "fertig"):
            userInput = input()
            if userInput.isdigit() == True:
                self.addBlock(userInput)



    def addBlock(self,intervall):
        block = bl.Block(intervall)
        self.listOfBlocks.append(block)

    @classmethod
    def checkStatusFromTo(self,start,end,time):
        listOfBlocks = self.listOfBlocks
        x = end - start
        for i in range(x):
            if listOfBlocks[start + i].checkStatues(int(time)) == True:
                return True
            else:
                return False
    
    def printList(self):
        for i in range(len(self.listOfBlocks)):
            print(self.listOfBlocks[i].interval)
    