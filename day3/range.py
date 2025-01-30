
list1=[1,2,3,4,"string"]
# print directly list
for i in list1:
    print(i)


# without directly using list we can print by using indexing
for i in range(0,len(list1)):
    print(i, list1[i])


# SET : collection of unorder , unique, finate elements .. no indexing and order for set .. in one run the order is same.
set1 = {2, True, "str1"}
print(set1)

# type
print(type(set1))

# length
print(len(set1))

# set1 = {2, True, "str1",[2,3]}  list is not allow bcz list is stored in hashing 
set1 = {2, True, "str1",(2,3)} 
print(set1)



# Dictionary: collection of unique key and value paires where key is unquic and values cano repitation , mutables

d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(d)

d1 = {
    1:'one',
    2:'two',
    3:'three',
    4:'four',
}
print(d1)

# type
print(type(d1))



# access
print(d1[1], d1[3])



# loop
for i in d1:
    print(d1[i])



# None
num1= None
print(num1)



# type
print(type(num1))


# input in python
input("enter input:")

num1 = input("enter num1 : ")
num2 = input("enter num2 : ")
print(num1 + num2) 
# in python input is always taken as string only


# to convert string to int
num1 = int(input("enter num1 : "))
num2 = int(input("enter num2 : "))

#inputs are by default strings...

print(bool(-1));