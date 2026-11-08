import numpy as np

#Copy method
arr = np.array([1, 2, 3, 4])
x = arr.copy()
arr[0] = 42
print(arr)
print(x)


# View method
arr2 = np.array([1, 2, 3, 4])
y = arr2.view()
arr2[0] = 34
print(arr2)
print(y)

arr3 = np.array([1, 2, 3, 4])
z = arr3.view()
z[1] = 23
print(z)
print(arr3)

#Base

arr4 = np.array([1, 2, 3, 4])
x2 = arr4.view()
y2 = arr4.copy()
print(x2.base)
print(y2.base)