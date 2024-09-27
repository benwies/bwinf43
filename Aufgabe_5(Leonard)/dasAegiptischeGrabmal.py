import keyboard
import Block as bl
import Action as po

listOfBlocks = []
listOfActions = []
movedTiles = int(0)

# hier werden die einzelnen Intzervalle für die Blöcke eingegeben und ein Objekt Block wird erstellt mit dem jeweiligen Intervall als Variable
userInput = -1
print("Bitte geben sie  Steinblock Intervalle ein falls fertig geben sie fertig ein ")
while (userInput != "fertig"):
    userInput = input()
    if userInput.isdigit() == True:
        block = bl.Block(userInput)
        listOfBlocks.append(block)


    
    

        

        

