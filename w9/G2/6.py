class Person:
    # magic methods
    def __init__(self, name, age):
        # print ('init method from Person class')
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self): # snake case
        return self.age

    def __str__(self):
        return '{}, {}'.format(self.name, self.age)


class Student(Person):
    def __int__(self, name, age, gpa):
        super(Student, self).__init__(name, age)
        self.gpa = gpa

    def recalculate_gpa(self):
        pass


p1 = Person('Person 1', 18)
print(p1)
