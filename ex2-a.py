depenses_mensuelles = [1000.20, 1200, 800, 1500, 1100, -12, 1400, 900, 1000, 950, 1200, -78000]

depenses_annuelles = 0

for depense in depenses_mensuelles:
    depenses_annuelles += depense

print(f"Les dépenses totales de l'année sont de : {depenses_annuelles} dollars")
