class Aktion:
    def __init__(self,zuWarten, numAkt):
        self.warten = int
        self.bewegt = int
        self.zuWarten = zuWarten
        self.numAkt = numAkt
        self.nachfolger = Aktion
        self.vorgänger = Aktion
        pass
    
    def getLength(self):
        if self.nachfolger == None:
            return self.nachfolger.getLength() +1
        else:
            return 1