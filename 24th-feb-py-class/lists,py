
# LISTS and DICTIONARIES

"""A list in Python is an ordered, mutable collection of items that can hold elements of different data types (integers, floats, strings, objects, even other lists). Lists are one of the most commonly used data structures in Python.
"""
"""1. Creating Lists
1.1 Empty List"""
my_list = []
# Using the list() function/method
my_list = list()  

# 1.2 List with Elements
numbers = [1, 2, 3, 4, 5]
# Different data types
mixed = [1, "hello", 3.5, True]  
# List inside a list
nested = [[1, 2], [3, 4]]  

"""2. Accessing Elements
2.1 Indexing (Starts at 0)"""
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # apple
print(fruits[1])  # banana
print(fruits[-1])  # Last item -> cherry

# 2.2 Slicing [start:stop:step]
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])  # [20, 30, 40] (Excludes index 4)
print(numbers[:3])  # [10, 20, 30] (First 3 elements)
print(numbers[::2])  # [10, 30, 50] (Every second element)

"""Modifying Lists
3.1 Changing Elements"""
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"  # Replace banana with blueberry
print(fruits)  # ['apple', 'blueberry', 'cherry']

"""3.2 Adding Elements
Append (Adds to the end)"""
fruits.append("mango")

# Insert at a specific position
fruits.insert(1, "orange")

# Extend (Concatenates another list)
fruits.extend(["grapes", "kiwi"])

print(fruits)  # ['apple', 'orange', 'blueberry', 'cherry', 'mango', 'grapes', 'kiwi']
# 3.3 Removing Elements
fruits.remove("cherry")  # Removes by value
popped_item = fruits.pop(2)  # Removes by index, returns the item
del fruits[0]  # Deletes first element
fruits.clear()  # Empties the list

"""4. List Operations
4.1 Concatenation and Repetition"""
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2  # [1, 2, 3, 4, 5, 6]
repeated = list1 * 3  # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# 4.2 Checking Membership
print(3 in list1)  # True
print(7 not in list1)  # True

# 5. Iterating Through Lists
fruits = ["apple", "banana", "cherry"]
# Looping through items
for fruit in fruits:
    print(fruit)

# Looping with index
for index, fruit in enumerate(fruits):
    print(index, fruit)

"""6. Useful List Methods
Method	Description
append(x)	Adds x to the end
insert(i, x)	Inserts x at index i
extend(iterable)	Adds multiple elements from an iterable
remove(x)	Removes the first occurrence of x
pop(i)	Removes and returns element at index i (default last)
clear()	Removes all elements
index(x)	Returns index of first occurrence of x
count(x)	Counts occurrences of x
sort()	Sorts list (ascending by default)
reverse()	Reverses the list
copy()	Returns a shallow copy of the list
Example:"""
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()  # [1, 1, 2, 3, 4, 5, 9]
numbers.reverse()  # [9, 5, 4, 3, 2, 1, 1]

"""7. List Comprehension
A concise way to create lists."""
squares = [x**2 for x in range(1, 6)]  # [1, 4, 9, 16, 25]
even_numbers = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

"""8. Copying Lists
8.1 Incorrect Copy (Creates Reference)"""
list1 = [1, 2, 3]
list2 = list1  # Both point to the same list!
list2.append(4)
print(list1)  # [1, 2, 3, 4]

# 8.2 Correct Copy (Creates a New List)
list2 = list1.copy()  # or list1[:]
list2.append(4)
print(list1)  # [1, 2, 3] (Unchanged)

# 9. Nested Lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][2])  # 6 (Row index 1, Column index 2)

"""10. Common Mistakes
10.1 IndexError (Out of Range)"""
fruits = ["apple", "banana"]
print(fruits[2])  # ❌ IndexError: list index out of range

# 10.2 Using = Instead of copy()
list1 = [1, 2, 3]
list2 = list1  # ❌ Both now refer to the same object!

"""When to Use Lists?
When you need an ordered collection.
When you need to modify elements (unlike tuples).
When you need fast iteration and random access."""


"""Relevance
✔ Lists are ordered, mutable collections.
✔ Support indexing, slicing, and iteration.
✔ Can hold different data types.
✔ Provide various methods for adding, removing, and modifying elements.
✔ Use list comprehension for efficiency.
✔ Use copy() instead of = to avoid reference issues."""

