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


set15 = {"BMW", "Volvo", "Mercedes", "Ducatti", "Buggati", "Range Rover"}
for i in set15:
    if i == "Mercedes":
        print("This is what i am instructed to do.")
        break
    print(i)


set14.pop()
print(set14)

set14.pop()
print(set14)

set14.discard(534)
# The discard method won't throw an erro if there is not element which we want to remove is not there
print(set14)

# set14.remove(12)
# The remove method will throw an error if there is not element which we want to remove is not there
print(set14)

set14.clear()
print(set14)


# del set14
# print(set14)

set16 = {12, 23, 34, 45,}
set17 = {13, 14, 23, 45}
set18 = {12, 23}
# set18 = set16.union(set17)
# print(set18)

# set18 = set16.intersection(set17)
# print(set18)

# set16.intersection_update(set17)
# print(set16)

# set18 = set16.difference(set17)
# print(set18)


print(set18.issubset(set16))
print(set16.issuperset(set18))
print(set16.difference(set18))
print(set16.difference_update(set18))


x = {1, 2, 3, 4, 5}
y = {3, 4, 6, 7, 8}
print(x.symmetric_difference(y))

x.symmetric_difference_update(y)
print(x)




#Question_01

# Balance team score
# you are given tuple containing scores
# (12, 18, 7, 25, 18, 10, 7, 30, 15)
# 1. create highscores (>=18)
# 2. create lowscore (<18)
# disply both lists
# display the difference between their sums 

# challenge do not use sum()


scores = (12, 18, 7, 25, 18, 10, 7, 30, 15)

highscores = []
lowscores = []

for i in scores:
    if i >= 18:
        highscores.append(i)
    elif i < 18:
        lowscores.append(i)

print(highscores)
print(lowscores)

sum = 0 
for i in highscores:
    sum = sum + i

sum2 = 0 
for i in lowscores:
    sum2 = sum2 + i


print(sum)
print(sum2)

print(f"The difference between {sum} and {sum2} is {sum - sum2}")


# Question_02
#Duplicate-Free Transaction IDs
# given:
# [101, 103, 101, 105, 107, 103, 109, 105, 110]
# create a new list containing only the first occurence of each transaction ID

# challenge: Do not use set()

IDs = [101, 103, 101, 105, 107, 103, 109, 105, 110]
list1 = []
for i in IDs:
    if i in list1:
        pass
    else:
        list1.append(i)

print(list1)

# Question_03
# given:
# [45, 12, 78, 34, 89, 67, 89, 23]

# find the second largest distinct number 
# challenge Do not use sort(), sorted(), max(), or set()

data = [45, 12, 78, 34, 89, 67, 89, 23]
list2 = []
for i in data:
    if i in list2:
        pass
    else:
        list2.append(i)


print(list2)

for i in list2:
    if i > i + 1:
        temp = i 
        (i + 1) = i
        i = temp
    list2.append(i)

print(list2)
    



# Question_04:
# given:
# T = (10, 20, 30, 40, 50, 60)
# Rotate the tuple to the right by 2 positions
# Then modify the program to accept the rotation value from the User