class Customer:
    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address

class Address:
    def __init__(self, city, state, pin):
        self.city = city
        self.state = state
        self.pin = pin

add = Address("Prayagraj", "Uttar Pradesh", 211003)
cust = Customer("Ayush", "male", add)
print(f"Your name is: {cust.name}")
print(f"Your gender is: {cust.gender}")
print(f"Your city is: {cust.address.city}")
print(f"Your state is: {cust.address.state}")
print(f"Your pin is: {cust.address.pin}")

class User:
    def login(self):
        print("Login here")
    def registration(self):
        print("Register here")

class Student(User):
    def read(self):
        print("Read")

class instructor(User):
    def write(self):
        print("Provide your content here")

    def evaluate(self):
        print("evaluate the assignment")

u = User()
stu = Student()
ins = instructor()

u.login
u.registration

stu.registration
stu.login
stu.read

ins.evaluate
ins.write


class SmartPhone:
    def __init__(self, price, brand, processor, camera, features):
        self.brand = brand
        self.price = price
        self.processor = processor
        self.camera = camera
        self.features = features

    def showdetails(self):
        print(f"The brand name is: {self.brand}")
        print(f"The price is: {self.price}")
        print(f"The processor is: {self.processor}")
        print(f"The camera is: {self.camera}")
        print(f"The features are: {self.features}")

    def another(self):
        print("This one is first")

class AnotherPhone(SmartPhone):
    def showanotherdetails(self):
        print("This process has been completed")

    def another(self):
        print("This one is second")
        super().another()

phone = SmartPhone(2000, "Samsung", "I8", "200MP", "Smartphone with Ai")
anotherphone = AnotherPhone(200000, "Apple", "M5 Max", "12MP", "Phone for Rich peoples because it gives class")


phone.showdetails()
anotherphone.showdetails()
anotherphone.another()
phone.another()




class Superclass:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def greet(self):
        print(f"Hello {self.name} your age is {self.age} and your gender is {self.gender}")


super = Superclass("Ayush", 20, "Male")

super.greet()


from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car is starting...")


car = Car()
car.start()
