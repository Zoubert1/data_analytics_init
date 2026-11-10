
import statistics as stats

lst_nb = [10005, 10, 1000, 60, 0, 770, 118]


# Fonction ajoutée par le binôme : calcul de l'étendue
def calculer_etendue(liste_nombre):
    """Calcule la différence entre la valeur maximale et minimale."""

    if len(liste_nombre) == 0:
        return None

    etendue = max(liste_nombre) - min(liste_nombre)
    return etendue


def analyser_ventes(transaction):
    """Analyse les transactions valides et retourne les indicateurs."""

    indicateurs = {}
    valide = []
    outliers = []

    # Filtrer les transactions invalides
    for nb in transaction:
        if nb <= 0:
            continue
        valide.append(nb)

    nb_transaction = len(valide)
    somme_transaction = sum(valide)

    # Calculer les indicateurs statistiques
    if nb_transaction > 0:
        moyenne_brute = stats.mean(valide)
        moyenne = round(moyenne_brute, 2)
        mediane = stats.median(valide)
        ecart_type = round(stats.stdev(valide), 2) if nb_transaction > 1 else None
        val_min, val_max = min(valide), max(valide)
        # Ajout de l'indicateur d'étendue à partir des transactions valides
        etendue = calculer_etendue(valide)

        # Repérer les outliers
        seuil_outlier = moyenne_brute * 2
        for nb in valide:
            if nb > seuil_outlier:
                outliers.append(nb)

    else:
        moyenne = None
        mediane = None
        ecart_type = None
        val_min = None
        val_max = None
        etendue = None

    # Dictionnaire des résultats
    indicateurs["transactions_valide"] = nb_transaction
    indicateurs["ventes_totales"] = somme_transaction
    indicateurs["moyenne"] = moyenne
    indicateurs["mediane"] = mediane
    indicateurs["ecart_type"] = ecart_type
    indicateurs["valeur_minimale"] = val_min
    indicateurs["valeur_maximale"] = val_max
    # Intégration de l'étendue au dictionnaire des résultats
    indicateurs["etendue"] = etendue
    indicateurs["outliers"] = outliers

    return indicateurs

resultat = analyser_ventes(lst_nb)
print(resultat)