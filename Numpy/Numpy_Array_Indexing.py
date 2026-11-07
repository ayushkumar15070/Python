#accessing array elements using indexing

import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr[0])
print(arr[2])
print(arr[1] + arr[2])


arr2 = np.array([[2, 3, 4, 5], [1, 2, 3, 4]])
print(arr2[0, 1])


arr3 = np.array([[[1, 2, 3, 4], [3, 4, 5, 6]], [[2, 3, 4, 5], [5, 6, 7, 7]]])
print(arr3[0, 1, 2])


arr4 = np.array([[2, 3, 4, 5], [5, 6, 6 ,7]])
print(arr4[1, -1])
print(arr4[0, -1])