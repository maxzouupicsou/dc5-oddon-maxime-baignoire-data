try:
    nombre_clients = 100
    revenu_moyen_par_client = 20
  
    if not (isinstance(nombre_clients, (int, float)) and isinstance(revenu_moyen_par_client, (int, float))):
        raise TypeError("Attention ! Le nombre de clients et le revenu moyen par client doit être entré au format numérique ")

    revenu_total = revenu_moyen_par_client * nombre_clients
    print(f"Le montant du revenu total est de {revenu_total}")

except TypeError as e:
    print(f"Erreur: {e}")
