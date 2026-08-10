# Python is an object-oriented programming language, allowing you to structure your code using classes and objects for better organization and reusability. 

# Advantage of OOPs
# 1. Provides a clear structure to programs
# 2. Makes code easier to maintain, reuse, and debug
# 3. Helps keep your code DRY( Don't Repeat Yourself)
# 4. Allows you to build reusable applications with less code


# examples of OOPs in Python

class Myclass:
    x = 5
    y = 10
    z = 15



p1 = Myclass()
print(p1.x)

p2 = Myclass()
print(p2.x)
print(p2.y)
print(p2.z)

print(p2.x * p2.y * p2.z)



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello {self.name}, How are you?")
        print(f"You will be a billionaire by the age of {age + 5 if age == 20 else age + 4}")


name = input("Enter your name: ")
age = int(input("Enter your age: "))
p1 = Person(name, age)

p1.greet()