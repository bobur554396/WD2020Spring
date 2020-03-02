# Classes

class Person: # CamelCase
    # magic methods
    def __init__(self, name, age):
        # print('init method from Person class')
        self.name = name
        self.age = age

    def get_name(self): # snake case
        return self.name

    def get_age(self):
        return self.age

    @staticmethod
    def sum(a, b):
        return a + b

    def __str__(self):
        return '{}, {}'.format(self.name, self.age)


class Student(Person):
    def __init__(self, name, age, gpa):
        # super(Student, self).__init__(name, age)
        super(name, age)
        self.gpa = gpa

    def recalculate_gpa(self):
        pass


p1 = Person('Person 1', 18)
p2 = Person('Person 1', 20)
print(p1)


class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


d = D()
