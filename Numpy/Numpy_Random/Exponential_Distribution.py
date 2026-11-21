from numpy import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

x = random.exponential(scale=2, size=(2, 3))
x = random.exponential(size=(1000))
print(x)

sns.displot(x, kind="kde")
plt.show()