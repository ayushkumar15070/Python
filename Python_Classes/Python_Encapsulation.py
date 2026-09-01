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