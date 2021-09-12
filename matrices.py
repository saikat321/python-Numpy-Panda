import numpy as num

#arr1 = num.array([[1, 2,5,6,5,5], [3,3,4,5, 6,6]])
#print(num.ndim(arr1))
#print(num.shape(arr1))
# arr2 =arr1.flatten()
# print("flaten" , arr2)
# arr2 = arr1.reshape(3,4)
# arr3 = arr1.reshape(2,2,3)
# print(arr2)
# print(arr3)
# print(arr1.ndim)
# print(arr1.shape)

# i f we need to print it as a matrices
# m = num.matrix(arr1)
# print(m)

# matrix can be directly printed
m1 = num.matrix('6 5 3 4 ;7 3 1 98')
m2 = num.matrix('6 5 3 7 ;7 6 3 98')
m3 = num.matrix(m1) * num.matrix(m2)
print(num.matrix(m3))
print(num.diagonal(m1))
