class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname(self):
        print(self.firstname, self.lastname)


x = Person("Ayush", "Vishwakarma")

print(x.printname())


class Student(Person):
    pass

y = Student("Ayush", "Kumar")
print(y.printname())