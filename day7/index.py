# Problem-solving in Python follows the same general principles as problem-solving in other contexts but involves using Python as the tool to implement your solution. The aim is to break down the problem, devise an algorithm, and write code to solve the problem in an efficient way.
 
# In the context of programming with Python, problem-solving has three major aspects:
 
# Understanding the Question (33.33%):
 
# Before jumping into code, it's essential to understand what the problem is asking. Identify inputs, outputs, and the desired behavior of the program. This is the analysis phase where you’ll figure out what the problem actually requires.
# Algorithm (33.33%):
 
# This is the step where you design a strategy or solution to the problem. Choose an efficient approach, like deciding whether to use recursion, iteration, or data structures like lists or dictionaries. This algorithm design step defines how the problem will be solved logically.
# Coding (33.33%):
 
# This is the implementation phase. It involves writing Python code to express the algorithm in a way that the computer can execute. During this step, you translate your solution into Python using syntax and best practices.
# Bonus Points:
# Edge Cases: These are situations that could break your program or make it behave unexpectedly. It is important to handle edge cases, such as empty inputs or extreme values.
# Code Quality: Writing readable, maintainable, and efficient code is essential. Use proper naming conventions, comments, and structure your code for clarity.
# Python Concepts for Problem Solving:
# 1. Declaring Data Types:
# Python supports various data types, including:



# Integer: Whole numbers, e.g., a = 5
# Float: Decimal numbers, e.g., b = 3.14
# String: Text data, e.g., s = "Hello"
# List: Ordered collection of items, e.g., lst = [1, 2, 3]
# Boolean: True or False, e.g., flag = True
# 2. Operators:
# Python provides several types of operators:



# Arithmetic Operators: +, -, *, /, // (floor division), % (modulus), ** (exponentiation)
# Comparison Operators: ==, !=, >, <, >=, <=
# Logical Operators: and, or, not
# Assignment Operators: =, +=, -=, *=, /=
# Membership Operators: in, not in (for checking membership in a sequence like a list or string)
# Identity Operators: is, is not (for comparing object identity)


# 3. Conditional Statements:
# Conditional statements allow your program to execute certain parts of code depending on conditions.

# if: Executes a block of code if the condition is true.

# if x > 10:
    # print("x is greater than 10")
# else: Executes a block of code if the condition is false.

# if x > 10:
    # print("x is greater than 10")
# else:
    # print("x is less than or equal to 10")
# elif: Executes a block of code if the previous condition(s) are false and the elif condition is true.

# if x > 10:
    # print("x is greater than 10")
# elif x == 10:
    # print("x is equal to 10")
# else:
    # print("x is less than 10")


# 4. Loops:
# Loops are used to execute a block of code multiple times.
# 
# while loop: Continues executing as long as a condition is true.
# python
# Copy
i = 0
while i < 5:
    print(i)
    i += 1
# for loop: Iterates over a sequence (e.g., a list).

for i in range(5):
    print(i)
# Jump Statements:
# break: Exits the loop immediately.
# continue: Skips the current iteration and proceeds to the next iteration of the loop.
# python
# Copy
for i in range(5):
    if i == 3:
        continue  # Skips the iteration when i is 3
    print(i)



# 5. Functions:
# Functions help modularize code, make it reusable, and improve readability.
# 
# Declaring a Function:
# python
# Copy
# def greet(name):
    # print(f"Hello, {name}!")
# Calling a Function:
# python
# Copy
# greet("Alice")
# Return Statement: Functions can return values.


def add(a, b):
    return a + b

result = add(3, 4)
print(result)  # Outputs 7


# 6. Inbuilt Functions:
# Python provides many built-in functions for working with common data structures.
# 
# String Functions:
# 
# len(): Returns the length of a string.
# upper(): Converts a string to uppercase.
# lower(): Converts a string to lowercase.
# split(): Splits a string into a list.
# python
# Copy
# name = "Alice"
# print(len(name))  # 5
# print(name.upper())  # "ALICE"
# print(name.split())  # ['Alice']
# List Functions:

# append(): Adds an item to the list.
# remove(): Removes an item from the list.
# sort(): Sorts a list in ascending order.
# python
# Copy
numbers = [3, 1, 2]
numbers.append(4)
numbers.remove(1)
numbers.sort()
print(numbers)  # [2, 3, 4]