class Student:
    def __init__(self, name='Leo', age=22, course='MBA', city='Mumbai'):
        self.Name = name
        self.Age = age
        self.Course = course
        self.City = city


obj = Student()
print('Dictionary output is:', vars(obj))
obj2 = obj = Student("Samir", 22, "MBB", "Bouira")
print('Dictionary output is:', vars(obj2))
