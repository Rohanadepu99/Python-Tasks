# Introduction to OOP (Object-Oriented Programming) in Python
# Object-Oriented Programming is a programming paradigm that organizes code into "objects." These objects are instances of classes, and each class defines properties (attributes) and methods (functions) that are associated with these objects.
 
# The four main principles of OOP are:
 
# Encapsulation: Bundling data and methods that operate on that data within a single unit (class).
 
# Inheritance: Creating a new class that is based on an existing class.
 
# Polymorphism: Allowing methods to have the same name but behave differently based on the object calling them.
 
# Abstraction: Hiding the complex implementation details and exposing only the necessary parts of the object.
 
# Diamond Pattern Using OOP
# We'll create a class called DiamondPattern that has methods to print a diamond-shaped pattern. The pattern will depend on the number of rows (which should be an odd number to form a symmetric diamond).

# Here's how you can do it:


class DiamondPattern:
    def __init__(self, n):
        """Initializes the number of rows in the diamond"""
        self.n = n

    def print_upper_half(self):
        """Prints the upper half of the diamond"""
        for i in range(1, self.n + 1, 2):
            spaces = ' ' * ((self.n - i) // 2)  # Calculate spaces before stars
            stars = '*' * i  # Number of stars in the row
            print(spaces + stars)

    def print_lower_half(self):
        """Prints the lower half of the diamond"""
        for i in range(self.n - 2, 0, -2):
            spaces = ' ' * ((self.n - i) // 2)  # Calculate spaces before stars
            stars = '*' * i  # Number of stars in the row
            print(spaces + stars)

    def print_diamond(self):
        """Prints the complete diamond pattern"""
        self.print_upper_half()  # Print the upper half
        self.print_lower_half()  # Print the lower half

# Driver code
n = 7  # Example: number of rows (must be odd)
diamond = DiamondPattern(n)
diamond.print_diamond() 

# Explanation:

# Class Definition:

# DiamondPattern class is defined with an __init__ method to initialize the number of rows (n).
 
# Methods:
 
# print_upper_half(): This method prints the top half of the diamond (including the middle row).
 
# print_lower_half(): This method prints the bottom half of the diamond.
 
# print_diamond(): This method calls both print_upper_half and print_lower_half to print the full diamond.
 
# Spaces and Stars Calculation:
 
# For each row, spaces are calculated based on the total number of rows, and stars are printed accordingly. The number of stars increases until the middle, then decreases symmetrically.