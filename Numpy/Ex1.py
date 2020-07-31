# 1 1 1 1 1
# 1 0 0 0 1 
# 1 0 9 0 1
# 1 0 0 0 1
# 1 1 1 1 1

import numpy as np
a = np.ones([5,5])
b = np.zeros([3,3])

a[1:4,1:4] = b

a[2,2] = 9
print(a)

# = will just set pointer location, for copying use the .copy function
