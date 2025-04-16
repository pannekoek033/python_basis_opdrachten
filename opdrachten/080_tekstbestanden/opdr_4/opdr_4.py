# Opdracht 4 Tekst opslaan
# Naam student: Keano Hotzky
# Groep: IT2B


# Party enquete

# Lijst met vragen
vragen = [
    "Wat is je voornaam?",
    "Wat is je achternaam?",
    "Wat neem je mee aan drank?",
    "Wat neem je mee om te eten?"
]

# Dictionary om de antwoorden in op te slaan
antwoorden = {}

# Loop door de vragen en verzamel antwoorden
for i, vraag in enumerate(vragen, start=1):
    antwoord = input(f"{i}. {vraag}\n")
    if i == 1:
        antwoorden["voornaam"] = antwoord
    elif i == 2:
        antwoorden["achternaam"] = antwoord
    elif i == 3:
        antwoorden["drank"] = antwoord
    elif i == 4:
        antwoorden["eten"] = antwoord

# Print afsluitende boodschap
print("\nBedankt voor het invullen!")
print("See you at the party.")

# Sla de antwoorden op in een tekstbestand
with open("feestgangers.txt", "a", encoding="utf-8") as bestand:
    bestand.write("----\n")
    for key, value in antwoorden.items():
        bestand.write(f"{key}: {value}\n")
    bestand.write("\n")  # lege regel tussen deelnemers
