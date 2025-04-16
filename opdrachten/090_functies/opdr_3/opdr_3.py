# Opdracht 1 functies
# Naam student: Keano Hotzky
# Groep: IT2B


import math  


def kubus_vol(zijde):
    volume = zijde ** 3  
    return volume


def bol_vol(straal):
    volume = (4/3) * math.pi * (straal ** 3)  
    return volume


kubus_resultaat = kubus_vol(5)
print(f"De inhoud van deze kubus is: {kubus_resultaat}")

bol_resultaat = bol_vol(4)
print(f"De inhoud van deze bol is: {bol_resultaat}")
