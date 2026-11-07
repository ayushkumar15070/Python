#Numpy Array Slicing

import numpy as np 

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr[0:3])
print(arr[4:])
print(arr[:4])

#Negative Slicing
print(arr[-3:-1])

#Step Slicing
print(arr[0:9:2])

#From the entire array
print(arr[::-2])
print(arr[::1])
print(arr[::-1])

#2-D array slicing
arr2 = np.array([[2, 3, 4, 5, 6], [1, 2, 3, 4, 5]])
print(arr2[0, 1:4])

print(arr2[0:2, 2])

print(arr2[0:2, 1:4])