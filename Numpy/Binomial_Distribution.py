from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt

x = random.binomial(n = 100, p=0.8, size=10)
print(x)
y = random.binomial(n = 10, p=0.5, size=10)

print(y)

sns.displot(y)
plt.show()


data = {
    "normal":random.normal(loc = 10, scale = 0.5, size=10),
    "binomial":random.binomial(n = 10, p=0.5, size=10)
}

print(data['normal'])
print(data["binomial"])

sns.displot(data, kind="kde")
plt.show()