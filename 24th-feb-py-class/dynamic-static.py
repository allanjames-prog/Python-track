"""In Python, the terms dynamic functions and static functions can refer to different concepts, depending on the context. However, most commonly, they relate to how functions behave or are defined within classes or the type of function they represent."""

"""1. Static Functions (Static Methods)
A static method is a method that belongs to the class, rather than an instance of the class. It does not have access to the instance (self) or class (cls) attributes. Static methods are used when you want to perform a task that is related to the class but does not require access to the instance."""

# You define static methods using the @staticmethod decorator in Python.

# Example:
class MyClass:
    @staticmethod
    def greet():
        print("Hello from a static method!")

# Usage
MyClass.greet()  # No need to instantiate the class

"""Key Points:
- Static methods don't access or modify the state of the instance or the class.
- They can be called on the class itself, not necessarily an instance of the class.
"""
"""2. Dynamic Functions (Instance Methods)
When people talk about dynamic functions in Python, they may refer to regular instance methods or functions that are defined during runtime or belong to the instance of a class."""

"""In Python, instance methods are functions that operate on the instance of the class. These functions always take at least one argument, which is usually self, referring to the instance of the class."""

# Example:
class MyClass:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print(f"Hello, {self.name}!")

# Usage
obj = MyClass("Alice")
obj.greet()  # Instance method called on an object

"""Key Points:
- Instance methods are bound to instances of the class.
- They have access to instance attributes (self) and can modify or interact with them.
- They can be called only after creating an instance of the class."""
    
# Dynamic Nature of Python Functions
"""Python is a dynamically typed language, which means that functions, like other objects, can be created, modified, or deleted at runtime. A function can be assigned to variables, passed around, or even modified dynamically. This flexibility allows for dynamic behavior in how functions are used or defined."""

# For example, you can define a function and later change it at runtime:
def add(a, b):
    return a + b

# Dynamically changing the function
add = lambda a, b: a * b  # Change the function to multiply instead of adding
print(add(2, 3))  # Output: 6

"""Here, the function add is dynamically redefined to perform multiplication instead of addition."""

# Takeaways
"""
- Static functions (static methods) are methods that belong to the class and do not depend on instance-specific data.
- Dynamic functions are typically instance methods or functions defined/modified during runtime, reflecting Python’s dynamic behavior.
"""