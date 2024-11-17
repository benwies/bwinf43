import ListeAktionen as la
import ListeBloecke as lb 
import Block as bl
import Aktion as ak

liste = la.ListeAktionen()
blöcke = lb.ListBlocks()
blöcke.addBlock(3)
blöcke.addBlock(3)
blöcke.addBlock(3)
blöcke.addBlock(3)
blöcke.addBlock(3)
blöcke.addBlock(3)
blöcke.addBlock(3)
blöcke.addBlock(3)

# while liste.getPosition()-1 <= len(blöcke.listOfBlocks):
print("Huan")
while(liste.getPosition() != len(blöcke.listOfBlocks)):
    time = liste.getTime()
    liste.list[-1].move(time,blöcke.listOfBlocks)
    liste.extendList()
    print("Länge Blöcke: ", len(blöcke.listOfBlocks)," Länge Aktionen: ", liste.getPosition())
    print("time" , liste.getTime())
    print ("Position:" ,liste.getPosition())

for i in range(len(liste.list)):
    print(liste.list[i].warten)
    
print("Länge Liste: ",len(liste.list))