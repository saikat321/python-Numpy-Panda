from array import *
from numpy import *
# vals = array('i', [4,6,2,0,67])
# newArr = array(vals.typecode , (a-1 for a in vals))
# for i in range(len(newArr)):
#     print(newArr[i])

# Initialize array

arr = [5, 2, 8, 7, 1];
temp = 0;

# Displaying elements of original array
print("Elements of original array: ");
for i in range(0, len(arr)):
    print(arr[i], end=" ");

# Sort the array in ascending order
for i in range(0, len(arr)):
    for j in range(i + 1, len(arr)):
        if (arr[i] > arr[j]):
            temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;

print();

# Displaying elements of the array after sorting

print("Elements of array sorted in ascending order: ");
for i in range(0, len(arr)):
    print(arr[i], end=" ");

#User input the value
ar = array('i',[])
n = int(input("eneter the length of array"))
for q in range(n):
    x =int(input("enter he value"))
    ar.append(x)
print(ar)
val = int(input("enter the nymber to searched"))
k= 0
for e in ar:
    if (e ==val):
        print(k)
        break
    k+=1
else:
    print("wrong value entered")
print(ar.index(val))
print("Reversed list is", ar[::-1])
#deleteing an element
del ar[2]
print(ar)


