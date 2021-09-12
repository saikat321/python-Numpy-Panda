# x = 'saikat'
# for i in x:
#     print(i)
#
# for i in range(10):
#     print(i)
#
# for d in range(10,87,8):
#     print(d)
# for y in range(87, 10, -8):
#     if y%5==0:
#         print(y)
#perfect aquare number

# def squares(a, b):
#     lists=[]
#     # Traverse through all numbers
#     for i in range (a,b+1):
#         j = 1;
#         while j*j <= i:
#             if j*j == i:
#                  lists.append(i)
#             j = j+1
#         i = i+1
#     return lists
# print(squares(1, 50))

#break statement
# available =5
# x = int(input("how many candy you want? "))
# i =1
# while i<=x:
#     if i>available:
#         print("out of stock")
#         break
#     print("candy")
#     i+=1
# print("bye")

#continue statement
# for i in range (1,50):
#     if i%5==0 or i%6==0:
#         continue
#     print(i)
# print("bye")

# #pass statement
# for i in range (1,40):
#     if i%2==0:
#         pass
#     else:
#         print(i)


# #fibonacci series
# x,y=0,1
# z = int(input("enter number"))
# while y<z:
#     print(y)
#     x,y = y,x+y

def fib (n):
    # a=0
    # b=1
    # if n==1:
    #     print(a)
    # else:
    #     for i in range(2,n):
    #         c = a+b
    #         a=b
    #         b=c
    #         print(c)

    x,y=0,1
    z = int(input("enter number"))
    while y<z:
        print(y)
        x,y = y,x+y
l = int(input("enyer the number"))
fib(l)



#printing pattern

# for i in range(4):
#     for j in range(4-i):
#         print("# " ,end="")
#     print()

# rows = 6
# # if you want user to enter a number, uncomment the below line
# # rows = int(input('Enter the number of rows'))
# # outer loop
# for i in range(rows):
#     # nested loop
#     for j in range(i):
#         # display number
#         print(i, end=' ')
#     # new line after each row
#     print('')

# ro = 5
# for k in range(0,ro+1):
#     for l in range(1, k+1):
#         print(l,end=" ")
#     print()

# ro = 5
# for k in range(0,ro+1):
#     for l in range(ro-k , 0 ,-2):
#         print(l,end=" ")
#     print()
#for else
#
# nums = [10,34,56,71,78,67]
# for num in nums:
#     if (num %5 ==0):
#         print(num)
#         break
# else:
#     print("not found")

    # print prime or not
# prime  = int(input("enetr e number"))
# for p in range(2,prime):
#     if(prime%p ==0):
#         print("prime number")
#         break
# else:
#     print("not a prime")

#Factorial of a number
# def fact (n):
#     f =1
#     for i in range(1,n+1):
#         f = f*i
#         print(f)
#     return f
# x = int(input("enter factorial number =="))
# result =fact(x)
# print(result)

# Recursion
# import sys
# sys.setrecursionlimit(2000)
# print(sys.getrecursionlimit())
# i =0
# def greet ():
#     global  i
#     i+=1
#     print("hello" , i)
#     greet()
# greet()
#recursion  to find factorial
def fact (n):
    if n==0:
        return 1
    return n * fact(n-1)
k = int(input("enter the number"))
result = fact(k)
print(result)
