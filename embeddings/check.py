import numpy as np

x = np.arange(10)

print("Original array:")
#print(x)

np.random.shuffle(x)

print(x)

n = 3
print (x[np.argsort(x)[-n:]])

