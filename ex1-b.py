# Demandez à l'utilisateur de saisir une phrase
phrase_utilisateur = input("Veuillez saisir une phrase : ")

# Affichez la phrase en majuscules (sans utiliser upper())
phrase_majuscules = ''.join([chr(ord(c) - 32) if 'a' <= c <= 'z' else c for c in phrase_utilisateur])
print(f"En majuscules : {phrase_majuscules}")

# Affichez la phrase en minuscules (sans utiliser lower())
phrase_minuscules = ''.join([chr(ord(c) + 32) if 'A' <= c <= 'Z' else c for c in phrase_utilisateur])
print(f"En minuscules : {phrase_minuscules}")

# Comptez le nombre de mots dans la phrase (sans utiliser split()),
# en tenant compte de tous les caractères spéciaux collés aux mots
import re

mots = re.findall(r'\w+|[?&!]', phrase_utilisateur)
nombre_mots = len(mots)

print(f"Nombre de mots : {nombre_mots}")
