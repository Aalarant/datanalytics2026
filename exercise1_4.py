import numpy as np

# Let's create a linearly spaced array (list/vector) of 10 values between 0 and 1.
data = np.linspace(0, 1, 10)
print(data)

# Let's create a linearly spaced 10x10 matrix between values 0 and 5.
data2 = np.linspace(0, 5, 100).reshape(10, 10)
print(data2)

