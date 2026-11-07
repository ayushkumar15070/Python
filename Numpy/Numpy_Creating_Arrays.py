import numpy as np

arr = np.array([1, 23, 34, 54, 5])

print(arr)
print(type(arr))


#we can pass any array like object into that array funciton

#tuple
arr2 = np.array((1, 2, 3, 4, 5))
print(arr2)


#0-D array
arr3 = np.array(34)
print(arr3)

#1-D array
arr4 = np.array([2, 3, 4, 5, 6])
print(arr4)

#2-D array
arr5 = np.array([[1, 2, 3, 4], [2, 3, 4, 5]])
print(arr5)

#3-D array
arr6 = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]], [[1, 2, 3, 4], [5, 6, 7, 7]]])
print(arr6)

print(arr3.ndim)
print(arr4.ndim)
print(arr5.ndim)
print(arr6.ndim)


#any number of dimensions
arr7 = np.array([1, 2, 3, 4], ndmin=5)
print(arr7)
print(arr7.ndim)