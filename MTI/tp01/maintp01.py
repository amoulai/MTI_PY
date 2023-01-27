import sys


def insert_table_rows(data_table, file):
    for row in data_table:
        file.write("<tr>")
        for element in row:
            file.write("<td>" + str(element) + "</td>")
        file.write("</tr>")


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


def tokenize3(text):
    """
    Convert text into tokens, return a matrix of tokens(words)
    """
    tokens = []
    for line in text:
        token = line.split("\t")
        tokens.append(token)
    return tokens


def write_html_body(html_file, name):
    html_file.write(f"""
        <!doctype html>
        <html>
            <head>
                <title>{name}</title>
            </head>
        <body>
    """)


def close_html(html_file):
    html_file.write("""
            </body>
        </html>
    """)


def create_table(html_file, name):
    html_file.write(f"""
    <h1>{name}</h1>
        <table border="1">
    """)


def close_table(html_file):
    html_file.write("</table>")


def add_column(table, col_nbr, col_name):
    table = [element + [0] for element in table]
    table[0][col_nbr] = col_name
    return table


def calculate_cc(data_file):
    for i in range(1, len(data_file)):
        assiduite = \
            3 - (float(data_file[i][7]) - float(data_file[i][8]))
        if assiduite < 0:
            assiduite = 0
        data_file[i][14] = \
            str(format(assiduite + float(data_file[i][9]) +
                       float(data_file[i][10]) + float(data_file[i][11]), ".2f"))


def calculate_moy(data_file):
    for i in range(1, len(data_file)):
        data_file[i][15] = \
            str(format(float(data_file[i][14]) * 0.4 + float(data_file[i][12]) * 0.6, ".2f"))


def calculate_ratt(data_file):
    for i in range(1, len(data_file)):
        if float(data_file[i][15]) >= 10 or data_file[i][13] == "None":
            data_file[i][16] = ""
        else:
            data_file[i][16] = \
                str(format(float(data_file[i][14]) * 0.4 + float(data_file[i][13]) * 0.6, ".2f"))


def calculate_result(data_file):
    for i in range(1, len(data_file)):
        assiduite = \
            3 - (float(data_file[i][7]) - float(data_file[i][8]))
        if assiduite <= 0:
            data_file[i][17] = "exlus"
        elif float(data_file[i][15]) >= 10:
            data_file[i][17] = "admis session1"
        elif data_file[i][16] == "" and float(data_file[i][15]) <= 10:
            data_file[i][17] = "ajournee"
        elif float(data_file[i][16]) >= 10:
            data_file[i][17] = "admis session2"
        else:
            data_file[i][17] = "ajournee"


def calculate_statistique(data_file):
    nbr_admis1 = nbr_admis2 = nbr_ajr = nbr_exclus = 0
    for i in range(1, len(data_file)):
        if data_file[i][17] == "admis session1":
            nbr_admis1 += 1
        elif data_file[i][17] == "admis session2":
            nbr_admis2 += 1
        elif data_file[i][17] == "ajournee":
            nbr_ajr += 1
        else:
            nbr_exclus += 1
    return nbr_admis1, nbr_admis2, nbr_ajr, nbr_exclus


def main():
    data = read_file("tp01/suivi_etudiant.txt")
    data_table = tokenize3(data)
    data_table = add_column(data_table, len(data_table[0]), "CC")
    calculate_cc(data_table)
    data_table = add_column(data_table, len(data_table[0]), "moyenne")
    calculate_moy(data_table)
    data_table = add_column(data_table, len(data_table[0]), "moyenne_ratt")
    calculate_ratt(data_table)
    data_table = add_column(data_table, len(data_table[0]), "resulta")
    calculate_result(data_table)
    file = open("tp01/tp01_suivi_etudiant.html", "w")
    write_html_body(file, "TP01")
    create_table(file, "leste des etudiants:")
    insert_table_rows(data_table, file)
    close_table(file)
    nbr_admis1, nbr_admis2, nbr_ajr, nbr_exclus = calculate_statistique(data_table)
    file.write("<br/><h2>les statistiques: <h2/> ")
    file.write("<h3>nombre admis session 1  : " + str(nbr_admis1) + " </h3>")
    file.write("<h3>nombre admis session 2 : " + str(nbr_admis2) + "</h3>")
    file.write("<h3>nombre ajourne  : " + str(nbr_ajr) + "</h3>")
    file.write("<h3>nombre exclus : " + str(nbr_exclus) + "</h3>")
    close_html(file)
    file.write("<br/><h2>Liste des etudiant  ajournes <h2/>")
    file.write("<table border=\"1\"><tr></tr>")
    file.write("""<tr>
        <td>nom</td>
        <td>prenom</td>
        </tr>
    """)
    for i in range(1, len(data_table)):
        if data_table[i][17] == "ajournee":
            file.write("<TR>")
            file.write("<td>" + str(data_table[i][5]) + "</td>")
            file.write("<td>" + str(data_table[i][6]) + "</td>")
            file.write("</TR>")
    file.write("""</table>""")
    file.close()


if __name__ == "__main__":
    main()
