# Opdracht 1 input function
# Naam student: Keano Hotzky
# Groep: IT2B

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.



import math

def bereken_schuine_zijde(a, b):
    # Stelling van Pythagoras: c² = a² + b²
    c_kwadraat = a**2 + b**2
    c = math.sqrt(c_kwadraat)
    return c

def main():
    # Gebruikersinvoer vragen
    a = float(input("Geef de lengte van de eerste zijde\n"))
    b = float(input("Geef de lengte van de tweede zijde\n"))
    
    # Bereken de schuine zijde
    c = bereken_schuine_zijde(a, b)
    
    # Resultaat weergeven
    print(f"\nDe lengte van de schuine zijde is: {c}")

# Programma uitvoeren
if __name__ == "__main__":
    main()