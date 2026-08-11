# The self parameter is a reference to the current instance of class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        

    def printing(self):
        print(f"Your name is {self.name} and your age is {self.age}")

name = input("Enter your name: ")
age = input("Enter your age: ")

p1 = Person(name, age)

p1.printing()