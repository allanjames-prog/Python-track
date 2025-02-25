# Tuples in Python
# A tuple is an ordered, immutable collection of items in Python. It is similar to a list but with the key difference that tuples cannot be modified (immutable) after creation.

# Key Features of Tuples
# 1. Ordered → Items retain their position.
# 2. Immutable → Cannot be changed (no adding, removing, or modifying elements).
# 3. Allows Duplicates → Can store repeated values.
# 4. Can Hold Mixed Data Types → Strings, integers, lists, etc.
# 5. Faster than Lists → Tuples are more memory efficient.


# Creating a Tuple

# Tuple with multiple values
my_tuple = (10, 20, 30, "Hello", 50.5)
print(my_tuple)

# Note: Tuples can also be created without parentheses, using just commas:
my_tuple = 10, 20, 30
print(my_tuple)  # Output: (10, 20, 30)


# Accessing Elements
print(my_tuple[0])  # First element: 10
print(my_tuple[-1])  # Last element: 50.5

# Tuple Unpacking
a, b, c = (1, 2, 3)
print(a, b, c)  # Output: 1 2 3


# Immutable Property (Throws Error)
my_tuple[1] = 100  # TypeError: 'tuple' object does not support item assignment

# Tuple Methods
# Tuples have very few built-in methods:

t = (1, 2, 3, 2, 2, 4)

print(len(t))      # Count elements → Output: 6
print(t.count(2))  # Count occurrences of 2 → Output: 3
print(t.index(3))  # Find index of 3 → Output: 2

# When to Use Tuples Instead of Lists?
#  When you need data protection (no modifications).
#  When you want faster performance in large data collections.
#  When working with fixed data (e.g., coordinates, database records).

