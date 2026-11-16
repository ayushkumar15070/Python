from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


x = random.uniform(size=(3, 4))
print(x)
# sns.displot(x, kind="kde")
plt.plot(x)
plt.show()
plt.show()