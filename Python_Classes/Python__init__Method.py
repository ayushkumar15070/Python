class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = person("Ayush", 34)

print(p1.name)
print(p1.age)


# Without using that init 

class person:
    pass

p1 = person()
p1.name = "Ayush"
p1.age = 26

print(p1.name)
print(p1.age)


#With init

class person1:
    def __init__(self, name, age, hobby, talent, ambition):
        self.name = name
        self.age = age
        self.hobby = hobby
        self.talent = talent
        self.ambition = ambition

firstname = input("Enter your first name: ")
yesorno = input("Do you have any middle name: ")
if yesorno.casefold() == "yes":
    middlename = input("Enter your middle name: ")
else:
    middlename = ""

lastname = input("Enter your last name: ")

name = f"{firstname} {middlename} {lastname}"

age = int(input("Enter your age: "))
hobby = input("Enter your hobby: ")
talent = input("Enter your talent: ")
ambition = input("Enter your biggest ambition: ")

p1 = person1(name, age, hobby, talent, ambition)

print(f"Your full name is {p1.name} and your age is {p1.age}, your hobby is {p1.hobby}, your talent is {p1.talent}, your ambition is {p1.ambition}")

