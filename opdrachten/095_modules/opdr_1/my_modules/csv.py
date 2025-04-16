# csv.py (in de map my_modules)

import csv

def lees_csv(bestandsnaam):
    """Leest een CSV-bestand en retourneert de inhoud als een lijst van dictionaries."""
    try:
        with open(bestandsnaam, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except FileNotFoundError:
        print(f"Het bestand {bestandsnaam} is niet gevonden!")
        return []

