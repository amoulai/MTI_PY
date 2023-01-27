class Singleton(object):
    instance = None

    def __new__(cls):
        "Méthode de construction standard Python"
        if cls.instance is None:
            cls.instance = object.__new__(cls)
        return cls.instance


class file_create_Singleton(object):
    instance = None

    def __new__(cls):
        if cls.instance is None:
            file = open("test.txt", "w")
            return file
        else:
            return cls.file

monSingleton1 = file_create_Singleton()
monSingleton2 = file_create_Singleton()
# monSingleton1 et monSingleton2 renvoient à la même instance
# assert monSingleton1 is monSingleton2
print(monSingleton1, monSingleton2)
