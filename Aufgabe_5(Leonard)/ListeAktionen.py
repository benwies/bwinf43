import Aktion as ak

class ListeAktionen:
    def __init__(self):
        self.list = []
    
    def extendList(self):
        a = ak.Aktion(1)
        self.list.append(a)
    
        
l = ListeAktionen()



for a in range(len(l.list)):
    print(l.list[a].zuWarten)