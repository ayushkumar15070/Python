import numpy as np

studentmarks  = np.array([
    [85, 78, 92, 88], 
    [67, 89, 76, 95],
    [91, 93, 89, 97],
    [56, 65, 72, 60],
    [78, 82, 85, 80]
])

# #Total Marks of each student
totalmarksofeachstudent = []

for i in range(len(studentmarks)):
    totalmarksofeachstudent.append(np.sum(studentmarks[i]))

print("-----Student Analysis-----\n")

print("Total marks of each student are: ")
j = 1
for i in totalmarksofeachstudent:
    print(f"\tTotal marks of Student {j} -> {i}")
    j = j + 1

#Average marks of each student
averagemarksofstudent = []

for i in range(len(studentmarks)):
    averagemarksofstudent.append(np.mean(studentmarks[i]))

print() #This print statement is only to create a spane between these two questions of programs
print("Average marks of each student are: ")

k = 1
for i in averagemarksofstudent:
    print(f"\tAverage marks of student {k} -> {i}")

print()
#Highest marks in the dataset
print(f"Highest marks is: {np.max(studentmarks)}\n")

#Lowest marks in the dataset
print(f"Lowest marks is: {np.min(studentmarks)}\n")

#Average marks of each subject
averagesubjectofeachsubject = []

averagesubjectofeachsubject.append(np.mean(studentmarks, axis=0))

print("The average marks of each subjects are: ")

l = 1
for i in averagesubjectofeachsubject:
    for j in i:
        print(f"\tAverage marks of Subject {l} -> {j}")
        l = l + 1

    