# The python have these default data types
# 1. String
# 2. Boolean
# 3. Integer
# 4. Float
# 5. Complex


import numpy as np 

arr = np.array([1, 2, 3, 4])
print(arr)
print(arr.dtype)

arr2 = np.array(['apple', 'banana', 'cherry'])
print(arr2)
print(arr2.dtype)

arr3 = np.array([1, 2, 3, 4], dtype='S')
print(arr3)
print(arr3.dtype)

arr4 = np.array([1, 2, 3, 4], dtype='i4')
print(arr4)
print(arr4.dtype)

arr5 = np.array([1.0, 2.8, 3.9, 5.5])
newarr = arr5.astype('i')
print(newarr)
print(newarr.dtype)

# another method

arr6 = np.array([3.4, 5.6, 7.9, 0.2])
newarr2 = arr6.astype(int)
print(newarr2)
print(newarr2.dtype)


#Boolean
arr7 = np.array([0, 2, 3, 10-10])
newarr3 = arr7.astype(bool)
print(newarr3)
print(newarr3.dtype)