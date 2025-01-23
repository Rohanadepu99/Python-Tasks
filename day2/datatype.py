
# tuple
# string and tuple are immutable in python and js not in other lang
# Why these are immutable ?

num1= 26
print(type(num1))
print(id(num1))
num2 = 26
print (id(num2))
print("varible used to refer the value only not to store")

str1 = "hi"
print(type(str1))
print(id(str1))
str2 = 'hi'
print (id(str2))

print('number of different varibles with same values have a same location/id.. if we want to change a particular varible then all the varibles should change so to this bug strings in python are immutable ')


name = "str"
name = "str"
name = "str"
name = "str"
name = "str"
print(name);
print(id(str))
name = "str"
name = "str"
name = "str1"
print(name)
print(id(name))

print('so we cannt change particular index value of the string onl ')
print('--------')

# tuple immutable
tup1 = (1, 'hi',True, [1,"rohan"],"string")
print(type(tup1))
print(tup1[1]) 
# tup1[1]= 'welcome';
# tuple is immutable;
print(tup1[1]) 
print(tup1);
tup1 += (1)
print(tup1)

# difference blt tuple and list... important

# adv of tuple
# 1. not to make any chance by user
# it will dublicate the code and always to make change

# range - 
# range(0,10)
r1=range(0,10)
print(list(r1))

# slice
print()

# steps to skip
print(r1[2: 10: 2])



num1=901094
num2=9010
# print(num1)

# print(num2)
num2=630384
# print(num2)
# print(num2)
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1%num2)
print(num1&num2)
# print(num1**num2)....It is not applying
print(num1//num2)

#Datatype
print(type(num1))
print(type(num2))


#Strings
name= 'Rohan Sai'
print(name)
name2="Rohan"
print(name2)

#length
print(len(name))
print(len(name2))

#String Indexing
print(name[5])
print(name2[8])

#Negative Indexing
print(name[-10])
print(name2[-4])

#slicing (or) Substring
print(name[2:10])
print(name[5:8])

#Negative Slicing
print(name[-12:-2])
print(name2[-8:-1])

#Datatypes
#1.Numeric data types
#2.Sequence Data types

#Numeric Data types
#1.Int data type
#2.Float data type
#3.Complex number data type
#4.Boolean data type

#Int Data type
a=12345
b=98765
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(type(a))
print(type(b))

#float Data type
r=5.11
m=5.5
print(r+m)
print(r-m)
print(r*m)
print(r/m)
print(r//m)
print(r**m)

#Float class
print(type(r))
print(type(m))

#complex number data type
t=8
n=5j
print(t+n)
print(t-n)
print(t*n)
print(t/n)
# print(t//n) unsupported operand
print(t**n)


#Complex class
print(type[t])
print(type(n))

#Boolean data type
#True condition
rohan=2420
nikhil=2420
print(rohan==nikhil)

#False condition
rohan=2420
surya=2423
print(rohan==surya)

#Boolean class
print(type(rohan==nikhil))

#Boolean length
# print(len(rohan==nikhil))....objects of boolean has no length

#Sequence Data types
#1.string data type
str1= '10k coders'
str2= 'python classes'
print(str1)
print(str2)

#String lenght
print(len(str1))
print(len(str2))

#String append
str1 +=" hyd"
print(str1)

#string class
print(type(str1))

#List data types
list1=[1,2,3,name,[True,2025],2+5j,[False,2024],3020]
print(list1)

#length
print(len(list1))

#list type
print(type(list1))

#List indexing
print(list1[6])

#Slicing
print(list1[2:8])
print(list1[-5:-1])

#List Append
list1.append(89)
print(list1)
print(len(list1))

#Tuple Data type
tup=(2,5,8,str,5678,__name__,[2,5j,-55],[-7,name,2.5],25,3.9,7j)
print(tup)
print(type(tup))

#tuple append 
tup +=(2+3j,)
print(tup)

#length tuple
print(len(tup))

#Slicing
print(tup[2:10])
print(tup[-12:-4])