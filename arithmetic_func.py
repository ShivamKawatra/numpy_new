import numpy as np

print("1D ARRAY:-\n")
a = np.array([33,4,55,67])
print(np.min(a))
print(np.max(a))
print(np.argmin(a))
print(np.argmax(a))
print(np.sqrt(a))
print(np.sin(a))
print(np.cos(a))
print(np.cumsum(a)) #cumulative frequency

print("\n2D ARRAY:-\n")
b = np.array([[2,3,4],[1,5,3]])
print(np.min(b,axis=0))
print(np.max(b,axis=0))
print(np.argmin(b,axis=0))
print(np.argmax(b,axis=0))
print(np.min(b,axis=1))
print(np.max(b,axis=1))
print(np.argmin(b,axis=1))
print(np.argmax(b,axis=1))