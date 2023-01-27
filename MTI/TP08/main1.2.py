int_1 = 7
str_1 = "Learn Python"
list_1 = [2, 4, 6]
print("Is int_1 an integer? " + str(isinstance(int_1, int)))
print("Is int_1 a string? " + str(isinstance(int_1, str)))
print("Is str_1 a string? " + str(isinstance(str_1, str)))
print("Is list_1 an integer? " + str(isinstance(list_1, int)))
print("Is list_1 a list? " + str(isinstance(list_1, list)))
# test if its types is in a list
print("Is int_1 integer or list or string? " + str(isinstance(int_1, (list, str, int))))
print("Is list_1 string or tuple? " + str(isinstance(list_1, (str, tuple))))


class Test1:
    a = 6


testInstance = Test1()
print(isinstance(testInstance, Test1))
print(isinstance(testInstance, (list, tuple)))
print(isinstance(testInstance, (list, tuple, Test1)))
