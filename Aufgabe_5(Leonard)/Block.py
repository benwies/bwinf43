# Erstellt die einzelnen Blöcke

class Block():
    def __init__(self, interval):
        self.interval = int(interval)
        self.closed = True

    
# Überprüft ob die Tür gerade geschlossen oder offen ist
    def checkStatues(self,time):     
        return (time-1//self.interval)%2 == 1
        
