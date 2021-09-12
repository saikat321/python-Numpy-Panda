# user input
# x =int (input("enter 1s number"))
# y = int(input("enter 2nd number"))
# z = x + y
# print(z)

# ch = input("eneter a char")[3:]
# print(ch)

# evaluate a expression
# result = eval(input("enter the exp"))
# print(result)

# condition
# x= int(input("enter number"))
# r = x%2
# if r==0:
#   print("even")
# else:
#    print("odd")

# elif
# x = int(input("enter 1 a number"))
# y = int(input("enter 2 a number"))
# z = int(input("enter 3 a number"))
#
# if (x >= y) and (x >= z):
#    largest = x
# elif (y >= x) and (y >= z):
#    largest = z
# else:
#    largest = z
#
# print("The largest number is", largest)
#while loop
i =1
while i<=6:
    print("saikat ", end="")
    j = 1
    while j<=5:
        print("rocks ", end="")
        j=j+1
    i =i+1
    print()

#print number 1 to 100
num=1
a=1
while num<=100:
    if ((a%3 and a%5)==0) :
        a=a+1
    else:
        print(a)
        a=a+1
    num=num+1

 # need to print #
hash =1
while hash<=5:
        print("#  " ,end="")
        hash2= 1
        while hash2<=4:
            print("#  ", end="")
            hash2=hash2+1
        hash=hash+1
        print()