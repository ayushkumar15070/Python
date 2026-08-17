class Person:
    def __init__(self, name, ):
        self.name = name

    def greet(self):
        print("Hello" + self.name)

p1 = Person("John")
print(p1.name)


class Calculator:
    def addition(seld, a, b):
        return a + b

    def subtraction(self, a, b):
        if a < b:
            return b - a
        else:
            return a - b


c1 = Calculator()

print(c1.addition(23, 44))
print(c1.subtraction(5, 23))



class person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def __str__(self):
        return f"{self.name} {self.age}"


p1 = person("Ayush", 20)
print(p1)