from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# x = random.poisson(lam=29, size=100)
# print(x)
# # print(type(x))
# # sns.displot(random.poisson(lam=2, size=100))
# sns.displot(x)

# plt.show()


data = {
    "normal": random.normal(loc=50, scale=7, size=1000),
    "poisson":random.poisson(lam=50, size=1000)
}

print(data["normal"])
print(data["poisson"])

sns.displot(data, kind="kde")

plt.show()


data2 = {
    "binomial":random.binomial(n=100, p=0.5, size=200),
    "poisson":random.poisson(lam=50, size=200)
}

print(data2['binomial'])
print(data2['poisson'])

sns.displot(data2, kind="kde")
sns.displot(data2, kind="ecdf")
sns.displot(data2, kind="hist")

plt.show()

