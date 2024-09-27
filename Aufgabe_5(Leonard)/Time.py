#gibt den Zeitverlauf der Aufgabe an 
class Time():
    def __init__(self):
        self.time = int(0)
        pass
    def timePass(self):
        self.time += self.time
    
    def getTime(self):
        return (self.time)
    
    def setTime(self,newTime):
        self.time = newTime
        