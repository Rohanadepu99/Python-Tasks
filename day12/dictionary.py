# 1. Swap keys and values of a dictionary and store keys in a list:

# Function to swap keys and values and store keys in a list
def swap_keys_values(d):
    swapped_dict = {v: k for k, v in d.items()}  # Swap the keys and values
    keys_list = list(d.keys())  # Store the keys in a list
    return swapped_dict, keys_list

# Example
d = {'a': 1, 'b': 2, 'c': 3}
swapped_dict, keys_list = swap_keys_values(d)
print("Swapped Dictionary:", swapped_dict)
print("List of Keys:", keys_list)






# 2. Find the key with the highest value in a dictionary:

# Function to find the key with the highest value
def key_with_highest_value(d):
    return max(d, key=d.get)

# Example
d = {'a': 10, 'b': 20, 'c': 5}
key = key_with_highest_value(d)
print("Key with highest value:", key)






# 3. Return a dictionary of elements that appear more than once along with their counts (frequency of elements in a list):

from collections import Counter

# Function to count elements in a list and return those that appear more than once
def count_occurrences(lst):
    counts = Counter(lst)
    return {key: value for key, value in counts.items() if value > 1}

# Example
lst = [1, 2, 2, 3, 4, 4, 5]
result = count_occurrences(lst)
print("Elements appearing more than once:", result)





# 4. Merge two dictionaries and sum their values if the key exists in both:

# Function to merge two dictionaries and sum values for common keys
def merge_and_sum_dicts(d1, d2):
    merged_dict = d1.copy()  # Copy the first dictionary
    for key, value in d2.items():
        if key in merged_dict:
            merged_dict[key] += value  # Sum the values if the key exists in both
        else:
            merged_dict[key] = value  # Add the key-value pair if not present
    return merged_dict

# Example
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
merged = merge_and_sum_dicts(d1, d2)
print("Merged Dictionary:", merged)





# 5. Check if two strings are anagrams:

# Function to check if two strings are anagrams
def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

# Example
str1 = "listen"
str2 = "silent"
result = are_anagrams(str1, str2)
print("Are the strings anagrams?", result)






# Count Occurrences of Each Digit in an Integer (e.g., 2788):

# Function to count occurrences of each digit in a number
def count_digit_occurrences(num):
    num_str = str(num)
    digit_count = {}
    for digit in num_str:
        if digit in digit_count:
            digit_count[digit] += 1
        else:
            digit_count[digit] = 1
    return digit_count

# Example
num = 2788
digit_counts = count_digit_occurrences(num)
for digit, count in digit_counts.items():
    print(f"{digit} => {count}")
