# Comparison operators
# These compare two values and return a boolean.
# In mathematics we have operators like >, <, >= etc.

# lets decalare some variables
comp1 = 20
comp2 = 40

print(comp1 < comp2)
print(comp1 > comp2)
print(comp1 >= comp2)
print(comp1 <= comp2)
print(comp1 != comp2)
print(comp1 == comp2)


# NOTE
# 1. Write comments on top of the line you want comment about
# Alway go to the point, follow the rules of english grammer
# 2. There is an assignment that is to be started on thursday as shown on the googel classrom

# Logical Operators
# We have the following, and (&), or (||), not (!)
log1 = 5
log2 = 6
# The and operator in Python returns True if both conditions are True
print((log1 > log2) and (log2 < log1))

# The not operator in Python negates a Boolean value—if something is True
print( not (log2 < log1))

# The or operator in Python returns True if at least one condition is True. It only returns False if both conditions are False
print((log1 > log2) or (log2 < log1))

# This print true
print(True and True)

# This prints False
print(True and False)

# This prints false
print(not True)

# This will print True
print(True or True)

# This will print True
print(True or False)

# This prints false
print(False or False)

# SPECIAL OPERATORS IN PYTHON
# 1. Membership Operators.
# We only have two operators in membership operators ie in and not in
members = {20, 30, 40, 50}
print(20 in members)
print(20 not in members)

name = "Ozzy"
print("o" not in name)
print("O" not in name)


# 2. Identity Operators
# We have is, not is
print(20 is not members)
print(20 is 20)

