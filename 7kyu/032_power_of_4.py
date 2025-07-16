# Power of 4

# ---
# ## CodeWars Description
# Write a method that returns true if a given parameter is a power of 4, and false if it's not. If parameter is not an Integer (eg String, Array) method should return false as well.
# (In C# Integer means all integer Types like Int16,Int32,.....)
# Examples
# powerOf4(1024) // returns true
# powerOf4(44) // returns false
# powerOf4("not a positive integer") // returns false

# ---
# ## Solution

from math import log

def powerof4(n):
    # Check if the input 'n' is an integer or a float and is positive.
    if type(n) in (float, int) and n > 0:
        # Calculate the logarithm of 'n' with base 4.
        # If 'n' is a power of 4, log(n, 4) will be an integer.
        # .is_integer() checks if a float value is an integer.
        return log(n, 4).is_integer()
    # If 'n' is not a number or not positive, return False.
    return False
