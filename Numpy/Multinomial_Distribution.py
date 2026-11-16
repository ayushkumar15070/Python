from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns 

x = random.multinomial(n = 5, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])

print(x)

sns.displot(x, kind="kde")
plt.show()