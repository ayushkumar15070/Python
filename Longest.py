a = "Ayush"
b = "Kumar"
c = "Vishwakarma"

print(a + b + c)

def addition(*args):
    result = []
    sum = 0
    for i in args:
        result.append(i)

    for i in args:
        sum = sum + i

    return sum

print(addition(10, 10, 10, 10, 10))


str1 = "888999"
str2 = "343"
list1 = []
list2 = []


while len(str1) != len(str2):
    if len(str1) > len(str2):
        str2 = " " + str2
    else:
        str1 = " " + str1

for i in str1:
    if i == "1":
        list1.append(1)
    elif i == "2":
        list1.append(2)
    elif i == "3":
        list1.append(3)
    elif i == "4":
        list1.append(4)
    elif i == "5":
        list1.append(5)
    elif i == "6":
        list1.append(6)
    elif i == "7":
        list1.append(7)
    elif i == "8":
        list1.append(8)
    elif i == "9":
        list1.append(9)
    else:
        list1.append(0)


for i in str2:
    if i == "1":
        list2.append(1)
    elif i == "2":
        list2.append(2)
    elif i == "3":
        list2.append(3)
    elif i == "4":
        list2.append(4)
    elif i == "5":
        list2.append(5)
    elif i == "6":
        list2.append(6)
    elif i == "7":
        list2.append(7)
    elif i == "8":
        list2.append(8)
    elif i == "9":
        list2.append(9)
    else:
        list2.append(0)


print(list1)
print(list2)

name = input("Enter your name: ")
age = int(input("Enter your age: "))
gender = input("Enter your gender: ")
address = input("Enter your address")