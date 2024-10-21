import keyboard
import Block as bl


class ListBlocks:
    def __init__(self) -> None:
        self.listOfBlocks = []
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


    def checkStatusFromTo(self,start,end,time):
        for i in range(end-start):
            if self.listOfBlocks[start + i].checkStatues(time) != True:
                return False
        return True
    
    def printList(self):
        for i in range(len(self.listOfBlocks)):
            print(self.listOfBlocks[i].interval)
    