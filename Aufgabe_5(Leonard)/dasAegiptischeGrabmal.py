import ListeAktionen as la
import ListeBloecke as lb 
import Block as bl
import Aktion as ak

liste = la.ListeAktionen()
blöcke = lb.ListBlocks()
blöcke.addBlock(20)
blöcke.addBlock(3)
blöcke.addBlock(3)
blöcke.addBlock(4)
blöcke.printList()

# while liste.getPosition()-1 <= len(blöcke.listOfBlocks):
print("Huan")
while(liste.getPosition() != len(blöcke.listOfBlocks)):
    time = liste.getTime()
    liste.list[-1].move(time,blöcke.listOfBlocks)
    liste.extendList()
    print(len(liste.list))
    print ("Position:" ,liste.getPosition())

