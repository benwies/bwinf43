# Erstellt die einzelnen Blöcke

class Block():
    def __init__(self, interval):
        self.interval = int(interval)
        self.closed = True

    
# Überprüft ob die Tür gerade geschlossen oder offen ist
    def checkStatues(self,time):
        if time == 0:
            return False    
        else: 
            return ((time)//self.interval)%2 == 1
        
