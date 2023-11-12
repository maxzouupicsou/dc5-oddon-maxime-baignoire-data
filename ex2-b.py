nombres = [4, 1, "coucou", 3, -54.5, 2, 6.45, 5, 8, 1000000]

try:
    if not nombres:
        raise ValueError("La liste est vide")

    max_nombre = -float('inf')
    min_nombre = float('inf')
    somme = 0

    for nombre in nombres:
        if not isinstance(nombre, (int, float)):
            raise TypeError(f"Type de données incorrect pour l'élément '{nombre}'. La liste doit contenir uniquement des nombres réels au format numérique")
        if nombre > max_nombre:
            max_nombre = nombre
        if nombre < min_nombre:
            min_nombre = nombre
        somme += nombre

    moyenne = somme / len(nombres)

    print("Maximum:", max_nombre)
    print("Minimum:", min_nombre)
    print("Moyenne:", moyenne)

except ValueError as e:
    print(f"Erreur de valeur : {e}")
except TypeError as e:
    print(f"Erreur de type : {e}")
