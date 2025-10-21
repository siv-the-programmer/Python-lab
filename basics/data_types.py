print("Lets learn Data Types with Python")
#--------------------------------------------------------------
# Data Types with Python
#-------------------------------------------------------------

# Data types in python are a way to classify data items
# They represent the kind of value, which determines what operations can be performed on the data
# Since everything is an object in python programming
# Python data types are classes and variables are instances (objects) of those classes


"""
The following are starndard or built in data types in Python:
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
# 