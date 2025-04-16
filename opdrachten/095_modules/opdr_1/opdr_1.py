# Opdracht 1 functies
# Naam student: Keano Hotzky
# Groep: IT2B

# importeer de module csv...

# opdr_1.py

from my_modules.csv import lees_csv

# Bestandspad naar het CSV-bestand
bestand = "data.csv"  # Zorg ervoor dat dit bestand bestaat in dezelfde map als opdr_1.py

# Roep de functie lees_csv aan
data = lees_csv(bestand)

# Print de data die uit het CSV-bestand is gelezen
print(data)
