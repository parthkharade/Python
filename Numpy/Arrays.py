import numpy as np


#initialize an array

a = np.array([1,2,3],dtype='int16')
print(a)

b = np.array([[1,2,3],[1.2,3.2,4.5]])
print(b)

#get dimension

print(f'Dimension of A : {a.ndim}')
print(f'Dimension of B : {b.ndim}')

# get shape
print(f'Shape of A : {a.shape}')
print(f'Shape of B : {b.shape}')

#get type

print(f'Type of A : {a.dtype}')

#get size
print(f'ITEM SIZE A : {a.itemsize}')
print(f'SIZE A : {a.size*a.itemsize}')

print(f'ITEM SIZE B : {b.itemsize}')
print(f'SIZE B : {b.size*b.itemsize}')
