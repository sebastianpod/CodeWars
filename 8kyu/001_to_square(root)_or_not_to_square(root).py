# To square(root) or not to square(root)

# ---
# ## CodeWars Description
# Write a method, that will get an integer array as parameter and will process every number from this array.
# Return a new array with processing every number of the input-array like this:
# If the number has an integer square root, take this, otherwise square the number.
# Example
# [4,3,9,7,2,1] -> [2,9,3,49,4,1]
# Notes
# The input array will always contain only positive numbers, and will never be empty or null.

# ---
# ## Solution

import math

def square_or_square_root(arr):
    # Initialize an empty list to store the processed numbers.
    result_list = [] # Renamed from 'list' to 'result_list' to avoid shadowing built-in 'list' and for clarity.
    
    # Iterate through each number in the input array.
    for i in arr:
        # Calculate the square root of the current number.
        sqrt_i = math.sqrt(i)
        # Check if the square root is an integer (i.e., has no fractional part).
        if sqrt_i % 1 == 0:
            # If it's an integer square root, append it to the result list.
            result_list.append(int(sqrt_i)) # Cast to int as per example output
        else:
            # If it's not an integer square root, square the original number and append it.
            result_list.append(i ** 2)
            
    # Return the new list with processed numbers.
    return result_list
