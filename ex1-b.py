
phrase_utilisateur = input("Veuillez saisir une phrase : ")

phrase_majuscules = ''.join([chr(ord(c) - 32) if 'a' <= c <= 'z' else c for c in phrase_utilisateur])
print(f"En majuscules : {phrase_majuscules}")

phrase_minuscules = ''.join([chr(ord(c) + 32) if 'A' <= c <= 'Z' else c for c in phrase_utilisateur])
print(f"En minuscules : {phrase_minuscules}")

import re
mots = re.findall(r'\b\w+\b|\S', phrase_utilisateur)
nombre_mots = len(mots)
print(f"Nombre de mots : {nombre_mots}")