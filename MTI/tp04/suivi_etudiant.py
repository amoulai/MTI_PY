import xml.dom.minidom as minidom
import sys

DATA_FILE = 'suivi_etudiant.xml'


def get_value(xmldoc, elment):
    values = xmldoc.getElementsByTagName(elment)
    value_list = []
    for value in values:
        try:
            val = float(value.firstChild.data)
        except:
            val = "    "
        value_list.append(val)
    return value_list


def calculate_cc(xmldoc):
    nb_seances_list = get_value(xmldoc, "nb_seances")
    nb_presence_list = get_value(xmldoc, "nb_presence")
    part_list = get_value(xmldoc, "part")
    test1_list = get_value(xmldoc, "test1")
    test2_list = get_value(xmldoc, "test2")

    nb_abs_liste = []
    for nb_seances, nb_presence in zip(nb_seances_list, nb_presence_list):
        nb_abs = nb_seances - nb_presence
        if nb_abs >= 3:
            note_abs = 0
        else:
            note_abs = 3 - nb_abs
        nb_abs_liste.append(note_abs)
    cc_notes_liste = []
    for abs, part, test1, test2 in zip(nb_abs_liste, part_list, test1_list, test2_list):
        cc_note = abs + part + test1 + test2
        cc_notes_liste.append(cc_note)
    return cc_notes_liste, nb_abs_liste


def calculate_moy(xmldoc, cc_notes_listes):
    exam_notes_list = get_value(xmldoc, "exam")
    moy_liste = []
    for cc, exam in zip(cc_notes_listes, exam_notes_list):
        moy = float(format((cc * 0.4) + (exam * 0.6), ".2f"))
        moy_liste.append(moy)
    return moy_liste


def calculate_ratt(xmldoc, cc_notes_liste, moy_notes_liste):
    ratt_notes_list = get_value(xmldoc, "rattrapage")
    moy_ratt_liste = []
    for cc, moy, ratt in zip(cc_notes_liste, moy_notes_liste, ratt_notes_list):
        if ratt == "    ":
            moy_ratt_liste.append("    ")
        elif ratt != "    " and moy < 10:
            moy_ratt = float(format((cc * 0.4) + (ratt * 0.6), ".2f"))
            moy_ratt_liste.append(moy_ratt)
    return moy_ratt_liste


def calculate_result_and_stat(xmldoc, nb_abs_liste, moy_notees_liste, ratt_notes_liste):
    resulta_liste = []
    s1_cpt, s2_cpt, aj_cpt, ex_cpt = 0, 0, 0, 0
    for abs, moy, ratt in zip(nb_abs_liste, moy_notees_liste, ratt_notes_liste):
        if abs == 0:
            resulta_liste.append("exclu")
            ex_cpt += 1
        elif moy >= 10:
            resulta_liste.append("Admis S1")
            s1_cpt += 1
        elif ratt != "    " and ratt >= 10:
            resulta_liste.append("Admis S2")
            s2_cpt += 1
        else:
            resulta_liste.append("Ajourner")
            aj_cpt += 1
        statistiques = [s1_cpt, s2_cpt, aj_cpt, ex_cpt]
        statistiques_names = ["damis_S1", "damis_S2", "Ajournner", "exclu"]
        resulta = xmldoc.createElement("resulta")
        for stat, ele in zip(statistiques, statistiques_names):
            element = xmldoc.createElement(ele)
            element.appendChild(xmldoc.createTextNode(str(stat)))
            resulta.appendChild(element)

    return resulta_liste, resulta


def add_ele(xmldoc, etudiants, doc_root, obj_list, ele_name):
    for etudiant, ele in zip(etudiants, obj_list):
        element = xmldoc.createElement(ele_name)
        element.appendChild(xmldoc.createTextNode(str(ele)))
        etudiant.appendChild(element)
        doc_root.appendChild(etudiant)


def main():
    try:
        xmldoc = minidom.parse(DATA_FILE)
    except:
        print("Can't Open the file")
        sys.exit()

    cc_notes_liste, nb_abs_liste = calculate_cc(xmldoc)
    moy_notes_liste = calculate_moy(xmldoc, cc_notes_liste)
    ratt_notes_liste = calculate_ratt(xmldoc, cc_notes_liste, moy_notes_liste)
    resulta_liste, statistiques = calculate_result_and_stat(xmldoc, nb_abs_liste, moy_notes_liste, ratt_notes_liste)

    etudiants = xmldoc.getElementsByTagName("etudiant")
    doc_root = xmldoc.createElement("suivietudiant")
    calcul_list = [cc_notes_liste, moy_notes_liste, ratt_notes_liste, resulta_liste]
    name_list = ["CC", "moyenne", "moyenne_ratt", "resultat"]
    for calc, name in zip(calcul_list, name_list):
        add_ele(xmldoc, etudiants, doc_root, calc, name)
    suivi_etudiant = open("tp4-suivi_etudiant-v2.xml", 'w')
    suivi_etudiant.write(doc_root.toxml())
    suivi_etudiant.close()
    resulta = open("statistiques.xml", 'w')
    resulta.write(statistiques.toxml())
    resulta.close()
    return 0


if __name__ == '__main__':
    main()
