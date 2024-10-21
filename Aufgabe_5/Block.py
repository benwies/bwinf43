# Erstellt die einzelnen Blöcke

class Block():
    def __init__(self, interval):
        self.interval = int(interval)
        self.time = int(0)
        self.closed = True

    
# Überprüft ob die Tür gerade geschlossen oder offen ist
    def checkStatues(self):
        if self.time % self.interval == 0:
            if self.time/self.interval%2 == 0:
                self.closed = True
                print("closed")
            else:
                self.closed = False
                print("open")
    
        