from szamitas import Szamitas
import datetime


class Nyomtat:
    def __init__(self, ceg_nev, projekt, kesedelmes_napok):
        self.ceg_nev = ceg_nev
        self.projekt = projekt
        self.kesedelmes_napok = kesedelmes_napok
    
    def nyomtatos_metodus(self):
        szamolas = Szamitas(self.projekt,self.kesedelmes_napok)
        szamolas.szamol()
        
        datum = datetime.datetime.now().strftime("%m.%d.%y")

        f = open("kisztina_kalapacs.txt", "w")
        f.write("szamitasos lap")
        f.write(f"felhasznalo neve: {self.ceg_nev}")
        f.write(f"projekt: {self.projekt}")
        f.write(f"kesedelmes napok: {self.kesedelmes_napok}")
        
        f.write(f" kötbér : {szamolas.kotber}")
        
        f.write("\n")
        f.write(f"kelt: szeged , {datum}")

        f.close()