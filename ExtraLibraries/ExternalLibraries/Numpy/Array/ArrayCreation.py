import numpy as np

# Creating array from list with type int(by default)
array00 = np.array([[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10]], dtype = 'int')
print(f"array00 : \n{array00}")
print(f"\narray00[0][4] : {array00[0][4]}")
print("Array00 stores elements of type: ", array00.dtype)

print("__________________________________________________________")
# Creating array from list with type float
array01 = np.array([[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10]], dtype = 'float')
print(f"array01 : \n{array01}")
print(f"\narray01[0][4] : {array01[0][4]}")
print("Array01 stores elements of type: ", array01.dtype)

print("__________________________________________________________")
# Creating array from list with type float
array02 = np.array([[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10]], dtype = 'complex')
print(f"array02 : \n{array02}")
print(f"\narray02[0][4] : {array02[0][4]}")
print("Array02 stores elements of type: ", array02.dtype)


print("__________________________________________________________")
# Creating array from tuple(Single dimension only)
array03= np.array((1,2,3,4,5))
print(f"array03: \n{array03}")

print("__________________________________________________________")
# Creating array from arange(Single dimension only)
array04 = np.arange(0,10,2)
print(f"array04: \n{array04}")

print("__________________________________________________________")

array05 = np.zeros((2,2,2),dtype= int) # 3:D
array06 = np.ones([2,2]) # 2:D
array07 = np.full((3,3),10,dtype=int)
print(array05)
print()
print(array06)
print()
print(array07)