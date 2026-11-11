import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 4)
print(newarr)

print(newarr[0])
print(newarr[1])
print(newarr[2])
print(newarr[3])


arr2 = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr2 = np.array_split(arr2, 3)
print(newarr2)

arr3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr3 = np.array_split(arr3, 3)

print(newarr3)


arr4 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9],[10, 11, 12]])

newarr4 = np.hsplit(arr4, 3)
print(newarr4)

for i in newarr4:
    print(i)