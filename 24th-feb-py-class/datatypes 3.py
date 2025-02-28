"""1. What Are Key-Value Pairs?
A key-value pair consists of:"""

"""A key → A unique identifier (e.g., a name, ID, or label).
A value → The associated data (e.g., a number, string, list, or another dictionary).
Example:"""

student = {"name": "Allan", "age": 25, "city": "Kampala"}

""""name" → Key
"Allan" → Value
"age": 25, "city": "Kampala" → More key-value pairs"""



"""2. Creating Key-Value Pairs (Dictionaries)
Dictionaries (dict) are the most common way to store key-value pairs in Python."""

# Method 1: Using Curly Braces ({})
person = {
    "name": "James",
    "age": 30,
    "city": "Nairobi"
}

# Method 2: Using dict() Constructor
person = dict(name="James", age=30, city="Nairobi")

# Method 3: Creating an Empty Dictionary and Adding Key-Value Pairs
person = {}
person["name"] = "James"
person["age"] = 30
person["city"] = "Nairobi"



"""3. Accessing Key-Value Pairs
Using Keys ([] notation)"""

print(person["name"])  # Output: James
# Error Alert! If the key doesn’t exist, Python raises a KeyError.

# Using get() Method (Prevents Errors)
print(person.get("name"))   # Output: James
print(person.get("gender", "Not Found"))  # Output: Not Found



# 4. Modifying Key-Value Pairs
person["age"] = 31  # Update age
person["country"] = "Kenya"  # Add new key-value pair



# 5. Removing Key-Value Pairs
del person["city"]  # Removes "city" key
age = person.pop("age")  # Removes "age" and returns its value



"""6. Looping Through Key-Value Pairs
Loop Through Keys"""
for key in person:
    print(key)  # Prints: name, country

    

# Loop Through Values
for value in person.values():
    print(value)  # Prints: James, Kenya

# Loop Through Both Keys and Values
for key, value in person.items():
    print(f"{key}: {value}")

# 7. Checking If a Key Exists
if "name" in person:
    print("Key exists!")

"""8. Dictionary Methods for Key-Value Pairs
Method	- Description
keys()	- Returns all keys
values()	Returns all values
items()	Returns key-value pairs as tuples
get(key, default)	Returns value or default if key not found
pop(key, default)	Removes and returns value of key
update(dict2)	Updates dictionary with another dictionary"""

# Example:
print(person.keys())    # Output: dict_keys(['name', 'country'])
print(person.values())  # Output: dict_values(['James', 'Kenya'])
print(person.items())   # Output: dict_items([('name', 'James'), ('country', 'Kenya')])

# 9. Nested Key-Value Pairs (Dictionaries Inside Dictionaries)
students = {
    "student1": {"name": "Allan", "age": 22},
    "student2": {"name": "Dorothy", "age": 23}
}
print(students["student1"]["name"])  # Output: Allan

# 10. Key-Value Pairs in Other Data Structures
# 1. List of Dictionaries
people = [
    {"name": "Alice", "age": 28},
    {"name": "Bob", "age": 25}
]

# 2. Using Tuples for Key-Value Pairs
pairs = (("name", "James"), ("age", 30))
person = dict(pairs)

"""11. Use Cases of Key-Value Pairs
Databases (storing user info in key-value format)
API Responses (JSON data is structured as key-value pairs)
Configurations (settings stored in key-value format)
Caching (fast lookups using dictionaries)"""

"""12. Converting Key-Value Pairs
Convert Dictionary to JSON"""
import json
data = {"name": "James", "age": 30}
json_data = json.dumps(data)
print(json_data)  # Output: '{"name": "James", "age": 30}'

# Convert JSON to Dictionary
dict_data = json.loads(json_data)
print(dict_data["name"])  # Output: James

"""Relevance
Key-value pairs are essential for efficient data storage and retrieval.
Dictionaries are the most common way to store them in Python.
Methods like .items(), .keys(), and .values() help in working with key-value pairs efficiently."""

