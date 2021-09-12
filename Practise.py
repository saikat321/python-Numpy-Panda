nums = [223, 45, 345]
print(nums)
print(nums[1:3])
mils = [nums]
print(mils)

# strings are mutable

nums.append("saikat")
print(nums)
# to remove element
nums.pop(3)
print(nums)

# to add in between use insert
nums.insert(2, 47)
print(nums)

# to delete multiple element
del nums[2:4]
print(nums)

# if we want to extend the list
nums.extend(["saikat", "is ", "good"])
print(nums)

# min(nums)
# max(nums)
# sum(nums)
# nums.sort()
print(nums)

# List
s = [1, 2, 3, 4, 5, 6]
res = [x for x in s if x % 2 == 0]
print(sum(res))

# Tuple
tup = (2, 2, 2, 3, 3, 7, 2, 9, 8, 6)
print(tup)
print(tup.count(2))

# set
se = {1, 5, 9, 3}
print(se)

# dictionary
data = {1: "saikat", 2: "tukai", 5: "chakraborty"}
print(data)
print(data.get(3))
d1 = {3: "family"}
data.update(d1)
print(data)
d2 = {1: "sai"}
data.update(d2)
print(data)

keys = ["saikat", "Dhruv", "Pooja"]
values = ["aws", "python", "java"]
data1 = dict(zip(keys, values))
print(data1.get("saikat"))

# list and dictionary inside a dictionary
prog = {'js': 'visual studioo', 'C': 'turbo c', 'python': ['pycharm', 'jupiter'],
        'java': {'jse': 'eclipse', 'jee': 'sts'}}
print(prog)
print(prog['python'][1])
print(prog['java']['jse'])
print(prog['js'])

#variables

nu = 5
#how to get the address of variable
print(id(nu))

#Data types
#complex
com = 2 +6j
print(type(com))

a =4.5
b=5
b= int(a)
print(b)
k = complex(b)
print(k)

#range
range(120)
print(range)
lis = list(range(1 ,120,10 ))
print(lis)
#Dictinary
dic = {'saikat':'samsung' ,'pooja':'iphone' ,'rahul':'Mi'}
print(dic.keys())
print(dic.values())
print(dic['saikat'])

#Operators
#assignment operators
x = 2
x+= 2
print(x)
x*=3
print(x)
a,b=5,6
print(a,b)

#Unary operator
n =7
n =-n
print(n)

#Number system
print(bin(34))
#hexadecimal
print(0x234)
#octal
print(0o57)
print(hex(876))
print(0b1010101010)
