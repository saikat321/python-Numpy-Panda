import numpy as num
import matplotlib.pyplot as plt
# from numpy import *
# # using diffrerent type of array
# # arr = num.linspace(0,15,16)
# # print(arr)
# #
# # ar = num.arange(0,15,2)
# # print(ar)
# #
# # a = num.logspace(1,30,5)
# # print('%.2f'%a[3])
# #
# # a1 = num.zeros(4)
# # #this wil  make integer
# # a2 =num.ones(4,int)
# # print(a1)
# # print(a2)
#
# #basic math operation
# # arr1= num.array([2, 5, 1, 3, 7])
# # arr2 = num.array([2,64,2,45,3])
# # arr3= num.concatenate([arr1,arr2])
# # print(arr3)
#
# #copying an array
# # arr1= num.array([2, 5, 1, 3, 7])
# # #view just copy the array and changee the address and copy do deep copying if something change in arr1 it wont reflect in arr4
# # arr5=arr1.copy()
# # arr4=arr1.view()
# # arr1[3]=98
# # print(arr5)
# # print(arr1)
#
# #add 2 array using for loop
# # arr6= num.array([2, 5, 1, 3, 7])
# # arr7= num.array([2, 5, 1, 3, 7])
# # arr8 = []
# # for i in  (arr6):
# #     arr8 =(arr6+arr7)
# #     print("array 8 = ",arr8)
# # # 2nd way of aading array
# #     NumList1 = [10, 20, 30]
# #     NumList2 = [15, 25, 35]
# #     total = []
# #
# #     for j in range(3):
# #         total.append(NumList1[j] + NumList2[j])
# #
# #     print("\nThe total Sum of Two Lists =  ", total)
#
# # a = num.array([2,6,23,66])
# # element =(num.amax(a))
# # print("max ele" , element)
# #
# # #finding the max element
# # def largest(arr, n):
# #     # Initialize maximum element
# #     max = arr[0]
#
#     # Traverse array elements from second
#     # and compare every element with
#     # current max
#
#     #
#     # for i in range(1, a):
#     #     if arr[i] > a:
#     #         a = arr[i]
#     # return a
#     # print("largest element", a)
#
#
# # Driver Code
# myLst = [[1,2,2,5], [23,43,5,4],[5,7,3,7],[4,6,3,5] ]
# arr = num.array(myLst)
# print(num.shape(arr))
# aray = arr.reshape(2,8)
# print(aray)
# print(aray[0:2,4:7])
# print(num.arange(1,23))
# aray[3:]=100
#
# #changing the vvalue frojm 1 to other is called beoadcasting
#
# print(aray)
# arr1 = num.array([1,2,3,4,6,6,7,8,8,8,6])
# arr1[5:]=3343
# print(arr1)
# arr2 =arr1.copy()
# print(arr2)
# arr2[3:]=65656
# print(arr1)
# print("arr2 ====",arr2)
#
# #some condtion helpful in exploratory data analysis
# val=67
# print(arr2<val)
# print(arr2*val)
# print(arr2/val)
# print(arr2+val)
# #to check how many element are less than particular value
# print("it will show less than value  ",arr2[arr2<val])
#
# #random distribution
# print("random distribution ",num.random.rand(4,4))
# slice_of_arr= arr1[0:6]
# slice_of_arr[:] =99
# print(slice_of_arr ,"array 1 slice")
# print(slice_of_arr ,"array 1 slice")
#
# arr_2d = num.zeros((10,10))
# # print(arr_2d.shape)
#
# # we need to convert the array in scalar to iterarte in the for loop
# len = arr_2d.shape[1]
# for i in range (len):
#     arr_2d[i]=i
# print(arr_2d)


# Array transposition
arr = num.arange(50).reshape(10,5)
# print(arr)
# print(arr.T)
# # dot product of array
# print(num.dot(arr.T,arr))

arr_3d = num.arange(50).reshape(5,5,2)
print(arr_3d)
print(arr_3d.transpose((1,0,2)))

print(num.exp(arr_3d))
a = num.random.randn(4)
print(a)
print(num.add(a,arr_3d))
print(num.max(a,arr_3d))