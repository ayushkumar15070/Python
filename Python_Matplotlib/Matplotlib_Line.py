import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([1, 3, 4, 2, 1, 45, 12, 2, 3, 12, 344])

plt.plot(ypoints, linestyle = 'dotted')
plt.show()

plt.plot(ypoints, linestyle = 'dashed')
plt.show()

#Shorter format for the above styles

plt.plot(ypoints, ls = ':')
plt.show()

plt.plot(ypoints, ls = '--')
plt.show()

plt.plot(ypoints, color = 'r')
plt.show()

