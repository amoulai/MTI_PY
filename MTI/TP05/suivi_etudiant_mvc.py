import xml.dom.minidom as minidom
import sys


class model:

    def __init__(self):
        self.DATA_FILE = 'suivi_etudiant.xml'
        try:
            self.xmldoc = minidom.parse(self.DATA_FILE)
        except:
            print("Can't Open the file")
            sys.exit()

    def get_value(self, elment):
        values = self.xmldoc.getElementsByTagName(elment)
        value_list = []
        for value in values:
            try:
                val = float(value.firstChild.data)
            except:
                val = "    "
            value_list.append(val)
        return value_list

    def add_ele(self, etudiants, doc_root, obj_list, ele_name):
        for etudiant, ele in zip(etudiants, obj_list):
            element = self.xmldoc.createElement(ele_name)
            element.appendChild(self.xmldoc.createTextNode(str(ele)))
            etudiant.appendChild(element)
            doc_root.appendChild(etudiant)
        return doc_root

    def update_xmldoc(self, calcul_list, name_list):
        etudiants = self.xmldoc.getElementsByTagName("etudiant")
        doc_root = self.xmldoc.createElement("suivietudiant")
        for calc, name in zip(calcul_list, name_list):
            self.add_ele(etudiants, doc_root, calc, name)
        self.xmldoc = doc_root


class view:
    def __init__(self):
        pass

    def affichier_liste_etudiants(self, xmldoc):
        etudiants = xmldoc.getElementsByTagName("etudiant")

        print("\t", "+------------------------------+")
        print("\t", "|  La liste des Étudiants:     |")
        print("\t", "+------------------------------+")
        print()
        for etudiant in etudiants:
            print("-"*40)
            print("\t\tniveau: ", etudiant.getElementsByTagName("niveau")[0].firstChild.data)
            print("\t\tspecialite: ", etudiant.getElementsByTagName("specialite")[0].firstChild.data)
            print("\t\tgroupe: ", etudiant.getElementsByTagName("groupe")[0].firstChild.data)
            print("\t\tmatricule: ", etudiant.getElementsByTagName("matricule")[0].firstChild.data)
            print("\t\tNom: ", etudiant.getElementsByTagName("nom")[0].firstChild.data)
            print("\t\tPrenom: ", etudiant.getElementsByTagName("prenom")[0].firstChild.data)
            print("\t\tnb_seances: ", etudiant.getElementsByTagName("nb_seances")[0].firstChild.data)
            print("\t\tnb_presence: ", etudiant.getElementsByTagName("nb_presence")[0].firstChild.data)
            print("\t\tpart: ", etudiant.getElementsByTagName("part")[0].firstChild.data)
            print("\t\ttest1: ", etudiant.getElementsByTagName("test1")[0].firstChild.data)
            print("\t\ttest2: ", etudiant.getElementsByTagName("test2")[0].firstChild.data)
            print("\t\texam: ", etudiant.getElementsByTagName("exam")[0].firstChild.data)
            print("\t\trattrapage: ", etudiant.getElementsByTagName("rattrapage")[0].firstChild.data)
            print("\t\tCC: ", etudiant.getElementsByTagName("CC")[0].firstChild.data)
            print("\t\tmoyenne: ", etudiant.getElementsByTagName("moyenne")[0].firstChild.data)
            print("\t\tmoyenne_ratt: ", etudiant.getElementsByTagName("moyenne_ratt")[0].firstChild.data)
            print("\t\tresulta: ", etudiant.getElementsByTagName("resultat")[0].firstChild.data)
            print("-"*40)


    def affichier_les_statistiques(self, xmldoc):
        ads1 = xmldoc.getElementsByTagName("damis_S1")[0]
        ads2 = xmldoc.getElementsByTagName("damis_S2")[0]
        ajr = xmldoc.getElementsByTagName("Ajournner")[0]
        exl = xmldoc.getElementsByTagName("exclu")[0]
        print("\t" * 8, "+------------------------------+")
        print("\t" * 8, "|  La liste des statistique:   |")
        print("\t" * 8, "+------------------------------+")
        print()
        print("\t\t", "+" + "------------------+" * 4)
        print("\t\t |  Admis session1  |  Admis session2  |     Ajourner     |      exclus      |")
        print("\t\t", "+" + "------------------+" * 4)
        print("\t\t |    \t", ads1.firstChild.data, "\t    |  \t\t", ads2.firstChild.data, "\t   |  \t\t",
              ajr.firstChild.data, "\t\t  |  \t\t", exl.firstChild.data, "\t |")
        print("\t\t", "+" + "------------------+" * 4)


class controller:
    def __init__(self):
        self.data_model = model()
        self.affichage = view()

    def calculate_cc(self):
        nb_seances_list = self.data_model.get_value("nb_seances")
        nb_presence_list = self.data_model.get_value("nb_presence")
        part_list = self.data_model.get_value("part")
        test1_list = self.data_model.get_value("test1")
        test2_list = self.data_model.get_value("test2")

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

    def calculate_moy(self, cc_notes_listes):
        exam_notes_list = self.data_model.get_value("exam")
        moy_liste = []
        for cc, exam in zip(cc_notes_listes, exam_notes_list):
            moy = float(format((cc * 0.4) + (exam * 0.6), ".2f"))
            moy_liste.append(moy)
        return moy_liste

    def calculate_ratt(self, cc_notes_liste, moy_notes_liste):
        ratt_notes_list = self.data_model.get_value("rattrapage")
        moy_ratt_liste = []
        for cc, moy, ratt in zip(cc_notes_liste, moy_notes_liste, ratt_notes_list):
            if ratt == "    ":
                moy_ratt_liste.append("    ")
            elif ratt != "    " and moy < 10:
                moy_ratt = float(format((cc * 0.4) + (ratt * 0.6), ".2f"))
                moy_ratt_liste.append(moy_ratt)
        return moy_ratt_liste

    def calculate_result_and_stat(self, nb_abs_liste, moy_notees_liste, ratt_notes_liste):
        global resulta
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
            resulta = self.data_model.xmldoc.createElement("resulta")
            for stat, ele in zip(statistiques, statistiques_names):
                element = self.data_model.xmldoc.createElement(ele)
                element.appendChild(self.data_model.xmldoc.createTextNode(str(stat)))
                resulta.appendChild(element)

        return resulta_liste, resulta

    def main(self):
        cc_notes_liste, nb_abs_liste = self.calculate_cc()
        moy_notes_liste = self.calculate_moy(cc_notes_liste)
        ratt_notes_liste = self.calculate_ratt(cc_notes_liste, moy_notes_liste)
        resulta_liste, statistiques = self.calculate_result_and_stat(nb_abs_liste, moy_notes_liste,
                                                                     ratt_notes_liste)

        calcul_list = [cc_notes_liste, moy_notes_liste, ratt_notes_liste, resulta_liste]
        name_list = ["CC", "moyenne", "moyenne_ratt", "resultat"]
        self.data_model.update_xmldoc(calcul_list, name_list)
        self.affichage.affichier_liste_etudiants(self.data_model.xmldoc)
        self.affichage.affichier_les_statistiques(statistiques)


if __name__ == '__main__':
    ctrl = controller()
    ctrl.main()
