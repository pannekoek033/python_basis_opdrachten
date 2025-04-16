# Opdracht 3 Tekst opslaan
# Naam student: Keano Hotzky
# Groep: IT2B

def encrypt_tekst(tekst, shift=5):
    resultaat = ""

    for char in tekst:
        if char.isalpha():
            basis = ord('A') if char.isupper() else ord('a')
            verschoven = (ord(char) - basis + shift) % 26 + basis
            resultaat += chr(verschoven)
        else:
            resultaat += char

    return resultaat

# Vraag de gebruiker om een tekst
invoer = input("Geef de tekst die je wilt encrypten...\n")

# Versleutel de tekst
versleuteld = encrypt_tekst(invoer)

# Print het resultaat
print(versleuteld)



