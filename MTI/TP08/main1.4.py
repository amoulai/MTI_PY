import random

print("The random library's contents are as follows::")
print(dir(random))
number = [1, 2, 3]
print(dir(number))


class Student():
    def __init__(self, x):
        return self.x  # Calling function

    def __dir__(self):
        return [10, 20, 30]


# att = dir(Student)
# print(att)

s = Student
att = dir(s)
print(att)
