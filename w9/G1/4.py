""" """


class Student:
    """ This is Student class """

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def hello(self):
        print('hello from student')

    def __str__(self):
        return '{}, {}'.format(self.name, self.gpa)


s1 = Student('student 1', 3.5)
s2 = Student('student 2', 3.7)

print(s2)
