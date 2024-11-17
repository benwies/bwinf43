import ListeAktionen as la
import ListeBloecke as lb 
import Block as bl
import Aktion as ak

liste = la.ListeAktionen() 
blöcke = lb.ListBlocks()
blöcke.addBlock(4)
blöcke.addBlock(10)
blöcke.addBlock(3)
blöcke.addBlock(3)
blöcke.addBlock(4)
blöcke.addBlock(1)
print(blöcke.checkStatusFromTo(0,2,11))
print(blöcke.listOfBlocks[1].checkStatues(11))

liste.extendList()
while(liste.getPosition() != len(blöcke.listOfBlocks)):
    print("position: ",liste.getPosition())
    time = liste.getTime()
    t = liste.list[-1].move(time,blöcke.listOfBlocks)
    if t == "kill":
        print("kill")
        a = liste.list[-1]
        liste.list.pop()
        liste.list[-1].zuWarten = liste.list[-1].zuWarten + a.zuWarten
        liste.list[-1].setBack()

    elif t == "moved":
        liste.extendList()
        
     
    
print("finall")
print("position: ",liste.getPosition())
for i in range(len(liste.list)):
    print("Warten:", liste.list[i].warten, " Bewegt: " ,liste.list[i].bewegt,"zuWarten:",liste.list[i].zuWarten,"Position: ",liste.list[i].position )
    
print("Länge Liste: ",len(liste.list))

