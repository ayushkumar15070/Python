from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


#x = random.zipf(a = 2, size=(2, 3))
x = random.zipf(a = 2, size=(1000))

print(x)

sns.displot(x[x<100])
# sns.displot(random.zipf(a = 2, size=(1000)), kind="kde")

plt.show()