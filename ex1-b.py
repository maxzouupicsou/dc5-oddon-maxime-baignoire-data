# Demandez à l'utilisateur de saisir une phrase
phrase_utilisateur = input("Veuillez saisir une phrase : ")

# Affichez la phrase en majuscules 
phrase_majuscules = ''.join([chr(ord(c) - 32) if 'a' <= c <= 'z' else c for c in phrase_utilisateur])
print(f"En majuscules : {phrase_majuscules}")

# Affichez la phrase en minuscules
phrase_minuscules = ''.join([chr(ord(c) + 32) if 'A' <= c <= 'Z' else c for c in phrase_utilisateur])
print(f"En minuscules : {phrase_minuscules}")

# Comptez le nombre de mots dans la phrase
nombre_mots = 0

for caractere in phrase_utilisateur:
    if caractere == ' ':
        nombre_mots += 1

print(f"Nombre de mots : {nombre_mots}")
