# volume of a cup

# ---
# ## CodeWars Description
# Your job is to return the volume of a cup when given the diameter of the top, the diameter of the bottom and the height.
# You know that there is a steady gradient from the top to the bottom.
# Inputs will be in range 1 <= dTop, dBotton, height <= 10_000.
# You do not need to do any rounding. Your answer will be checked with tolerance of 0.01.
# Examples
# cupVolume(1, 1, 1)          # 0.7853981633974483 +/- 0.01
# cupVolume(10, 8, 9)         # 574.9114556069321  +/- 0.01
# cupVolume(1000, 1000, 1000) # 785398163.3974483  +/- 0.01
# cupVolume(12, 123, 1)       # 4384.877946247953  +/- 0.01
# cupVolume(6, 12, 33)        # 2177.1237089377264 +/- 0.01

# ---
# ## Solution

from math import pi

def cup_volume(d1, d2, height):
    # Convert diameters to radii.
    r1 = d1 / 2
    r2 = d2 / 2
    
    # Calculate the volume using the formula for a frustum of a cone.
    # The formula is (1/3) * pi * (r1^2 + r1*r2 + r2^2) * height.
    # The if/else structure is present in the original code,
    # though the formula is symmetrical for r1 and r2.
    if r1 > r2:
        return round((1/3) * pi * (r1 ** 2 + r1 * r2 + r2 ** 2) * height, 2)
    else:
        return round((1/3) * pi * (r2 ** 2 + r2 * r1 + r1 ** 2) * height, 2)
