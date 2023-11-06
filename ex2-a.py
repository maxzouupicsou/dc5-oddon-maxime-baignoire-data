# Créez une liste des dépenses marketing mensuelles
depenses_mensuelles = [1000, 1200, 800, 1500, 1100, 1300, 1400, 900, 1000, 950, 1200, 1100]

# Initialisez une variable pour stocker les dépenses totales de l'année
depenses_annuelles = 0

# Parcourez la liste des dépenses mensuelles et additionnez-les
for depense in depenses_mensuelles:
    depenses_annuelles += depense

# Affichez les dépenses totales de l'année
print(f"Les dépenses totales de l'année sont de : {depenses_annuelles} dollars")
