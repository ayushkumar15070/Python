# Encapsulation means protecting a data inside a class

# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age

# c1 = person("Ayush", 20)
# print(c1.name)
# print(c1.__age)



class person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

c1 = person("Ayush", 20)

print(c1.name)
print(c1.get_age())

class Student:
    def __init__(self, name, classname):
        self.name = name
        self.classname = classname

    def getclassname(self):
        return self.classname

c2 = Student("Ayush", "CS-2C")

print(c2.name)
print(c2.getclassname())

