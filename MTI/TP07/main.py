class Person:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom


class personne:
    def __init__(self, nomcomplet):
        self.nom = nomcomplet


class adapter(personne):
    def __init__(self, person, nomcomplet):
        super().__init__(nomcomplet)
        self.nom = person.nom + "-" + person.prenom


def main():
    # personne
    person_one = Person("Akli", "Mohand")
    per = adapter(person_one)
    print(per.nom)
    return 0


if __name__ == '__main__':
    main()
