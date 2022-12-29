#demonstrates the use of an array

import numpy as np

numbers = np.array([2, 3, 5, 7, 11])
print(numbers)

numbers = np.array([[1, 2, 3], [4, 5, 6]])
print()
print(numbers)

numbers = np.array([x for x in range(2, 21, 2)])
print()
print(numbers)

numbers = np.arange(1, 21).reshape(4, 5)
print()
print(numbers)