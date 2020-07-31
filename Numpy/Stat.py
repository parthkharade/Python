import numpy as np

stats = np.array([[1,2,3],[4,5,6]]) 

print(np.min(stats, axis=1))
print(np.max(stats))
print(np.sum(stats[0,:]))#can call on slected elements


#reorganising arrays

before = np.array([[1,2,3,4],[5,6,7,8]]) 

print(before)

after = before.reshape((8,1))
print(after)


#Veritical Stacking vectors
v1 = np.array([1,2,3,4])

v2 = np.array([5,6,7,8])

v3 = np.vstack([v1,v2,v1,v2])
print(v3)

#horizontal Stack similar to vertical stack


