import keyboard
import Block as bl
import Aktion



#Hier wirt das Programm ausgeführt

schritte = []
zeit = int
aktion = Aktion
aktion.warten = 10
aktion.bewegt = 3
schritte.append(aktion)


def zeitGeben():
    for i in range (len(schritte)):
        zeit =+ schritte[i].warten
    return zeit

def postionGeben():
    for i in range(len(schritte)):
        pos =+ schritte[i].bewegt
    print(pos)
    
print("Bitte Interval für Block eigeben:")
s = input()

