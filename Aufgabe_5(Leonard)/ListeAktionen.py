import Aktion as ak

class ListeAktionen:
    def __init__(self):
        self.list = []
        self.extendList()
    
    def extendList(self):
        a = ak.Aktion(1)
        self.list.append(a)
    
    def getTime(self):
        time = int(0)
        for i in range(len(self.list)):
            time = time + self.list[i].warten
            return time

    