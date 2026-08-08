#   list -> creation
        #   accessing
        #   editing
        #   functions 
        #   operations
        #   methods


# lists are mutable

list1 = [1, 2, 3, 4, 5, 6]
print(list1)
print(type(list1))

for i in list1:
    print(i)

list1.reverse()
print(list1)

list1.append("Ayush")
print(list1)

list2 = list1.count(2)
print(list2)

# howmany = int(input("How many data you want to enter: "))

# i = 0
# list3 = []
# while i < howmany:
#     data = input("Enter your data: ")
#     list3.append(data)
#     i = i + 1


# print(list3)

multiple_list = [1, 2, 3, 4,5]
print(multiple_list)


# list3 = []

# name = input("Enter your name: ")
# list3.append(name)
# age = int(input("Enter your age: "))
# list3.append(age)
# college = input("Enter your college name: ")
# list3.append(college)
# course = input("Enter the course what you have done or doing: ")
# list3.append(course)
# branch = input("Enter your course branch: ")
# list3.append(branch)
# graduation_year = int(input("Enter your graduation year: "))
# list3.append(graduation_year)


# if "B.Tech" in list3:
#     print("Yes, you are doing all the things coorectly and right!!")

# print(list3)


# list3.append((2, 3, 4, 5, 6))
# print(list3)



multiple_list.insert(1, 52)
print(multiple_list)
print(multiple_list.index(1))
multiple_list.sort(reverse=True)
print(multiple_list)



multiple_list.clear()


list4 = [1, 2, 3, 4]
list5 = ["Ayush", "Kumar", "Vishwakarma"]

list6 = list4 + list5
print(list6)

list7 = list6*2
print(list7)


for i  in list5:
    print(i)
    if "Ayush" in i:
        print(f"Yes, Ayush is there in the {list5}")
        break

print(list5)

list6 = "Ayush", "Kumar", "Vishwakarma"

print(list6)

print(type(list6))