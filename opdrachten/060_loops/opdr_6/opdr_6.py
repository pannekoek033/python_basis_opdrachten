# Opdracht 3 input functie
# Naam student: Keano Hotzky
# Groep: IT2B

# Hier komt je code...

# Hier start de for-loop

pizzas = ['margharita', 'calzone', 'verdi', 'olivio', 'quattro stagioni']

pizzas.sort()
pizzas.append('yo-favorito')
pizzas.remove('olivio')

print(pizzas[:3])                      # eerste 3 pizza's
print([pizzas[len(pizzas)//2]])       # middelste pizza
print(pizzas[-3:])                    # laatste 3 pizza's
