from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E, Text, Listbox, OptionMenu
from tkinter import StringVar
from model_fichier import model_fichier


class view_tk:
    def __init__(self, model):
        master = Tk()
        self.master = master
        self.model = model
        master.title("Annuaire")
        self.entered_number = 0
        # ~ master.withdraw()
        master.clipboard_clear()
        master.clipboard_append('i can has clipboardz?')
        self.output_label = Label(master, text="Output")
        self.label = Label(master, text="Nom:")
        self.entry = Text(master, height=1, width=50)
        self.label_prenom = Label(master, text="Prenom:")
        self.entry_prenom = Text(master, height=1, width=50)
        self.label_tel = Label(master, text="Tel:")
        self.entry_tel = Text(master, height=1, width=50)
        self.output = Text(master, height=10, width=50)
        self.search_button = Button(master, text="Search", command=lambda: self.update("search"))
        self.add_button = Button(master, text="Add", command=lambda: self.update("add"))
        self.all_button = Button(master, text="Get All", command=lambda: self.update("get_all"))
        # LAYOUT
        self.label.grid(row=0, column=0, sticky=W)
        self.label_prenom.grid(row=0, column=1, sticky=W)
        self.label_tel.grid(row=0, column=2, sticky=W)
        # input nom
        self.entry.grid(row=1, column=0, columnspan=10, sticky=W + E)
        # prenom et tel
        self.entry_prenom.grid(row=1, column=1, columnspan=10, sticky=W + E)
        self.entry_tel.grid(row=1, column=2, columnspan=2, sticky=W + E)
        # command
        self.search_button.grid(row=2, column=0)
        self.add_button.grid(row=2, column=1)
        self.all_button.grid(row=2, column=2)
        # Output
        self.output_label.grid(row=3, column=0, sticky=E)
        # output
        self.output.grid(row=4, column=0, columnspan=5, sticky=W + E)

    def update(self, method):
        nom = self.entry.get("1.0", END).strip()
        prenom = self.entry_tel.get("1.0", END)
        tel = self.entry_tel.get("1.0", END)
        # clean ends of words
        nom = nom.strip()
        prenom = prenom.strip()
        tel = tel.strip()
        if method == "search":
            result = self.search(nom)
        elif method == "add":
            result = self.add(nom, prenom, tel)
        elif method == "get_all":
            result = self.get_all()
        else:  # reset
            print("method", method)
            result = nom
        self.output.insert(END, str(result))

    def add(self, nom, prenom, tel):
        return self.model.ajouter(nom, prenom, tel)

    def search(self, nom):
        result = self.model.rechercher(nom)
        if result:
            return result
        else:
            return "'%s' not found" % nom

    def get_all(self):
        return self.model.get_all()

    def run(self):
        self.master.mainloop()


def controleur3():
    data_model = model_fichier()
    affichage = view_tk(data_model)
    affichage.run()


if __name__ == '__main__':
    controleur3()
