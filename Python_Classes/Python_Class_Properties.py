class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Ayush", 20)

del p1.age

print(p1.name)


class person1:
    species = "Human"

    def __init__(self, name):
        self.name = name 


p1 = person1("Ayush")

p2 = person1("Rahul")

print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)