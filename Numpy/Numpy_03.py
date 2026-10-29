import numpy as np

array = np.array([[12, 13, 14, 15], [16, 17, 18, 19], [20, 21, 22, 23]])

print(array[1, 1])

array = np.arange(12, 28).reshape(4, 4)

print(array)

print(array[[0, 1, 3]])

print(array[array>17])

print(array[(array > 17) & (array % 2 == 0)])


np.ravel(array)

print(array)

print(np.max(array, axis=0))