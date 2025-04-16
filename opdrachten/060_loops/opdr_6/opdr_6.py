# Opdracht 3 input functie
# Naam student: Keano Hotzky
# Groep: IT2B

# Hier komt je code...

# Hier start de for-loop

pizzas = ['margharita', 'calzone', 'verdi', 'olivio', 'quattro stagioni']

pizzas.sort()
pizzas.append('yo-favorito')
pizzas.remove('olivio')

print(pizzas[:3])                      
print([pizzas[len(pizzas)//2]])       
print(pizzas[-3:])                   