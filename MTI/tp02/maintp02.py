import sys


def read_file(filename):
    """
    Read a text from file
    """
    try:
        fl = open(filename, "r")
    except:
        print("Can't open file ", filename)
        sys.exit()
    # if success
    return fl


def tokenize4(text):
    """
    Convert text into tokens, return a matrix of tokens(words)
    """
    tokens = []
    for line in text:
        token = line.split("\t")
        elements = []
        for element in token:
            elements.append(element.replace("\n", ""))
        tokens.append(elements)
    return tokens


def insert_xml_elements(xml_file, data_table):
    for i in range(1, len(data_table)):
        xml_file.write("\t<etudiant>\n")
        for j in range(0, len(data_table[0])):
            if str(data_table[0][j]) != "":
                xml_file.write("\t\t<" + str(data_table[0][j]) + ">"
                               + str(data_table[i][j])
                               + "</" + str(data_table[0][j])
                               + ">" + "\n")
        xml_file.write("\t</etudiant>\n")


def main():
    data = read_file("tp02/suivi_etudiant.txt")
    data_table = tokenize4(data)
    xml_file = open("tp02/suivi_etudiant.xml", "w")
    xml_file.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<suivietudiant>\n")
    insert_xml_elements(xml_file, data_table)
    xml_file.write("</suivietudiant>\n")
    xml_file.close()


if __name__ == "__main__":
    main()
