import sys


class model_fichier:
    """ Classe de model de donnée"""

    def __init__(self):
        self.annuaire = []
        try:
            myfile = open("annuaire.txt", "r")
        except:
            print("Can't open DataFile")
            sys.exit()
        lines = myfile.readlines()
        for line in lines:
            line = line.strip('\n')
            fields = line.split('\t')
            personne = {"nom": fields[0], "prenom": fields[1], "tel": fields[2]}
            self.annuaire.append(personne)
        myfile.close()

    def __del__(self, ):
        """ Destructeur de la classe Modele,
        Il est appelé à la fin de programme
        recharger les donnes dans le fichier """
        try:
            myfile = open("annuaire.txt", "w")
        except:
            print("Can't open DataFile")
            sys.exit()
        for personne in self.annuaire:
            line = personne['nom'] + '\t' + personne['prenom'] + '\t' + personne['tel'] + "\n"
            myfile.write(line)
        myfile.close()

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

    def ajouter(self, nom, prenom, tel):
        """ ajouter une personne """
        personne = {}
        personne["nom"] = nom
        personne["prenom"] = prenom
        personne["tel"] = tel
        self.annuaire.append(personne)


def main():
    data_model = model_fichier()
    personnes = data_model.get_all()
    for person in personnes:
        print(person)


if __name__ == "__main__":
    main()
