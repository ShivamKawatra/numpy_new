import numpy as np
var = np.array([[1,2,3,4,5],[4,5,6,7,9]])
print(var)
print(var.shape)

var_2 = np.array([1,2,3,4])
print(var_2)
print(var_2.shape)

var3 = np.array([1,2,3,4,5,6])
print(var3)
var4 = var3.reshape(3,2) #reshape(row,element)
print(var4)