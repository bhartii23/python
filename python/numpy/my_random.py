# Generate a random integer from 0 to 100:
from numpy import random
x= random.randint(100)
print(x)

# Generate a random float from 0 to 1:

from numpy import random

x = random.rand()

print(x)

# Generate a 1-D array containing 5 random integers from 0 to 100:

from numpy import random

x=random.randint(100, size=(5))

print(x)

# Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100:
from numpy import random
x=random.randint(100,size=(3,5))
print(x)

# Return one of the values in an array:

from numpy import random

x = random.choice([3, 5, 7, 9])

print(x)

# Generate a 2-D array that consists of the values in the array parameter (3, 5, 7, and 9):

from numpy import random

x = random.choice([3, 5, 7, 9], size=(3, 5))

print(x)

# Randomly shuffle elements of following array:
from numpy import random
import numpy as np
arr = np.array([1,2,3,4,5])
random.shuffle(arr)
print(arr)

print(random.permutation(arr))