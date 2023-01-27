import xml.dom.minidom as minidom
import sys

DATA_FILE = 'annuaire-v0.1.xml'


def treat_doc(xmldoc):
    # get the annuaire list
    annuaire = xmldoc.getElementsByTagName('annuaire')[0]
    # print(annuaire)
    cpt = 0
    # display personne by personne
    for personne in annuaire.childNodes:
        print("-" * 40)
        print("Personne n°", cpt)
        print(personne.toxml())
        cpt += 1


def display_tel(xmldoc):
    # display only telephones
    # get the tel list
    telephones = xmldoc.getElementsByTagName('telephone')
    print(telephones)
    cpt = 0
    # display tel by tel
    for tel in telephones:
        print("-" * 40)
        print("Tel n°", cpt)
        print(tel.toxml())
        print("N°:", tel.firstChild.data)
        print("Type:", tel.getAttribute("type"))
        cpt += 1


def display_tel_personne(xmldoc):
    # get the personnes list
    personnes = xmldoc.getElementsByTagName('personne')
    print(personnes)
    cpt = 0
    # display telephone by personne
    for personne in personnes:
        print("-" * 40)
        print("Personne n°", cpt)
        nom = personne.getElementsByTagName('nom')[0]
        prenom = personne.getElementsByTagName('prenom')[0]
        tels = personne.getElementsByTagName('telephone')
        print("*" * 20)
        print("Nom:\t", nom.firstChild.data)
        print("Prénom:\t", prenom.firstChild.data)
        for tel in tels:
            print("-" * 20)
            print("N°:", tel.firstChild.data)
            print("Type:", tel.getAttribute("type"))
        cpt += 1


def add_id_personne(xmldoc):
    # get the personnes list
    personnes = xmldoc.getElementsByTagName('personne')
    print(personnes)
    cpt = 0
    # display personne by personne
    for personne in personnes:
        print("-" * 40)
        print("Personne n°", cpt, personne.nodeValue, personne.nodeType, personne.setAttribute('id', str(cpt)))
        cpt += 1
        print(personne.toxml())


def main():
    try:
        xmldoc = minidom.parse(DATA_FILE)
    except:
        print("Can't Open the file")
        sys.exit()
    print(xmldoc.toxml())
    # treat_doc(xmldoc)
    # display_tel(xmldoc)
    # display_tel_personne(xmldoc)
    # add_id_personne(xmldoc)
    return 0


if __name__ == '__main__':
    main()
