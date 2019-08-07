# Numpy Array in python ...!
import numpy as npArray

# 1:D Array
array = npArray.array([1, 2, 3, 4, 5])
print(f"1:D Array : {array}")

# 2:D Array
array = npArray.array([[0, 1, 2, 3, 4],
                      [5, 6, 7, 8, 9]])
print(f"2:D Array :\n {array}")

# accessing 2:D array element by index
print(f"array[0][4] : {array[0][4]}")
print(f"array[1][4] : {array[1][4]}")

# (5 X 5) order 2:D Array
array = npArray.array([[0, 1, 2, 3, 4],
                       [5, 6, 7, 8, 9],
                       [10, 11, 12, 13, 14],
                       [15, 16, 17, 18, 19],
                       [20, 21, 22, 23, 24]])

# slicing Array element....
slicingArray =  array[:2, :2]
print(f"slicing first 2 row and 2 column : \n {slicingArray}")
print(f"slicing first 2 row and alternate column : \n {array[:2, 1::2]}")
