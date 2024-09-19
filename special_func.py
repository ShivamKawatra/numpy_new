import numpy as np

arr1 = np.zeros(5)
print(arr1)
#zeros func is used to create a array with all elements equal to zero
arr2 =np.zeros((5,4))
print(arr2)

arr3 = np.ones(5)
print(arr3)
#ones func is used to create array with all elements equal to one
arr4 = np.ones((3,4))
print(arr4)

arr5 = np.empty(4)
#empty func is used to create an empty array
print(arr5)

arr6 = np.arange(4)
#arange func is used to arange an array
print(arr6)

arr7 = np.eye(3)
#eye func is used to create a identity matrix in array
print(arr7)