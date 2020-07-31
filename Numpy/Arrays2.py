import numpy as np

a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])

print(a.shape)

#addressing a specific element
print(a[1,5])

#printing a specific row
print(a[0,:])

#printing a specific column
print(a[:,1])

#printing a specific column +row
print(a[1,1:4])

#[startindex:endindex:stepsize]
print(a[0,1:6:2])

#changing elements

a[1,5] = 14
print(a)


b = np.array([ [[1,2],[3,4]], [[5,6],[7,8]] ])

print(b)

#get specific element

print(b[0,1,1])