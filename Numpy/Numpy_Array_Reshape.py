import numpy as np 

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

print(arr.reshape(4, 3))

newarr = arr.reshape(2, 3, 2)
print(newarr)

arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr2.reshape(2, 4).base)

print(arr2.reshape(2, 2, -1))

arr3 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr3.reshape(-1))
