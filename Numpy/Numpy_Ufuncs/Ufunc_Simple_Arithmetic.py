import numpy as np

#Addition
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([2, 3, 4, 5])

finalarr1 = np.add(arr1, arr2)
print(finalarr1)


#Subtraction
arr3 = np.array([1, 2, 3, 4])
arr4 = np.array([4, 5, 6, 7])

finalarr2 = np.subtract(arr3, arr4)
print(finalarr2)


#Multiplication
arr5 = np.array([1, 2, 3, 4, 5])
arr6 = np.array([5, 6, 7, 4, 3])

finalarr3 = np.multiply(arr5, arr6)
print(finalarr3)

#Division
arr7 = np.array([1, 2, 3, 4, 5])
arr8 = np.array([5, 6, 7, 8, 9])

finalarr4 = np.divide(arr7, arr8)
print(finalarr4)

#Exponent

arr9 = np.array([1, 2, 3, 4])
arr10 = np.array([4, 6, 7, 8])

finalarr5 = np.power(arr9, arr10)
print(finalarr5)

#Remainder

arr11 = np.array([1, 2, 3, 4])
arr12 = np.array([12, 3, 4, 5])

finalarr6 = np.mod(arr11, arr12)
print(finalarr6)

arr13 = np.array([1, 2, 3, 4, 5])
arr14 = np.array([34, 34, 45, 45, 23])

finalarr7 = np.remainder(arr13, arr14)

print(finalarr7)


#Quotient and mod

arr15 = np.array([1, 2, 3, 4])
arr16 = np.array([12, 23, 3, 34])

finalarr8 = np.divmod(arr15, arr16)
print(finalarr8)

#Absolute Values

arr17 = np.array([1, 2, 3, 4])
arr18 = np.array([12, 12, 12, 12])

finalarr9 = np.absolute(arr)