class Szamitas:
    def __init__(self,projekt, kesedelmes_napok):
        self.kotber = 0
        self.projekt = projekt
        self.kesedelmes_napok = kesedelmes_napok
    
    def szamol(self):
        self.kotber = self.kesedelmes_napok * (self.projekt*0.05)