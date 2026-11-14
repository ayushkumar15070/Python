from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt

x = random.normal(size=(20, 10))

sns.barplot(x)
y = random.normal(loc=1, scale=3, size=(3, 4))
print(y)
sns.barplot(y)

plt.show()
plt.show()


print(x)

sns.displot(random.normal(size=1000), kind="kde")
sns.displot(random.normal(size=1000))

plt.show()