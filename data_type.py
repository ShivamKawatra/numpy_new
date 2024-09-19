import numpy as np

#getting data type by dtype
arr1 = np.array([1,2,3,4])
print(arr1.dtype)
arr2 = np.array([1.0,2.0,3.0,4.0])
print(arr2.dtype)
arr3 = np.array(["a","b","c","d"])
print(arr3.dtype)
arr4 = np.array(["A","B","C","D",2,5,7,9])
print(arr4.dtype)

#changing data type by dtype, astype and datatypes as function 
arr5 = np.array([1,2,3,4],dtype=np.int32)
print(arr5.dtype)

arr6 = np.array([1,2,3,4],dtype="f")
print(arr6.dtype)

arr7 = np.array([55,88,99,77])
arr8 = np.float32(arr7)
print(arr7.dtype,arr8.dtype)

arr9 = arr8.astype(int)
print(arr9.dtype)