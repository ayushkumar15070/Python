from numpy import random

x = random.choice([3,5, 7, 9] , p=[0.1, 0.2, 0.5, 0.2], size=(10))
print(x)

t = random.choice([1, 2, 3, 4], p = [0.1, 0.2, 0.5, 0.2], size=(3, 5))
print(t)

