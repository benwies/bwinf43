import ListeAktionen as la
import ListeBloecke as lb 
import Block as bl
import Aktion as ak

liste = la.ListeAktionen()
blöcke = lb.ListBlocks()
blöcke.addBlock(2)
blöcke.addBlock(2)
blöcke.addBlock(2)
blöcke.addBlock(2)
# blöcke.printList()
liste.extendList()


# time = liste.getTime()
# print("test")
# for i in range(5):
#     time = liste.getTime()
#     liste.list[-1].move(time,blöcke.listOfBlocks)
#     "test2"
print(blöcke.listOfBlocks[0].interval)
print(blöcke.listOfBlocks[0].checkStatues(4))
for i in range(len(blöcke.listOfBlocks)):
    if blöcke.listOfBlocks[i].checkStatues(3) == True:
        print("ist offen")
print(blöcke.checkStatusFromTo(0,3,1))
print(blöcke.checkStatusFromTo(0,3,2))
print(blöcke.checkStatusFromTo(0,3,3))
print(blöcke.checkStatusFromTo(0,3,4))


# block = bl.Block(10)
# for i in range(1,100):
#     print("Durchlauf: " ,i , " Status: ", block.checkStatues(i))

