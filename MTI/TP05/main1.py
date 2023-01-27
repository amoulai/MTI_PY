class model:
    def __init__(self):
        self.annuaire = [
            {'prenom': 'Ahmed', 'nom': 'Mahdi', 'tel': '0778787887'},
            {'prenom': 'Mohamed', 'nom': 'Mahdi', 'tel': '0778787887'},
            {'prenom': 'Mounir', 'nom': 'Katibi', 'tel': '0778787887'},
            {'prenom': 'Noui', 'nom': 'Brahimi', 'tel': '0778787887'},
        ]

    def rechercher(self, nom):
        """ Recherche un tel par nom"""
        # La liste des personnes trouvées

        personnes = []
        for persn in self.annuaire:
            # afficher toutes les personnes qui ont le nom donné
            if persn['nom'] == nom:
                personnes.append(persn)
            # retourner une liste de dictionnaires
        return personnes

    def get_all(self):
        """ rechercher un tel par nom"""
        # La liste des personnes trouvées

        personnes = []
        for persn in self.annuaire:
            # afficher toutes les personnes
            personnes.append(persn)
        # un tableau avec des noms des champs
        return personnes


class view:
    def __init__(self, ):
        pass

    def input(self, ):
        """ recuperer le nom à rechercher"""
        print("Recherche d'un telephone")
        print("Introduire Un nom")
        nom = input()
        return nom

    def output(self, personnes):
        """ Afficher les informations d'une liste des personnes"""
        print("La liste des noms trouvés")
        print(" %d personnes trouvées" % len(personnes))
        for pers in personnes:
            print(pers['nom'], pers['prenom'], pers['tel'])

    def out_all(self, personnes):
        """ Afficher les informations d'une liste des personnes"""
        print("La liste des tous les noms :")
        for pers in personnes:
            print(pers['nom'], pers['prenom'], pers['tel'])


def controleur():
    # Ce programme permet de recherche le num dans un tableau par son nom et afficher
    # lire des données à partir du clavier.
    data_model = model()
    affichage = view()
    """ rechercher un nom """
    nom = affichage.input()
    personnes = data_model.rechercher(nom)
    affichage.output(personnes)
    # personnes = data_model.get_all()
    # affichage.out_all(personnes)


if __name__ == '__main__':
    controleur()
