import ListeAktionen as la
import ListeBloecke as lb 
import Block as bl
import Aktion as ak

liste = la.ListeAktionen() 
blöcke = lb.ListBlocks()
blöcke.addBlock(5)
blöcke.addBlock(8)
blöcke.addBlock(17)



# test = la.ListeAktionen()
# test.extendList()
# test.list[-1].zuWarten = 1
# test.list[-1].move(0)
# for i in range(len(test.list)):
#     print("Warten: ",test.list[-1].warten)





liste.extendList()
while(liste.getPosition() != len(blöcke.listOfBlocks)):
    time = liste.getTime()
    t = liste.list[-1].move(time)
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

