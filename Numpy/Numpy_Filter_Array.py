import numpy as np

arr = np.array([1, 2, 3, 4])
x = [True, False, True, False]
print(arr[x])



arr2 = np.array([1, 2, 3, 4, 5, 6])
filtered_Array = []
for i in arr2:
    if i > 4:
        filtered_Array.append(True)
    else:
        filtered_Array.append(False)
newarr = arr2[filtered_Array]
print(newarr)



arr3 = np.array([34, 23, 12, 45, 56, 34])
filtered_Array2 = []
for i in arr3:
    if i%2 == 0:
        filtered_Array2.append(True)
    else:
        filtered_Array2.append(False)
newarr2 = arr3[filtered_Array2]
print(newarr2)



#creating filter directly 
arr4 = np.array([12, 34, 56, 67, 89, 90])
filtered_Array3 = arr4 > 23
newarr3 = arr4[filtered_Array3]
print(newarr3)

arr5 = np.array([23, 56, 34, 33, 12, 33, 122])
filtered_Array4 = arr5%2 == 0
newarr4 = arr5[filtered_Array4]
print(newarr4)