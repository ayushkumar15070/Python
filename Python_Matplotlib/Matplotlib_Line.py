import matplotlib.pyplot as plt
import numpy as np

# ypoints = np.array([1, 3, 4, 2, 1, 45, 12, 2, 3, 12, 344])

# plt.plot(ypoints, linestyle = 'dotted')
# plt.show()

# plt.plot(ypoints, linestyle = 'dashed')
# plt.show()

# #Shorter format for the above styles

# plt.plot(ypoints, ls = ':')
# plt.show()

# plt.plot(ypoints, ls = '--')
# plt.show()

# plt.plot(ypoints, color = 'r')
# plt.show()

# plt.plot(ypoints, linewidth = '34')
# plt.show()


xpoints = np.array([12, 34, 45, 2, 1, 0, 45])
ypoints = np.array([23, 12, 5, 4, 1, 3, 3])

plt.plot(xpoints, color = 'r')
plt.plot(ypoints, color = 'g')

plt.show()


x1 = np.array([12, 4, 0, 1, 2])
y1 = np.array([56, 3, 12, 3, 3])
x2 = np.array([10, 20, 4, 9 ,0])
y2 = np.array([56, 3, 1, 9, 39])

plt.plot(x1, y1, x2, y2)
plt.show()