
import numpy as np

#All 0s matrix
a = np.zeros([5,5])
#print(a)

#All 0s matrix
b = np.ones([4,4],dtype='int32')
#print(b)

#any other number

#print(np.full((2,2) , 99))

c = np.full_like(a,4)
#print(c)

#random decimal numbers
random = np.random.rand(4,2)
print(random)

#random integer values

# lower , upper , size
random = np.random.randint(0,10, size=(3,3) )
print(random)

identity = np.identity(5)
print(identity)

#repeat an array

arr = np.array([[1,2,3]])
r1  = np.repeat(arr,3,axis =0)
print(r1)




