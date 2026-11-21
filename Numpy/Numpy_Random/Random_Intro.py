from numpy import random

x = random.randint(100)
print(x)

t = random.rand()
print(t)


#generating random array

arr = random.randint(100, size = (5))
print(arr)


arr2 = random.randint(100, size=(3, 5))
print(arr2)


arr3 = random.rand(5)
print(arr3)

arr4 = random.rand(3, 5)
print(arr4)


arr5 = random.choice([1, 2, 3, 4])
print(arr5)


randomnumber = random.randint(100)
while True:
    inputfield = int(input("Enter you number: "))

    if inputfield == randomnumber:
        print("You guessed the right number")
        print(f"The random number is {randomnumber}")
        break
    else:
        print("You guessed the wrong number Try again")

list1 = []

i = 0

while i < 100:
    randomnumber2 = random.randint(100)
    list1.append(randomnumber2)
    i = i + 1

print(list1)



list1.sort()
print(list1)

filteredlist = []

for i in list1:
    if list1.count(i) == 1:
        filteredlist.append(i)
    else:
        pass

print(filteredlist)

count = 0

for i in filteredlist:
    count = count + 1

print(filteredlist, count, "These are the number which are unique")


arr6 = random.choice([1, 2, 3, 4], size=(3, 5))

print(arr6)

