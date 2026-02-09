import numpy

# 1. Let's create a NumPy vector (list) containing these values: 5, 16, 9, 2, 19, 18, 11, 7
vector = numpy.array([5, 16, 9, 2, 19, 18, 11, 7])
print("Original vector:", vector)

argmax_index = numpy.argmax(vector)
print("Index of the maximum value:", argmax_index)

# 2. Let's create a 7x7 array (matrix) with random integers between 0 and 49
rng= numpy.random.default_rng()
data = rng.integers(0, 49, size=49).reshape(7, 7)
print(data)

# 3. Let's generate 8x8 random number matrix, integer values between 0 and 5.
data2 = rng.integers(0, 5, size=64).reshape(8, 8)
print(data2)

# 4. Let's generate a 8x8 random number matrix, using standard normal distribution values (= values are any decimal values between -3 and 3).
data3 = rng.integers(-3, 3, size=64).reshape(8, 8)
print(data3)