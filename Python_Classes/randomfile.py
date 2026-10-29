# create a class rectangle with parameterised constructor that accept length nd breadth you have  to add method to calculate area nd parameter
class Rectangle:
    def __init__(self, length, breadth):
        
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
       
        return self.length * self.breadth

    def calculate_perimeter(self):
        
        
        return 2 * (self.length + self.breadth)

if __name__ == "__main__":
    my_rectangle = Rectangle(10, 5)

    area = my_rectangle.calculate_area()
    perimeter = my_rectangle.calculate_perimeter()

    print(f"Rectangle Dimensions: Length = {my_rectangle.length}, Breadth = {my_rectangle.breadth}")
    print(f"Area of the Rectangle: {area}")
    print(f"Perimeter of the Rectangle: {perimeter}")


# demonstrate single inheritance ... create a base class  person that has  name,age and employees that has salary attribute nd display the class

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def display_person_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Employee(Person):
    def __init__(self, name: str, age: int, salary: float):
        super().__init__(name, age)
        self.salary = salary

    def display_employee_info(self):
        self.display_person_info()
        print(f"Salary: ${self.salary:,}")


if __name__ == "__main__":
    emp = Employee(name="Alice Smith", age=30, salary=85000)
    print("--- Employee Details ---")
    emp.display_employee_info()
