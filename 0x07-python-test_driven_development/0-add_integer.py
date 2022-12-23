
#!/usr/bin/python3
"""
This module is composed by a function that adds two numbers
"""

def add_integer(a, b=98):
    # Check if a is an integer or a float
    if not isinstance(a, (int, float)):
        # If a is not an integer or a float, raise a TypeError exception
        raise TypeError('a must be an integer or a float')
    # Check if b is an integer or a float
    if not isinstance(b, (int, float)):
        # If b is not an integer or a float, raise a TypeError exception
        raise TypeError('b must be an integer or a float')
    # Cast a and b to integers if they are floats
    # Return the sum of a and b as an integer
    return int(a) + int(b)

