# print("Day 1")
#Datatypes
#1.Numeric data types
#2.Sequence Data types

#Numeric Data types
#1.Int data type
#2.Float data type
#3.Complex number data type
#4.Boolean data type


# int
num1 = 21
num2 = 4
print(type(num1))
# oprations
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 % num2)
print(num1 ** num2)

# float
num1= 21.0
num2=4.0
print(type(num1))
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 % num2)
print(num1 ** num2)

# boolean # boolean : capital T,F only 
bool= True
print(type(bool))
# boolen : capital T,F only 
my = 123
you = 4

# string class
print(type(my))

#boolean class
print(type(my==you)) 


# true condition
print(my==you) 


# false condition
print(my!=you)


my = "hi"
you = "hello"
# type class
print(type(my))

# boolean class
print(type(my==you)) 

# boolean conditions
print(my==you) 
print(type(len(my)==len(you)))
print(my==you) 

print("---")

# complex number
img1 = 2+3j
img2 = 5+1j
# type
print(type(img1))

# operations
print(img1+img2)
print(img1-img2)
print(img1**img2)
print(img1*img2)
print(img1/img2)
# print(img1//img2); this will not work
# print(img1%img2); this will not work

print("--------")

print("Sequences - string, list, tuple, and range")
# Sequences - 
# string, 
# list, 
# tuple, and 
# range

# strings: sequence of characters
str1="10k coders"
str2="hello"

# print string
print(str1);
print(str2)

# length
print(len(str1))
print(len(str2))

# string indexing : (0 to length-1) or  (-n to -1)
print(str1[0])
print(str2[0])

# negative indexing
print(str1[-10])
print(str2[-5])

# slicing (or) Substring
print(str1[4:11])
# print(str1[4:11:-1]) empty string reads from left to rigth

# right to left
print(str1[-4:-1:1])
# print(str1[-4:-1:-1]) empty string not work  string reads from left to rigth
# print(str1[-1:-4]) empty string not work string reads from left to rigth


# index steping ;; leave str1[-4:-1:n] skips n-1 nums and prints...
print(str1[-4:-1:2]) 

#String append : adding element
str1 += " welcome"
print(str1)


# why string immutable : 
print("when different varible refer a value .it is difficult to change particualar referance so to avoid it strings are made immutable")


# immutable object can’t be changed after it is created. int, float, bool, string, Unicode and tuple.
# mutable :: can change tuble and list value can be changed but particular 

# list : collection of sequenced items and it is mutable datatype 
# print("list can store hetrogenous items and size can flexable ;; datatype and size have no restrictions"

list1 = [1, 2.2 , "str1", 2+3j,True, ['hi','im here']];

print(list1)

# type
print(type(list1))

# to add item
list1.append("im extra")
print(list1)
print("--------")

# index
print(list1[2])

# slice
print(list1[3])
print(list1[:4])

# accessing list of list
print(list1[5][1])


# string is immutable in python and js not in other lang
print('for loop')
for i in list1:
    print(i)



# tuple
# string and tuple are immutable in python and js not in other lang