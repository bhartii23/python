# import numpy as np
# #take array input
# arr = np.array([1,2,3,4])
# print(arr)

# print(np.__version__)

# type():-tells type of the object
# print(type(arr))

#use tuple to create a numpy array
# arr1 = np.array((1,2,3,4))
# print(arr1)
# print(type(arr1))

#0D array
# arr1= np.array(42)
# print(42)

#2-D array 
# import numpy as np
# arr2 = np.array([[1,2,3],[4,5,6]])
# print(arr2)

# import numpy as np

# arr3 = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
# print(arr3)

# check dimensions
# print(arr1.ndim)
# print(arr2.ndim)
# print(arr3.ndim)

import numpy as np

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype(int)

print(newarr)
print(newarr.dtype)