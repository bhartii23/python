# import numpy as np
# arr= np.array([1,2,3,4])

# for x in arr:
#     print(x)
    
# import numpy as np

# arr = np.array([[1, 2, 3], [4, 5, 6]])

# for x in arr:
#   print(x)
  
  
# import numpy as np

# arr = np.array([[1, 2, 3], [4, 5, 6]])

# for x in arr:
#   for y in x:
#     print(y)

# import numpy as np

# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# for x in arr:
#   for y in x:
#     for z in y:
#       print(z)

#3-d array
import numpy as np

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)