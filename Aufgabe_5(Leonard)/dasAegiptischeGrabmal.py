import ListeAktionen as la
import ListeBloecke as lb 
import Block as bl
import Aktion as ak
import DateiEinlesen
liste = la.ListeAktionen() 
blöcke = lb.ListBlocks()



def einlesenBlöcke():
    for i in DateiEinlesen.lese_datei_ohne_erste_zeile():
        blöcke.addBlock(int(i))

def ausführen():
    
    einlesenBlöcke()
    
    liste.extendList()
    while(liste.getPosition() != len(blöcke.listOfBlocks)):
        time = liste.getTime()
        t = liste.list[-1].move(time)
        if t == "kill":
            a = liste.list[-1]
            liste.list.pop()
            liste.list[-1].zuWarten = liste.list[-1].zuWarten + a.zuWarten
            liste.list[-1].setBack()

        elif t == "bewegt":
            liste.extendList()
            
        
        
    print("finall")
    print("position: ",liste.getPosition())
    for i in range(len(liste.list)):
        print("Warten:", liste.list[i].warten, " Bewegt: " ,liste.list[i].bewegt,"zuWarten:",liste.list[i].zuWarten,"Position: ",liste.list[i].position )
        
    print("Länge Liste: ",len(liste.list))
    print(liste.getTime())

ausführen()