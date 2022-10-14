import numpy as np

arr3 = np.array([[[7,8,4],[6,5,9]],[[4,3,2],[6,3,8]]])
print(np.sort(arr3))

x = np.where(arr3 == 4)

print(x)
