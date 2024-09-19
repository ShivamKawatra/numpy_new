import numpy as np
arr=np.array([[[1,2,3,4],[1,3,5,7]],[[2,4,6,8],[5,10,15,20]],[[10,20,30,40],[50,60,70,80]]])
print(arr)
print(arr.ndim) #ndim is used to get that array is of which dimension.
print(arr.shape) #shape of matrix of array
x = np.array([1,2,3,4],ndmin=3) #ndmin is used to create dimensions for a array
print(x)