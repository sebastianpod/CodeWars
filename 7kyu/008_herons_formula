# Heron's formula

# ---
# ## CodeWars Description
# Write function heron which calculates the area of a triangle with sides a, b, and c.
# Heron's formula:
# s*(s-a)*(s-b)*(s-c)
# where: s = (a+b+c)/2
# Notes
# All inputs are valid triangles with integer sides.
# You do not need to round anything. Answers will be tested for correctness within a margin of 0.01.

# ---
# ## Solution

import math

def heron(a, b, c):
    # Calculate the semi-perimeter 's' of the triangle.
    # The semi-perimeter is half the sum of the lengths of the three sides.
    s = (a + b + c) / 2
    
    # Apply Heron's formula to calculate the area of the triangle.
    # The formula is: sqrt(s * (s - a) * (s - b) * (s - c)).
    # math.sqrt() is used to calculate the square root.
    # The result is rounded to 2 decimal places as per the user's original code.
    return round(math.sqrt(s * (s - a) * (s - b) * (s - c)), 2)
