# class A:
#     pass
#
#
# # ajouter dynamiquement un attribut à la classe A
# A.x = 1
# a = A()
# # ajouter dynamiquement un attribut à la l'objet a
# a.y = 2
# print("Attributs de la classe A: ", vars(A))
# print("Attributs de l'instance a: ", vars(a))

##################################

# def init(self):  # the function and argument can have any name
#     self.x = 1
#
#
# class A:
#     pass
#
#
# setattr(A, '__init__', init)
# a = A()
# print(a.x)

###################################


def test():
    return "Test old code"


print(test())
# ~ test.__code__ = (lambda x : print("Hello", x)).__code__
test.__code__ = (lambda: "Test new code").__code__
print(test())
