import inline as inline

import matplotlib
import  matplotlib.pyplot as plt
import  numpy as np
import math as ma
#if we write this statement we dont need to do write plt.show to get any graph
# % matplotlib inline
# x=np.arange(0,10)
# y=np.arange(11,21)
# y1 =x*x
# y2 =x**x
#
# # it was a scatter plot
# # plt.scatter(x,y,c="g")
# # plt.xlabel('x axis')
# # plt.ylabel('y axix')
# # plt.title('graph in 2d')
# # # plt.savefig('test.jpg')
# plt.show()
#
#
# # # now we will get a straight or curve line
# # plt.plot(x,y1,'m*', linestyle='dashed', linewidth=2 ,markersize=12)
# # plt.xlabel('x axis')
# # plt.ylabel('y axis')
# # plt.show()
#
# # in we need ton have a manynplot in single canvas
# # plt.subplot(2,2,1)
# # plt.plot(x,y1,"b--")
# # plt.subplot(2,2,2)
# # plt.plot(x,y2,"go")
# # plt.subplot(2,2,3)
# # plt.plot(x,y,"b*-")
# # plt.show()
#
# # x1 = np.arange(1,12)
# # y4 = 3*x1+5
# # plt.plot(x1,y4,'m')
# # plt.show()
#
# # sin curve
# # x2 = np.arange(0,6*np.pi,0.2)
# # y5 = np.sin(x2)
# # plt.plot(x2,y5)
# # plt.show()
#
# # subplot for sin and cos
# x3 = np.arange(0,6*np.pi,0.2)
# y6 = np.sin(x3)
# y7 =np.cos(x3)
#
# plt.subplot(2,2,1)
# plt.plot(x3,y6,"g*")
# plt.subplot(2,2,2)
# plt.plot(x3,y7,"m")
# plt.show()
#
# bar chart
x = [2,8,10]
y=[11,16,9]

x2=[3,9,11]
y2 =[6,15,7]

x3=np.arange(1,5)
y3=np.arange(2,6)

# plt.bar(x,y, color='m')
# plt.bar(x2,y2,color='g')
# plt.bar(x3,y3,color='b')
# plt.show()

# histogram
# a = np.array([22,3,6,11,67,3,8,55,67,89,2,45,67,12])
# # by default there vare 10 bins
# plt.hist(a,bins=15)
# plt.show()

# box plot
# data = [np.random.normal(0,std ,100) for std in range (1,4)]
# plt.boxplot(data ,vert=True ,patch_artist=True)
# plt.show()

# piechart
labels = 'Python' ,'Java' ,'Angular' ,'AWS'
size =[200,150,100,250]
colors =['gold' ,'yellowgreen' ,'blue' ,'lightcoral']
explode =(0,0,0,0)

plt.pie(size ,explode=explode ,labels=labels ,colors=colors,autopct ='%1.1f%%' , shadow=False)
plt.axis('equal')
plt.show()

