import Aktion as ak

class ListeAktionen:
    def __init__(self):
        self.head = ak
        self.tail = ak

    def length(self):
        if self.head == None:
            return 0
        return self.head.getLength()
        
    def extend(self):   
        a = ak.Aktion(1, self.length(),None,None)
        if self.head == None:
            head = a
        self.tail = a
        
        
l = ListeAktionen()
l.extend()
l.extend()
print(l.length)