#Loading data from a file
import numpy as np
x = np.genfromtxt('data.txt', delimiter=',')
x = x.astype('int16')
#print(x)

#Boolean Masking and Advanced indexing

#true false array of operator
flag = x>50
#print(flag)

#grab values >50
filter = x[x>50]
#print(filter)

#index with a list i.e can pass a list as an index

a = np.array([1,2,3,4,5,6,7,8,9])
b = a[[1,2,3]]
#print(b)

#print(np.any(x>50, axis=0))
#print(np.all(x>50, axis=0))
d = ~((x>50) & (x<100))
print(d)