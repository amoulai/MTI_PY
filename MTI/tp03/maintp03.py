from MTI.tp01 import maintp01 as m1
from MTI.tp02 import maintp02 as m2


def main():
    data_table = m2.read_file("suivi_etudiant.txt")
    data_table = m2.tokenize4(data_table)
    print(data_table)
    data_table = m1.add_column(data_table, len(data_table[0]), "CC")
    m1.calculate_cc(data_table)
    data_table = m1.add_column(data_table, len(data_table[0]), "moyenne")
    m1.calculate_moy(data_table)
    data_table = m1.add_column(data_table, len(data_table[0]), "moyenne_ratt")
    m1.calculate_ratt(data_table)
    data_table = m1.add_column(data_table, len(data_table[0]), "resulta")
    m1.calculate_result(data_table)
    xml_file = open("suivi_etudiant-v2.xml", "w")
    xml_file.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<suivietudiant>\n")
    m2.insert_xml_elements(xml_file, data_table)
    xml_file.write("</suivietudiant>\n")
    xml_file.close()


if __name__ == "__main__":
    main()
