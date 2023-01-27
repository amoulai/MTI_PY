annuaire = [
    {'prenom': 'Ahmed', 'nom': 'Mahdi', 'tel': '077878'},
    {'prenom': 'Mohamed', 'nom': 'Rabehi', 'tel': '06678'},
    {'prenom': 'Mounir', 'nom': 'Mahdi', 'tel': '0556644'},
    {'prenom': 'Noui', 'nom': 'Brahimi', 'tel': '067879'},
]


def main():
    # Ce programme permet de recherche le num dans un tableau par son nom et afficher
    # lire des données à parti du clavier.
    print("Recherche d'un telephone")
    print("Introduire Un nom")
    in_nom = input()
    # nombre d'elements trouvés
    nb_found = 0
    # parcours des noms
    for val in annuaire:
        # afficher toutes les personnes qui ont le nom donné
        if val['nom'] == in_nom:
            print(in_nom, val['prenom'], val['tel'])
            nb_found += 1
    if not nb_found:
        print("ce nom %s n'existe pas " % in_nom)


if __name__ == '__main__':
    main()
