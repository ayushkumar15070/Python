#Set
    # Storage of elements
    # Unordered
    # Unchangeable*
    # Don't allow duplicates
    # We use curly brackets while creating it

set1 = {1, 2, 3, 4, 5, 6}
set2 = {2, 3, 4, 5, 6}

print(set1.intersection(set2))

set3 = {1, 4, 2, 5, 3, 6}
print(set3)

set4 = {5, 4, 55, 44, 3, 23, 12, 43}
print(set4)

set5 = {"TATA","BMW", "Volvo", "Mercedes", 78, 78, 98, 9, 6, 0}

print(set5)

# set5.add(set4)
print(set5)

# set6 = set()

# i = 0
# howmany = int(input("how many data you want to enter: "))
# while i < howmany: 
#     data = (input("Enter the data: "))

#     if data.isdigit():
#         data = int(data)
#     elif data == "True":
#         data = bool(data)
#     elif data == "False":
#         data = bool(data)

#     set6.add(data)
#     i = i + 1


# print(set6)

set6 = {0, 1, 0.4, "xyz"}

set7 = [1, 2, 3, "Ayush", "Kumar", "Vishwakarma"]
set8 = {"madam"}

string8 = "madam"
list8 = []
for i in string8:
    list8.append(i)

print(list8)

set9 = set()

set9.update(list8)
print(set6)

print(set9)

set10 = {1, 2, 3}
set11 = {4, 5, 6, 23, 1, 1, 0, -1, -23}
print(set10 - set11)

for i in set10:
    print(i)
    if 1 in set10:
        print("Yes the number 1 is present in the set10")
        break

minimum = min(set10)
print(minimum)

maximum = max(set10)
print(maximum)


print(sorted(set11))

set12 = {12, 3, 34, 5}
set12.add(10)

print(set12)

set12.add(4)
print(set12)

set13 = {1, 2, 3}
set14 = {4, 5, 6, 3}
set13.update(set14)
print(set13)

print(set13.intersection(set14))

set13.update([2, 3, 4, 5, 5, 34])
print(set13)


