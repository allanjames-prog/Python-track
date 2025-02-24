# What Are Operators?
# Operators in Python are special symbols used to perform operations on values and variables. Python provides several types of operators, including arithmetic, comparison, logical, bitwise, assignment, identity, and membership operators.

# 1. Types of Operators in Python
# Arithmetic Operators
# Comparison (Relational) Operators
# Logical Operators
# Bitwise Operators
# Assignment Operators
# Identity Operators
# Membership Operators

# 1. Arithmetic Operators
# These operators perform mathematical operations such as addition, subtraction, multiplication, division, etc.

# Operator	Name	Example	Result
# +	Addition	5 + 3	8
# -	Subtraction	5 - 3	2
# *	Multiplication	5 * 3	15
# /	Division	5 / 2	2.5
# //	Floor Division	5 // 2	2 (Removes decimal)
# %	Modulus (Remainder)	5 % 2	1
# **	Exponentiation	5 ** 2	25
# Example:
a = 10
b = 3
print(a + b)  # Output: 13
print(a - b)  # Output: 7
print(a * b)  # Output: 30
print(a / b)  # Output: 3.3333
print(a // b)  # Output: 3
print(a % b)  # Output: 1
print(a ** b)  # Output: 1000

# 2. Comparison (Relational) Operators
# Used to compare two values and return True or False.

# Operator	Name	Example	Result
# ==	Equal to	5 == 3	False
# !=	Not equal to	5 != 3	True
# >	Greater than	5 > 3	True
# <	Less than	5 < 3	False
# >=	Greater than or equal to	5 >= 3	True
# <=	Less than or equal to	5 <= 3	False
# Example:
x = 10
y = 5
print(x == y)  # False
print(x != y)  # True
print(x > y)   # True
print(x < y)   # False
print(x >= y)  # True
print(x <= y)  # False

# 3. Logical Operators
# Used to combine conditional statements.

# Operator	Description	Example
# and	Returns True if both conditions are true	(5 > 3) and (10 > 5) → True
# or	Returns True if at least one condition is true	(5 > 3) or (10 < 5) → True
# not	Reverses the result	not(5 > 3) → False
# Example:

x = True
y = False
print(x and y)  # Output: False
print(x or y)   # Output: True
print(not x)    # Output: False

# 4. Bitwise Operators
# Used to perform bit-level operations.

# Operator	Name	Example	Result
# &	AND	5 & 3	1
# `	`	OR	`5
# ^	XOR	5 ^ 3	6
# ~	NOT	~5	-6
# <<	Left shift	5 << 1	10
# >>	Right shift	5 >> 1	2
# Example:

a = 5  # 101 in binary
b = 3  # 011 in binary

print(a & b)  # Output: 1 (001)
print(a | b)  # Output: 7 (111)
print(a ^ b)  # Output: 6 (110)
print(~a)     # Output: -6
print(a << 1) # Output: 10 (Shifts bits left)
print(a >> 1) # Output: 2 (Shifts bits right)

# 5. Assignment Operators
# Used to assign values to variables.

# Operator	Example	Equivalent to
# =	x = 5	x = 5
# +=	x += 3	x = x + 3
# -=	x -= 3	x = x - 3
# *=	x *= 3	x = x * 3
# /=	x /= 3	x = x / 3
# //=	x //= 3	x = x // 3
# %=	x %= 3	x = x % 3
# **=	x **= 3	x = x ** 3
# &=	x &= 3	x = x & 3
# `	=`	`x
# ^=	x ^= 3	x = x ^ 3
# <<=	x <<= 3	x = x << 3
# >>=	x >>= 3	x = x >> 3
# Example:
x = 10
x += 5
print(x)  # Output: 15

# 6. Identity Operators
# Used to compare memory locations of two objects.

# Operator	Description	Example
# is	Returns True if both variables refer to the same object	x is y
# is not	Returns True if variables do not refer to the same object	x is not y
# Example:
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # Output: True (same object)
print(a is c)  # Output: False (different objects with same values)
print(a == c)  # Output: True (values are equal)

# 7. Membership Operators
# Used to test if a value is in a sequence (list, tuple, set, string, dictionary).

# Operator	Description	Example
# in	Returns True if value exists in sequence	"a" in "apple"
# not in	Returns True if value does NOT exist in sequence	"x" not in "apple"
# Example:
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)  # Output: True
print("grape" not in fruits)  # Output: True

# Relevance
# Python operators allow you to perform various operations on variables and values.
# Arithmetic, Comparison, Logical, Bitwise, Assignment, Identity, and Membership operators serve different purposes.
# Operators can be used in expressions, conditions, and loop controls.