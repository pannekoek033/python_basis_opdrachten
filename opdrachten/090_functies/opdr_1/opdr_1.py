# Opdracht 1 functies
# Naam student: Keano Hotzky
# Groep: IT2B



    # je code komt hier
    # het woordje pass hieronder kun je weghalen
  
def write_to_file(bestandsnaam, tekst):
    with open(bestandsnaam, 'a', encoding='utf-8') as bestand:
        bestand.write(tekst + "\n")  


my_tekst = "Schrijf dit maar even in een bestandje"
my_file = "test.txt"
write_to_file(my_file, my_tekst)




