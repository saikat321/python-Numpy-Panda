# lambda function =anonymous funtion = a func with no name
# add = lambda a,b:a+b
# # it will work if we have on;y single expression mean we cant perform 2 operation i single lambda
# print(add(9,4))
#
# # check even
# def even (a):
#     if a%2==0:
#         return True
# print(even(8))
#
# even1 =lambda c:c%2==0
# print(even(12))
# # taking 3 parameter
# multiply= lambda q,w,e:q*w*e
# print(multiply(2,3,5))
#
# # FILTER FUNCTION
# # it uses 2 argument one is the logic function and other on which we need to apply the function
# def even(num):
#     if num%2==0:
#         return True
# # even1 = lambda k :k%2==0
# lst = [2,5,6,8,33,88,65,78,2,4,6]
# # we will apply filter=we need to store it in filter
# print(list(filter(lambda k :k%2==0,lst)))

# Map function

def even_or_odd(num):
    if num%2==0:
        return "the number {} is even" .format(num)
    else:
        return "the number {} is odd".format(num)
# print(even_or_odd(35))
# we can use a MAP to check multiple number
# ls =[5,6,83,55,66,79,9,23,46,88]
# print(list(map(even_or_odd,ls)))

# Reduce is imported from FUNCTOOL
import functools as ft
#  filter , map, reduce all in pne eg below

num =[4,5,6,2,54,67,98]
evens = print(list(filter(lambda n :n%2==0 ,num)))

doubles =list(map(lambda n : n*2 ,num))
print(doubles)

sum = print(ft.reduce(lambda a,b:a+b ,doubles))