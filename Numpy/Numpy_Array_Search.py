import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

x = np.where(arr == 4)
print(x)

if x[0] == 3:
    print(f"{arr[x]} is present at index {x[0]} in the array")
else:
    print("Something is wrong")


arr2 = np.array([12, 34, 45, 56, 56, 67])
print(np.where(arr2%2 == 1))


arr3 = np.array([1, 2, 3, 4, 5])

newarr = np.searchsorted(arr3, [6, 89, 9], side="right")
print(newarr)