import numpy as np

a = np.ones((2,3))
print(a)
b = np.full((3,2),2)
print(b)

c = np.matmul(a,b)
print(c)

c = np.identity(3)

print(np.linalg.inv(c))

#can do a lot of things 

