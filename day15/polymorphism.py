# Merging Two Sorted Lists Using OOP
# Create a class MergeSortedLists.
 
# Define an __init__ method to initialize the two sorted lists.
 
# Define a merge method that will merge the two sorted lists using a two-pointer approach (commonly used in merge sort).

# Return the merged sorted list.



class MergeSortedLists:
    def __init__(self, list1, list2):
        """Initializes the two sorted lists"""
        self.list1 = list1
        self.list2 = list2

    def merge(self):
        """Merges two sorted lists into one sorted list"""
        # Initialize pointers for both lists
        i, j = 0, 0
        merged_list = []

        # Traverse both lists and merge them
        while i < len(self.list1) and j < len(self.list2):
            if self.list1[i] < self.list2[j]:
                merged_list.append(self.list1[i])
                i += 1
            else:
                merged_list.append(self.list2[j])
                j += 1

        # If there are remaining elements in list1
        while i < len(self.list1):
            merged_list.append(self.list1[i])
            i += 1

        # If there are remaining elements in list2
        while j < len(self.list2):
            merged_list.append(self.list2[j])
            j += 1

        return merged_list


# Example usage:
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]

# Create an object of MergeSortedLists
merger = MergeSortedLists(list1, list2)

# Merge the lists and print the result
merged_list = merger.merge()
print("Merged Sorted List:", merged_list)
