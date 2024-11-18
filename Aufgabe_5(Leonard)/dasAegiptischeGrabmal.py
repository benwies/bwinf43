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
            
    liste.list.pop()
    
    print("Der Weg der Gegangen werden muss lautet")
    for i in range(len(liste.list)):
        print("Warte für", liste.list[i].warten,"Minuten.", "Gehe dann " ,liste.list[i].bewegt, "Blöcke weit" )


ausführen()