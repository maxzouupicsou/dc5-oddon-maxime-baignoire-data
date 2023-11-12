try:
    couts_de_la_campagne = [2000, 3000, 5000]
    revenus_generes = [15000, 10000, 5000]

    if not isinstance(couts_de_la_campagne, list) or not isinstance(revenus_generes, list):
        raise TypeError("Les coûts et les revenus doivent être impérativement fournis sous forme de listes")
    if not couts_de_la_campagne or not revenus_generes:
        raise ValueError("Les listes des coûts et des revenus ne doivent pas être vides !")

    for cout in couts_de_la_campagne + revenus_generes:
        if not isinstance(cout, (int, float)):
            raise TypeError("Tous les éléments des listes doivent être des nombres rentrés au format numérique")
        if abs(cout) > 1e9:  
            raise ValueError("Les valeurs ne sont pas censées être aussi élevés, il doit s'agir d'une erreur")

    cout_total_de_la_campagne = sum(abs(cout) for cout in couts_de_la_campagne)
    revenu_total_genere = sum(revenus_generes)

    if revenu_total_genere > cout_total_de_la_campagne:
        print("La campagne est rentable")
    else:
        print("La campagne n'est pas rentable")

except TypeError as e:
    print(f"Erreur de type : {e}")
except ValueError as e:
    print(f"Erreur de valeur : {e}")
except Exception as e:
    print(f"Erreur inattendue : {e}")
