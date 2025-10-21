print("Lets learn Data Types with Python")
#--------------------------------------------------------------
# Data Types with Python
#-------------------------------------------------------------

# Data types in python are a way to classify data items
# They represent the kind of value, which determines what operations can be performed on the data
# Since everything is an object in python programming
# Python data types are classes and variables are instances (objects) of those classes


"""
The following are standard or built in data types in Python:
--------------------------------------------------------------
    Numeric: int, float, complex
    Sequence Type: string, list, tuple
    Mapping Type: dict
    Boolean: bool
    Set Type: set, frozenset
    Binary Types: bytes, bytearray, memoryview
"""

# Below code assigns variable 'x' different values of a few Python data Types
# int, float, list, tuple and string.
# Each assignment replaces previous value making 'x' take on the data type and value of most recent assignment 

x = 50 # int
x = 60.5 # float
x = "Hello team" # string
x = ["python", "for", "aws"] # list
x = ("python", "for", "aws") # tuple
print(x) # This will print the most recent data type which is the tuple

# Output of this will look like:
"""
('python', 'for', 'aws')
    
"""

# Numeric Data Types 

# python numbers represent data that has a numeric value
# A numeric value can be an integer , a floating number or even a complex number
# These values are defined as int, float and complex classes
"""
Integers: value is represented by int class. It contains positive or negative whole numbers (without fractions or decimals). 
There is no limit to how long an integer value can be.

Float: value is represented by float class. 
It is a real number with a floating-point representation. 
It is specified by a decimal point. 

Complex Numbers: It is represented by a complex class. 
It is specified as (real part) + (imaginary part)j.
For example - 2+3j


"""
a = 5
print(type(a))

b = 5.0
print(type(b))

c = 2 +3j
print(type(c))

# The output will look like: 
"""
<class 'int'>
<class 'float'>
<class 'complex'>
    
"""

wel = "Welcome to Python data types"
print(wel)

# check data type
print(type(wel))

# access string with index (0, 1, 2, 3,)
print(wel[1]) # prints the second index or letter 
print(wel[2]) # prints the third index
print(wel[-1]) # -1 would start from the last letter from the back

# The output would look like: 
"""
Welcome to Python data types
<class 'str'>
e
l
s

"""

#----------LIST-DATA-TYPE----------------

"""
Lists are similar to arrays found in other languages. 
They are an ordered and mutable collection of items. 
It is very flexible as items in a list do not need to be of the same type.

Creating a List in Python

Lists in Python can be created by just
placing the sequence inside the square brackets[].
"""
#---------------LIST-EXAMPLE------------------

# Empty list 
list = []

# List with int values
list_int = [1, 2, 3]
print(list_int)

# list with mixed values int and string
list_val = ["byte", "gb", 1, 4, 5]
print(list_val)

# The output would look like : 
"""
[1, 2, 3]
['byte', 'gb', 1, 4, 5]

"""