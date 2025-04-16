# Opdracht 1 functies
# Naam student: Keano Hotzky
# Groep: IT2B


def volledige_naam(lijst_met_namen):
    # Itereer over de lijst van namen
    for naam in lijst_met_namen:
        # Controleer of er een tussenvoegsel is
        if naam["tussenvoegsel"]:
            # Als er een tussenvoegsel is, voeg dit toe
            volledige_naam = f"{naam['voornaam']} {naam['tussenvoegsel']} {naam['achternaam']}"
        else:
            # Als er geen tussenvoegsel is, voeg alleen voornaam en achternaam toe
            volledige_naam = f"{naam['voornaam']} {naam['achternaam']}"
        
        # Print de volledige naam
        print(volledige_naam)


# Test de functie met de lijst van namen
namen = [
    {"voornaam": "Willem", "tussenvoegsel": "van", "achternaam": "Dijk"},
    {"voornaam": "Klaas", "tussenvoegsel": "", "achternaam": "Wopstra"},
    {"voornaam": "Miep", "tussenvoegsel": "van der", "achternaam": "Plas"},
    {"voornaam": "Carla", "tussenvoegsel": "", "achternaam": "Hoogvliet"},
]

volledige_naam(namen)
