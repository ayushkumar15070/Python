class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly")

car1 = Car("Ford", "Mustang")
boat1 = Boat("Lamborghini", "145S")
plane1 = Plane("Gulfstream", "G800")


for i in (car1, boat1, plane1):
    i.move()