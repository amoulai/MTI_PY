class Product:
    def __init__(self):
        print("Instance Created")
        # Defining __call__ method

    def __call__(self, a, b):
        print(a * b)


# Instance created
ans = Product()

# __call__ method will be called
ans(10, 20)

#################################

print("Is str callable? ", callable(str))
# str class
print("Is len callable? ", callable(len))
# len function
print("Is list callable? ", callable(list))
# list class
num = 10
print("Is variable callable? ", callable(num))


####################################

# class student:
#     def greet(self):
#         print("Hello there")
#
#
# std = student()
# print("Is student class callable? ", callable(student))
# print("Is student.greet() callable? ", callable(std.greet))
# print("Is student instance callable? ", callable(std))


###############################################

class student:
    def greet(self):
        print("Hello there")

    def __call__(self):
        print("Hello, I am a student.")


std = student()
print("Is student instance callable? ", callable(std))
print(std())
