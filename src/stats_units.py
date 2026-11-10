import statistics as stats

lst_nb = [10005, 10, 1000, 60, 0, 770, 118]

def analyser_ventes(transaction):
    indicateurs = {}
    valide = []
    outliers = []

    for nb in transaction:
        if nb <= 0:
            continue
        valide.append(nb)                


    nb_transaction = len(valide)
    somme_transaction = sum(valide)
    moyenne = round(stats.mean(valide), 2)
    mediane = stats.median(valide)
    ecart_type = round(stats.stdev(valide,), 2)
    val_min, val_max = min(valide), max(valide)


    # Repérer les outliers
    for nb in valide:
        outlier = moyenne * 2
        if nb > outlier:
            outliers.append(nb) 


    indicateurs["transactions_valide"] = nb_transaction     # Compter transaction valide
    indicateurs["ventes_totales"] = somme_transaction       # Somme des totales des ventes
    indicateurs["moyenne"] = moyenne
    indicateurs["mediane"] = mediane
    indicateurs["ecart_type"] = ecart_type
    indicateurs["valeur_minimale"] = val_min
    indicateurs["valeur_maximale"] = val_max
    indicateurs["outliers"] = outliers

    return indicateurs


   
print(analyser_ventes(lst_nb))
