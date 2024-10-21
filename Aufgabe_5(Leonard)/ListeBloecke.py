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
                block = bl.Block(userInput)
                self.listOfBlocks.append(block)
        

    def checkStatusFromTo(self,start,end):
        for i in range(end-start):
            if self.listOfBlocks[start + i].checkStatues() != True:
                return False
        return True