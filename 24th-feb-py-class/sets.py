# 1. What is a Set?
# A set in Python is an unordered, mutable, and unindexed collection of unique elements. It is defined using curly braces {} or the set() constructor.

# Example:
# Creating a set
numbers = {1, 2, 3, 4, 5}
print(numbers)  # Output: {1, 2, 3, 4, 5}

# Key Features of Sets:
# Unordered: Elements have no specific order.
# Unique Elements: No duplicates allowed.
# Mutable: You can add or remove items.
# Unindexed: Cannot access elements by index.

# 2. Creating Sets
# 1. Using Curly Braces {}
fruits = {"apple", "banana", "cherry"}
print(fruits)  # Output: {'banana', 'cherry', 'apple'} (order may vary)

# 2. Using set() Constructor
fruits = set(["apple", "banana", "cherry"])
print(fruits)  # Output: {'banana', 'cherry', 'apple'}

# 3. Creating an Empty Set (Use set(), Not {})
empty_set = set()  # Correct
empty_dict = {}  # This creates an empty dictionary, not a set

# 3. Accessing Set Elements
# Sets are unordered, so you cannot access elements by index or slice them.

# Checking Membership (in Operator)
fruits = {"apple", "banana", "cherry"}
print("apple" in fruits)  # Output: True
print("grape" in fruits)  # Output: False

# 4. Adding and Removing Elements
# 1. Adding Elements (add())
fruits = {"apple", "banana"}
fruits.add("cherry")
print(fruits)  # Output: {'banana', 'cherry', 'apple'}

# 2. Adding Multiple Elements (update())
fruits.update(["orange", "grape"])
print(fruits)  # Output: {'banana', 'cherry', 'apple', 'orange', 'grape'}

# 3. Removing Elements
# remove() (Raises an error if the element does not exist)
fruits.remove("banana")
print(fruits)  # Output: {'cherry', 'apple'}
# discard() (Does NOT raise an error if the element does not exist)
fruits.discard("grape")  # No error if "grape" is not in the set
# pop() (Removes a random element)
fruits.pop()
print(fruits)  # Removes and returns a random item
# clear() (Removes all elements)
fruits.clear()
print(fruits)  # Output: set()

# 5. Set Operations (Mathematical Operations)
# Python sets support union, intersection, difference, and symmetric difference operations.

# 1. Union (| or union())
# Combines elements from two sets (removes duplicates).
A = {1, 2, 3}
B = {3, 4, 5}
print(A | B)  # Output: {1, 2, 3, 4, 5}
print(A.union(B))  # Same as above

# 2. Intersection (& or intersection())
# Finds common elements in both sets.
print(A & B)  # Output: {3}
print(A.intersection(B))  # Same as above

# 3. Difference (- or difference())
# Finds elements in the first set but not in the second.
print(A - B)  # Output: {1, 2}
print(A.difference(B))  # Same as above
# 4. Symmetric Difference (^ or symmetric_difference())
# Finds elements that are in either set but not both.
print(A ^ B)  # Output: {1, 2, 4, 5}
print(A.symmetric_difference(B))  # Same as above

# 6. Set Methods & Functions
# Method	- Description
# add(x)	- Adds an element x to the set
# update(iterable)	- Adds multiple elements to the set
# remove(x)	- Removes x (raises an error if x doesn’t exist)
# discard(x)	- Removes x (does NOT raise an error)
# pop()	- Removes and returns a random element
# clear()	- Removes all elements from the set
# union(set2)	- Returns a set containing all unique elements from both sets
# intersection(set2)	- Returns a set of common elements
# difference(set2)	- Returns elements only in the first set
# symmetric_difference(set2)	- Returns elements in either set, but not both
# issubset(set2)	- Checks if the set is a subset of set2
# issuperset(set2)	- Checks if the set is a superset of set2
# copy()	- Returns a shallow copy of the set

# 7. Checking Subsets and Supersets
# issubset() → Checks if one set is fully contained in another.
A = {1, 2}
B = {1, 2, 3, 4}
print(A.issubset(B))  # Output: True
# issuperset() → Checks if one set fully contains another.
print(B.issuperset(A))  # Output: True

# isdisjoint() → Checks if two sets have no elements in common.
C = {7, 8, 9}
print(A.isdisjoint(C))  # Output: True

# 8. Converting Other Data Structures to Sets
# List to Set
numbers = [1, 2, 2, 3, 4, 4]
unique_numbers = set(numbers)
print(unique_numbers)  # Output: {1, 2, 3, 4}

# String to Set
letters = set("hello")
print(letters)  # Output: {'h', 'e', 'l', 'o'} (order may vary)

# Set to List
numbers = {1, 2, 3, 4}
numbers_list = list(numbers)
print(numbers_list)  # Output: [1, 2, 3, 4]

# 9. Use Cases of Sets
# Removing Duplicates from a List
nums = [1, 2, 2, 3, 4, 4]
unique_nums = list(set(nums))
print(unique_nums)  # Output: [1, 2, 3, 4]

# Membership Testing (Fastest Method)
words = {"python", "java", "c++"}
print("python" in words)  # Output: True

# Finding Unique Characters in a String
text = "mississippi"
unique_chars = set(text)
print(unique_chars)  # Output: {'m', 's', 'p', 'i'}

# Relevance
# Sets are powerful, efficient, and useful for unique data storage.
# They provide fast membership tests and mathematical operations.
# Unlike lists, sets do not allow duplicates and are unordered.