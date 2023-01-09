from nyomtat import Nyomtat
from szamitas import Szamitas
ceg_nev = input("Cégneve : ")
projekt = input("Projekt értéke: " + "Ft : ")
kesedelmes_napok = input("késedelmes napo száma : ")
if kesedelmes_napok.isnumeric() and projekt.isnumeric():
    num1 = int(projekt)
    num2 = int(kesedelmes_napok)
    

    nyom = Nyomtat(ceg_nev,num1,num2)
    nyom.nyomtatos_metodus()

    szamolas = Szamitas(num1,num2,)
    szamolas.szamol()
    
    
else:
    print("nem szam")

