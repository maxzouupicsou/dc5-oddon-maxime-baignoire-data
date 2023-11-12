def calculer_ctr_en_pourcentage(nombre_de_clicks, nombre_d_impressions):

    if not isinstance(nombre_de_clicks, (int, float)) or not isinstance(nombre_d_impressions, (int, float)):
        raise TypeError("Les nombres de clicks et d'impressions doivent être des nombres (int ou float)")

    if nombre_de_clicks < 0 or nombre_d_impressions < 0:
        raise ValueError("Les nombres de clicks et d'impressions doivent être positifs ou nuls")
    if nombre_d_impressions == 0:
        return 0

    ctr = (nombre_de_clicks / nombre_d_impressions) * 100
    return ctr

try:
    nombre_de_clicks = "zero"
    nombre_d_impressions = 1000

    ctr_en_pourcentage = calculer_ctr_en_pourcentage(nombre_de_clicks, nombre_d_impressions)
    print(f"Le CTR est de {ctr_en_pourcentage}%")
except (TypeError, ValueError) as e:
    print(f"Erreur : {e}")
