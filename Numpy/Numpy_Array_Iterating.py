import numpy as np

arr = np.array([1, 2, 3])

for i in arr:
    print(i)

#2-D array iteration

arr2 = np.array([
    [1, 2, 3],
    [3, 4, 5],
    [5, 6, 7]
])


for i in arr2:
    for j in i:
        print(j)

#3-D array

arr3 = np.array([[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]])

for i in arr3:
    for j in i:
        for k in j:
            print(k)


# nditer function
print("Nditer function")
arr4 = np.array([[
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8],
    [9, 10]
]])

for i in np.nditer(arr4):
    print(i)

print("Another method")

arr5 = np.array([1, 2, 3, 4])

for i in np.nditer(arr5, flags=['buffered'], op_dtypes='S'):
    print(i)


print("Another method")

arr6 = np.array([[1, 2, 3], [4, 5, 6]])

for i in np.nditer(arr6[:, ::2]):
    print(i)

print("Another method")

arr7 = np.array([1, 2, 3])
for i in np.ndenumerate(arr7):
    print(i)


print("Another method")
arr8 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, i in np.ndenumerate(arr8):
    print(idx, i)