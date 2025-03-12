# Opdracht 3 tekstfuncties
# Naam student: Keano Hotzky
# Groep: IT2B

# Hier komt je code...
# Functie om y te berekenen op basis van de gegeven formule
def bereken_y(x):
    return (4 * x**3) - (2 * x**2) - 1

# Eerste testwaarde
x = 1
y = bereken_y(x)
print(f"De uitkomst is: {y}")

# Tweede testwaarde
x = 2
y = bereken_y(x)
print(f"De uitkomst is: {y}")

# Derde testwaarde
x = 0
y = bereken_y(x)
print(f"De uitkomst is: {y}")
