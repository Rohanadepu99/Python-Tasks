# TASK 1: Find the Sum of All Elements in a Nested List
# To find the sum of all elements in a nested list, you can use a recursive approach that handles each nested list inside the main list.



# python

def sum_nested_list(nested_list):
    total_sum = 0
    for element in nested_list:
        if isinstance(element, list):  # Check if the element is a list
            total_sum += sum_nested_list(element)  # Recursively call the function
        else:
            total_sum += element  # If it's a number, add to total
    return total_sum

# Example:
nested_list = [1, [2, 3], [4, [5, 6]], 7]
result = sum_nested_list(nested_list)
print(f"The sum of all elements in the nested list is: {result}")


# TASK 2: Find the Minimum and Maximum Values in a Nested List
# To find the minimum and maximum values in a nested list, you can also use recursion to traverse through the nested structure.

# Here’s the Python code for finding the minimum and maximum:


def find_min_max(nested_list):
    min_val = float('inf')  # Initialize with positive infinity
    max_val = float('-inf')  # Initialize with negative infinity
    
    for element in nested_list:
        if isinstance(element, list):  # If it's a sublist, recursively call the function
            sub_min, sub_max = find_min_max(element)
            min_val = min(min_val, sub_min)
            max_val = max(max_val, sub_max)
        else:
            min_val = min(min_val, element)
            max_val = max(max_val, element)
    
    return min_val, max_val

# Example:
nested_list = [1, [2, 3], [4, [5, 6]], 7]
min_val, max_val = find_min_max(nested_list)
print(f"The minimum value in the nested list is: {min_val}")
print(f"The maximum value in the nested list is: {max_val}")


# Revision on Binary Search and Bubble Sort
# 1. Binary Search
# Binary search is an efficient algorithm to find an element in a sorted list. It works by repeatedly dividing the search interval in half. If the value of the search key is less than the value in the middle of the interval, the algorithm narrows the interval to the lower half. Otherwise, it narrows it to the upper half.


def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2  # Find the middle index
        if arr[mid] == target:
            return mid  # Target found at index mid
        elif arr[mid] < target:
            low = mid + 1  # Narrow the search to the upper half
        else:
            high = mid - 1  # Narrow the search to the lower half
    return -1  # Target not found

# Example:
arr = [1, 3, 5, 7, 9, 11]
target = 7
result = binary_search(arr, target)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
# Time Complexity: O(log n), where n is the number of elements in the list.

# 2. Bubble Sort
# Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Flag to optimize if no swaps were made in the inner loop
        swapped = False
        for j in range(0, n-i-1):  # Last i elements are already sorted
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap if the elements are in wrong order
                swapped = True
        if not swapped:
            break  # If no elements were swapped, the list is already sorted

# Example:
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array:", arr)
# Time Complexity: O(n^2), where n is the number of elements in the list.
# Sorting a List from Lower Value to Higher
# To sort a list in Python from lower value to higher, you can use the sort() function or sorted() function.


# Example:
arr = [64, 34, 25, 12, 22, 11, 90]
arr.sort()  # Sorts the list in-place from low to high
print("Sorted list:", arr)
# Alternatively, to sort a list in descending order (higher to lower):
# python

arr.sort(reverse=True)  # Sorts the list from high to low
print("Sorted list in descending order:", arr)