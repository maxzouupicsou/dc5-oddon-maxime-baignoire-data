def calculer_factoriel_iteratif(n):
    if not isinstance(n, int):
        raise TypeError("L'entrée doit être un entier")
    if n < 0:
        raise ValueError("Le nombre doit être non négatif")

    resultat = 1
    for i in range(2, n + 1):
        resultat *= i
    return resultat

try:
    nombre = 1000
    resultat = calculer_factoriel_iteratif(nombre)
    print(f"Le factoriel de {nombre} est {resultat}")
except (TypeError, ValueError) as e:
    print(f"Erreur : {e}")
