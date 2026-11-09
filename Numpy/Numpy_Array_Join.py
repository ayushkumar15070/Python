import numpy as np

arr = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

finalarr = np.concatenate((arr, arr2))
print(finalarr)


#Join of two dimensional array

arr3 = np.array([[1, 2], [3, 4]])
arr4 = np.array([[5, 6], [7, 8]])

finalarr2 = np.concatenate((arr3, arr4), axis=1)

print(finalarr2)

#Joining of two array using stack function

arr5 = np.array([1, 2, 3, 4])
arr6 = np.array([5, 6, 7, 8])

finalarr3 = np.stack((arr5, arr6), axis=1)

print(finalarr3)

arr7 = np.array([1, 2, 3])
arr8 = np.array([4, 5, 6])

finalarr4 = np.hstack((arr7, arr8))
print(finalarr4)


arr9 = np.array([1, 2, 3])
arr10 = np.array([4, 5, 6])

finalarr5 = np.vstack((arr9, arr10))
print(finalarr5)


arr11 = np.array([1, 2, 3])
arr12 = np.array([4, 5, 6])

finalarr6 = np.dstack((arr11, arr12))
print(finalarr6)