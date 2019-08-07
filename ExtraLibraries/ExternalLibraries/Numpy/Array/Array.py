import numpy as npArray

# Creating array object
array = npArray.array([[1, 2, 3],
                       [4, 2, 5]])

# Printing type of array object
print("Array is of type: ", type(array))

# Printing array dimensions (axes)
print("No. of dimensions: ", array.ndim)

# Printing shape of array
print("Shape of array: ", array.shape)

# Printing size (total number of elements) of array
print("Size of array: ", array.size)

# Printing type of elements in array
print("Array stores elements of type: ", array.dtype)