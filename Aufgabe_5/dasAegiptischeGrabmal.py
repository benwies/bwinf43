import keyboard
import Block as bl
import Aufgabe_5.Action as po

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


    

# Setzt die Zeit immer um 1 Hoch für jedes Objekt einzeln

        
def checkPosition(position):
    if listOfBlocks[position].closed == True:
        return(True)
    else:
        return(False)
    
    
# def moving():
#     global movedTiles
#     print("try moving")
#     while (listOfBlocks[movedTiles].closed == False):
#         movedTiles = movedTiles + 1
#         print("moved" "Moved Tiles: " + str(movedTiles))
#         if movedTiles == len(listOfBlocks):
#             print("Finished")
#             break
        
def time():
    for i in range(len(listOfBlocks)):
        listOfBlocks[i].time = listOfBlocks[i].time + 1
        print(listOfBlocks[i].time)
        listOfBlocks[i].checkStatues()       

# while keyboard.read_key() != "e":
#     if keyboard.read_key() == "q":
#         time()
        

