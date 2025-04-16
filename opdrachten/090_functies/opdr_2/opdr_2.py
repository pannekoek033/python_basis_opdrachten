# Opdracht 1 functies
# Naam student: Keano Hotzky
# Groep: IT2B




# Functie die kilometers naar miles converteert
def kilometers_naar_miles(kilometers):
    miles = kilometers / 1.609344  # Converteer kilometers naar miles
    return miles

# Functie die miles naar kilometers converteert
def miles_naar_kilometers(miles):
    kilometers = miles * 1.609344  # Converteer miles naar kilometers
    return kilometers

# Voorbeeld van gebruik van de functies
kilometers = 1223
miles = 867

# Kilometer naar miles
miles_result = kilometers_naar_miles(kilometers)
print(f"{kilometers} kilometers = {miles_result} miles")

# Miles naar kilometer
km_result = miles_naar_kilometers(miles)
print(f"{miles} miles = {km_result} kilometers")
