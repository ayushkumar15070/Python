def myfunct():
    print("This is the function block")

def myanotherfunct():
    print("This is another function block")


myfunct()
myanotherfunct()


i = 0

while i < 34:
    myfunct()
    myanotherfunct()
    i = i + 1

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def division(a, b):
    return a / b

def multiplication(a, b):
    return a * b

print(addition(23, 34))
print(subtraction(23, 34))
print(division(23, 34))
print(multiplication(23, 34))


def area(radius):
     return 3.14 * radius * radius

print(area(23))


def student_info(name, department, year, /):
    print("Name: ", name)
    print("Department: ", department)
    print("Year: ", year)

student_info("Neha", "ECE", 3)


def calculate_bill(price, quantity = 1, tax_rate = 5):
    subtotal = price * quantity
    tax = subtotal * tax_rate / 100
    return subtotal + tax

print(calculate_bill(1000))
print(calculate_bill(1000, 3))
print(calculate_bill(1000, 3, 12))


def calculate(a, b):
    return a + b, a - b, a * b

result = calculate(12, 5)
print(result)
print(type(result))


total, difference, product = calculate(12, 5)
print(total, difference, product)

def total_marks(*marks):
    print("Received: ", marks)
    return sum(marks)

print(total_marks(70, 80, 90))
print(total_marks(65, 72, 81, 88, 94))

def student_profile(**details):
    print("Received", details)


student_profile(name = "Rohan", branch = "ECE", semester = 6)


def demo(name, *scores, city = "Unknown", **extra):
    print("Name: ", name)
    print("Scores:", scores)
    print("City: ", city)
    print("Extra: ", extra)


demo("Ankit", 78, 85, 91, city = "Kanpur", semester = 6, branch = "ECE")