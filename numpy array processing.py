import matplotlib.pyplot as plt
import numpy as np

points = np.arange(-5,5,0.01)
dx ,dy = np.meshgrid(points,points)
# print(dx,dy)
z=(np.sin(dx) + np.sin(dy))
# print(z ,"sin cos")
# plt.imshow(z)
# plt.colorbar()
# plt.show()

# array procesin putting condition in array
a = np.array([1,2,3,4])
b= np.array([100,200,22,33])
condition =np.array([True,False,True,False])
x = [(A_val if cond else B_val) for A_val,B_val,cond in zip(a,b,condition)]
print(x)
# short form of above condition
c = np.where(condition,a,b)
print(c)
# few more condition

arr = np.random.randn(5,5)
np.where(arr<0,0,arr)
print(arr.sum())
# we can add alon specific coloumn
print(arr.sum(1))
print(arr.mean(1))
print(arr.std(1))
print(arr.var(1))
(arr.sort(),"sort array")