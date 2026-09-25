import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 8])
y = np.array([3, 10])

plt.plot(x, y)
plt.show()


# we can plot as many points we want to

a = np.array([1, 2, 3, 4, 45, 6])
b = np.array([3, 4, 5, 6, 6, 73])

plt.plot(a, b)
plt.show()


arr = [2, 3, 4, 5, 6,7]
arr2 = [3, 4, 5, 6, 7, 7]

plt.plot(arr, arr2)
plt.show()