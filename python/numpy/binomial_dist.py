# Given 10 trials for coin toss generate 10 data points:

# from numpy import random

# x = random.binomial(n=10, p=0.5, size=10)

# print(x)

# Visualization of Binomial Distribution
# Example
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False)

plt.show()