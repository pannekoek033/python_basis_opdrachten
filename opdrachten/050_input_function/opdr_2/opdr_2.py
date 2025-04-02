# Opdracht 2 berekeningen
# Naam student: Keano Hotzky
# Groep: IT2B

# Hier komt je code...

gasten = ["Jij", "paul", "kees", "marie", "hilda"]
gasten = tuple(gasten)
gasten = list(gasten)

print(gasten)

#Nou belt Marie dat ze niet meer meegaat.

del gasten[3]

print(gasten)

#Even later belt George, hij wil ook mee. George wil naast Kees zitten!

gasten.insert(3, "George")

print(gasten)