# Task 1: Sum of digits for each number in the list
def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

# Task 2: Check if any digit is repeated in a number
def has_repeated_digit(num):
    digits = str(num)
    return len(digits) != len(set(digits))  # If there are repeated digits, set length will be less

# Task 3: Check if the digits of each number are in increasing order
def is_increasing_order(num):
    digits = str(num)
    return all(digits[i] < digits[i + 1] for i in range(len(digits) - 1))

# Example input list
numbers = [568, 89, 112, 88, 571]

# Task 1: Sum of digits for each number
sum_digits_list = [sum_of_digits(num) for num in numbers]
print(f"Sum of digits for each number: {sum_digits_list}")

# Task 2: Check for repeated digits in each number
repeated_digits_check = [has_repeated_digit(num) for num in numbers]
print(f"List with repeated digit check: {repeated_digits_check}")

# Task 3: Check if digits of each number are in increasing order
increasing_order_check = [is_increasing_order(num) for num in numbers]
print(f"List with increasing order check: {increasing_order_check}")



# Sum of digits:
# 
# For 568, the sum is 5 + 6 + 8 = 19.
# For 89, the sum is 8 + 9 = 17.
# For 112, the sum is 1 + 1 + 2 = 4.
# For 88, the sum is 8 + 8 = 16.
# For 571, the sum is 5 + 7 + 1 = 13.
# Repeated digits check:
# 
# 568: No repeated digits → False.
# 89: No repeated digits → False.
# 112: Repeated 1s → True.
# 88: Repeated 8s → True.
# 571: No repeated digits → False.
# Increasing order check:
# 
# 568: Digits are in increasing order 5 < 6 < 8 → True.
# 89: Digits are in increasing order 8 < 9 → True.
# 112: Digits are not in increasing order (1 < 1) → False.
# 88: Digits are not in increasing order (8 == 8) → False.
# 571: Digits are not in increasing order (5 < 7 but 7 > 1) → False.



# TASK 1: Sum of Digits for Each Number in the List

def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

# Example input list
numbers = [568, 89, 112, 88, 571]

# Calculate sum of digits for each number in the list
sum_digits_list = [sum_of_digits(num) for num in numbers]

print(f"Sum of digits for each number: {sum_digits_list}")







# TASK 2: Check if Any Digit is Repeated in the List

def has_repeated_digit(num):
    digits = str(num)
    return len(digits) != len(set(digits))  # If there are repeated digits, set length will be less

# Example input list
numbers = [568, 89, 112, 88, 571]

# Check if any digit is repeated in the list
repeated_digits_check = [has_repeated_digit(num) for num in numbers]

print(f"List with repeated digit check: {repeated_digits_check}")





# TASK 3: Check if Digits in Each Number are in Increasing Order

def is_increasing_order(num):
    digits = str(num)
    return all(digits[i] < digits[i + 1] for i in range(len(digits) - 1))

# Example input list
numbers = [568, 89, 112, 88, 571]

# Check if digits of each number are in increasing order
increasing_order_check = [is_increasing_order(num) for num in numbers]

print(f"List with increasing order check: {increasing_order_check}")

