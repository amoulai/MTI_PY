#######################
# a = 12
# b = 13.57
# c = True
# d = 12 + 3j
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))

########################

# mystr = 'Salam Alykom!'
# mylist = [1, 2, 3, 4, 5, 6, 7]
# mytuple = (80, 'TD', 15, 'Cours')
# print(type(mystr))
# print(type(mylist))
# print(type(mytuple))

########################


# my_tuple = (10, 'Hello', 45, 'Hi')
# my_dict = {1: 'One', 2: 'Two', 3: 'Three'}
# if type(my_tuple) is not type(my_dict):
#     print("Both variables have different object types.")
# else:
#     print("Same Object type")
#
# a = type('Test', (object,), dict(x='Hello', y=10, z='World'))
# print(type(a))
# print(vars(a))


########################

def calculate(x, y, op='sum'):
    if not isinstance(x, int) and isinstance(y, int):
        print(f'Invalid Types of Arguments - x:{type(x)}, y:{type(y)}')
        raise TypeError('Incompatible types of arguments, must be integers')

    if op == 'diff':
        return x - y
    if op == 'mult':
        return x * y
    # default is sum
    return x + y


print(calculate(3.5, 5))
