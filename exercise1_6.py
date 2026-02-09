import  numpy as np

# Let's create the matrix.
dataset = np.arange(1, 37).reshape(6, 6)
print(dataset)

# Let's create the first slice of the matrix
dataset2 = np.arange(21, 37).reshape(4, 4)
print(dataset2)

# Let's create a column slice from the first data that shows 4, 10, 16 and 22.
dataset3 = dataset[:, 3]
print(dataset3)

# Let's pick out the row from the data that includes the values of 13, 14, 15, 16, 17, 18.
dataset4 = dataset[2, :]
print(dataset4)

# Let's create the last slice
# That includes these three rows from data.
# 19, 20, 21, 22, 23, 24
# 25, 26, 27, 28, 29, 30
# 31, 32, 33, 34, 35, 36
dataset5 = dataset[3:6, :]  
print(dataset5)
