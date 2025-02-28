"""Conditional Statements in Python
Conditional statements in Python allow the program to execute different blocks of code based on conditions. These statements include if, elif, and else."""

"""1. The if Statement
The if statement evaluates a condition (expression that returns True or False). If the condition is True, the indented block of code under it executes.
if condition:"""
    # Code block executed if condition is True
age = 18
if age >= 18:
    print("You are an adult.")  # This runs because the condition is True

"""2. The if-else Statement
The else statement is used to execute a block of code when the if condition is False.
if condition:
    # Executes if condition is True
# else:
    # Executes if condition is False"""

# Example
age = 16
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")  # This runs because the condition is False
"""3. The if-elif-else Statement
The elif (short for "else if") allows checking multiple conditions."""
"""if condition1:
    Executes if condition1 is True
elif condition2:
    Executes if condition1 is False and condition2 is True
else:
    Executes if all conditions are False"""

# Example
score = 75

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")  # This runs because 75 >= 70
else:
    print("Grade: F")

"""4. Nested if Statements
You can nest if statements inside other if statements."""

# Example
num = 10

if num > 0:
    print("Positive number")
    if num % 2 == 0:
        print("Even number")  # This runs because num is positive and even

"""5. Logical Operators in Conditional Statements
Python provides logical operators to combine multiple conditions."""

"""Operator	Description	Example
and	Returns True if both conditions are True	x > 5 and x < 10
or	Returns True if at least one condition is True	x < 5 or x > 10
not	Negates a condition (True becomes False and vice versa)	not(x > 5)"""

# Example
x = 7
if x > 5 and x < 10:
    print("x is between 5 and 10")  # This runs because both conditions are True

"""6. Conditional Expressions (Ternary Operator)
Python allows a shorthand if-else expression using the ternary operator.
value_if_true if condition else value_if_false"""

# Example
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)  # Output: Adult

"""7. Using in with if Statements
You can check if a value exists in a list, tuple, dictionary, or string."""

# Example
fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("Banana is in the list.")

"""8. pass Statement in Conditional Blocks
The pass statement is used when a block is syntactically required but you don’t want to execute any code."""

# Example
x = 10
if x > 5:
    pass  # Placeholder for future code

"""9. Short-Circuiting in Logical Operators
For and: If the first condition is False, Python doesn’t evaluate the second condition.
For or: If the first condition is True, Python doesn’t evaluate the second condition."""

# Example
x = 10
y = 0

if y != 0 and x / y > 5:
    print("This won't run")  # The second condition is never checked to avoid ZeroDivisionError

"""10. Comparing Values in Conditional Statements
Python supports different comparison operators in conditional statements:"""

"""Operator	Description	Example (a = 5, b = 10)
==	Equal to	a == b → False
!=	Not equal to	a != b → True
>	Greater than	a > b → False
<	Less than	a < b → True
>=	Greater than or equal to	a >= b → False
<=	Less than or equal to	a <= b → True"""

"""11. Handling Multiple Conditions with match (Python 3.10+)
Python 3.10 introduced the match statement (similar to switch-case in other languages)."""

# Example
status_code = 200

match status_code:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:
        print("Unknown Status")  # Default case

"""Key takeaways:
Use if, elif, and else for flow control.
Use logical operators (and, or, not) to combine conditions.
Use ternary expressions for compact if-else statements.
Use match for multi-case conditions (Python 3.10+).
Short-circuiting helps optimize performance in complex conditions."""