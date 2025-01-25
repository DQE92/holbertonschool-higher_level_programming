#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers or floats and returns the result as an integer.
    
    Parameters:
    - a: The first number (int or float).
    - b: The second number (int or float), default is 98.
    
    Returns:
    - int: The addition of a and b after casting them to integers.
    
    Raises:
    - TypeError: If a or b is not an integer or a float.
    """
    # Check if 'a' is an integer or float
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    
    # Check if 'b' is an integer or float
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    # Convert 'a' and 'b' to integers if they are floats
    a = int(a)
    b = int(b)
    
    # Return their sum
    return a + b
