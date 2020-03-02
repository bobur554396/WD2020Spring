# Classes

class Person: # CamelCase
    """This is Person class"""

    # magic methods
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_ame(self): # snake case
        return self.name

    def __str__(self):
        return '{}, {}'.format(self.name, self.age)


class Student(Person):
    def __init__(self, name, age, gpa):
        super(name, age)
        self.gpa = gpa


p = Person('Person 1', 18)

print(p.get_name())
