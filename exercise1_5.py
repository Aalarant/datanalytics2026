# Let's recreate these matrices in code based on the pictures.
import numpy as np

# Let's create the first one.
data = np.random.randint(0, 100, size=(3, 5))
print(data)


# Let's create the second one.
data2 = np.random.randint(0, 255, size=(8, 16))
print(data2)

# Let's create the third one.
data3 = np.arange(0, 5, 0.05).reshape(10, 10)
print(data3)    