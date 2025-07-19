# Area of a Square

# ---
# ## CodeWars Description
# Complete the function that calculates the area of the red square, when the length of the circular arc A is given as the input. Return the result rounded to two decimals.
# Note: use the π value provided in your language (Math::PI, M_PI, math.pi, etc)

# ---
# ## Solution

import math

def square_area(a):
    return round((a / (math.pi / 2)) ** 2,2)
