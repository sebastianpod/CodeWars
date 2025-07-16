# Unique_Sum

# ---
# ## CodeWars Description
# Given a list of integers values, your job is to return the sum of the values; however, if the same integer value appears multiple times in the list, you can only count it once in your sum.
# For example:
# [ 1, 2, 3] ==> 6
# [ 1, 3, 8, 1, 8] ==> 12
# [ -1, -1, 5, 2, -7] ==> -1
# [] ==> None

# ---
# ## Solution

def unique_sum(lst):
    # Check if the input list is empty.
    # If it is, return None as per the problem's example for an empty list.
    if not lst:
        return None
    
    # Convert the list to a set to automatically get only unique values.
    # Sets store only distinct elements.
    unique_values = set(lst)
    
    # Calculate the sum of all unique values in the set.
    return sum(unique_values)
