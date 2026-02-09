import numpy as np
dataset= np.arange(1, 50).reshape(7, 7)

# Let's add 50 to all  values in the dataset.
dataset_plus_50 = dataset + 50
print(dataset_plus_50)

# Let's sum all the values in the dataset.
dataset_sum = np.sum(dataset)
print(dataset_sum)

# Let's sum only odd values in the dataset.
dataset_odd_sum = np.sum(dataset[dataset % 2 == 1])
print(dataset_odd_sum)

# Let's use standard deviation of the dataset
dataset_std = np.std(dataset)
print(dataset_std)

# Let's row-wise sum the dataset.
dataset_row_sum = np.sum(dataset, axis=1)   
print(dataset_row_sum)

# Let's column-wise sum the dataset.
dataset_col_sum = np.sum(dataset, axis=0)
print(dataset_col_sum)

