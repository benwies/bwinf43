

class ListeAktionen:
    def __init__(self):
        self.list = []
        self.extendList()
    
    def extendList(self):
        import Aktion as ak
        a = ak.Aktion(int(1),self.getPosition())
        self.list.append(a)
    
    def getTime(self):
        time = int(0)
        for i in range(len(self.list)):
            time = time + self.list[i].warten
        return int(time)
        
        
    def getPosition(self):
        position = int(0)
        for i in range(len(self.list)):
            position = position + self.list[i].bewegt
        return int(position)

    