#function

# def add_sub (a,b):
#     c = a+b
#     d =a-b
#     return c,d
#we can also print it
   # print(c)
#result1,result2 = add_sub(2,4)
#print(result1,result2)

#passing the value
# def update (lst):
#     print(id(lst))
#     lst[1] =35
#     print(id(lst))
#
# lst = [12,23,45]
# print(id(lst))
# update(lst)
# print(lst)

#passing variable value in function
# def sum (*a):
#     b=0
#     for i in a:
#         b = b+i
#     print(b)
#
# sum(5,6,888,7,34)

#other way
# def sum (c , *d):
#     e=c
#     for i in d:
#         e = e+i
#     print(e)
#
# sum(5,6,888,7,34)
# #ketword variable length argument
#
# def person(name , **data):
#     print(name)
#     for i,j in data.items():
#         print(i,j)
# person("saikat" ,age =23 ,city ="korba" ,mob=88888 )

#global and local var

# a =10
# def somethong ():
#     global a
#     a=188
#     print("in func" ,a)
# somethong()
# print("out" ,a)
#how to access global var address iin function and how to change the value of global var

# b=5
# print(id(b))
# c=4
# u=8
# def some ():
#     b=3
#     #this will take the value of variable u want
#     x= globals()['b']
#     print(id(x))
#     print("in function ", b)
#     globals()['b']=45
# some()
# print("outside    " ,b)

#even and odd from list
# def count (lst):
#     even=0
#     odd=0
#     for i in  lst:
#         if (i%2==0):
#             print(i)
#             even+=1
#         else:
#             if(i%2!=0):
#                 print(i)
#                 odd+=1
#     return even,odd
# l =[]
# n = int(input("enter the length of list"))
# for j in range(0,n):
#     ele = int(input("enter the value"))
#     l.append(ele)
# print(l)
# even , odd = count(l)
# print("even : {} and odd : {}" .format(even,odd))


#print name who has more than 5 letter
def namecount (name):
    nam =[]
    for i in range(0,name):
        if (len(i)>5):
            nam.append(i)
    return name
na = []
p = int(input("enter the number of name"))
for k in range(0,p):
    nam = str(input("enter name "))
    na.append(nam)
print(na)

name = namecount(na)
print(na)

