import Aktion as ak

class ListeAktionen:
    def __init__(self):
        self.list = []
    
    def extendList(self):
        a = ak.Aktion(1)
        self.list.append(a)
    
    def getTime(self):
        for i in range(len(self.list)):
            time =+ self.list[i].warten
            return time

    def executeAction(self):
        if self.list[-1].aktionAusführen() == True:
            self.extendList