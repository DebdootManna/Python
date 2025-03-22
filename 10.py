import numpy as np

# Basic Array Creation
print("=== Basic Array Creation ===")
# Create array from list
arr1 = np.array([1, 2, 3, 4, 5])
print("np.array():", arr1)

# Create arrays with zeros and ones
zeros_arr = np.zeros((3, 4))  # 3x4 array of zeros
ones_arr = np.ones((2, 3))    # 2x3 array of ones
print("\nnp.zeros():\n", zeros_arr)
print("\nnp.ones():\n", ones_arr)

# Create array with range
range_arr = np.arange(0, 10, 2)  # From 0 to 10 (exclusive) with step 2
print("\nnp.arange():", range_arr)

# Create array with evenly spaced values
linspace_arr = np.linspace(0, 1, 5)  # 5 values from 0 to 1 (inclusive)
print("\nnp.linspace():", linspace_arr)

# Array Reshaping
print("\n=== Array Reshaping ===")
original = np.arange(12)
reshaped = original.reshape((3, 4))  # Reshape to 3x4
print("Original array:", original)
print("\nReshaped to 3x4:\n", reshaped)

# Flatten a multi-dimensional array
flattened = reshaped.flatten()
print("\nFlattened array:", flattened)

# Transpose (swap rows and columns)
transposed = reshaped.transpose()
print("\nTransposed array:\n", transposed)

# Array Joining and Splitting
print("\n=== Array Joining and Splitting ===")
arr_a = np.array([1, 2, 3])
arr_b = np.array([4, 5, 6])

# Concatenate arrays
concatenated = np.concatenate((arr_a, arr_b))
print("Concatenated:", concatenated)

# Split array
arr_to_split = np.array([1, 2, 3, 4, 5, 6])
split_arrays = np.split(arr_to_split, 3)  # Split into 3 equal parts
print("\nSplit into 3:", [arr for arr in split_arrays])

# Vertical and horizontal stacking
print("\nVertical stack (vstack):")
v_stacked = np.vstack((arr_a, arr_b))
print(v_stacked)

print("\nHorizontal stack (hstack):")
h_stacked = np.hstack((arr_a, arr_b))
print(h_stacked)

# Array Modification
print("\n=== Array Modification ===")
base_arr = np.array([10, 20, 30, 40, 50])

# Append values
appended = np.append(base_arr, [60, 70])
print("Appended:", appended)

# Delete elements (delete element at index 2)
deleted = np.delete(base_arr, 2)
print("\nAfter deleting index 2:", deleted)

# Insert value
inserted = np.insert(base_arr, 2, 25)  # Insert 25 at index 2
print("\nAfter inserting 25 at index 2:", inserted)

# Array Indexing and Slicing
print("\n=== Array Indexing and Slicing ===")
sample = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Sample array:", sample)

# Access single element
print("\nElement at index 3:", sample[3])

# Slice array
print("Slice [2:6]:", sample[2:6])  # Get elements from index 2 to 5

# Slice with step
print("Slice [1:9:2]:", sample[1:9:2])  # Get every other element from index 1 to 8

# 2D array slicing
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\n2D array:\n", matrix)
print("\nAll elements in row 1:", matrix[1, :])
print("All elements in column 2:", matrix[:, 2])
print("Submatrix (first 2 rows, last 2 columns):\n", matrix[0:2, 1:3])