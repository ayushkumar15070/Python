import numpy as np
#Without using numpy ufunc
x = [1, 2, 3, 4, 5]
y = [5, 6, 7, 3, 2]
z = []

for i, j in zip(x, y):
    z.append(i + j)

print(z)

#With Numpy Ufunc 

x2 = [1, 2, 3, 4, 5]
y2 = [2, 3, 4, 5, 6]

z2 = np.add(x2, y2)
print(z2)
