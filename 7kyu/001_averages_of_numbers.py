# Averages of numbers

# ---
# ## CodeWars Description
# #Get the averages of these numbers
# Write a method, that gets an array of integer-numbers and return an array of the averages
# of each integer-number and his follower, if there is one.
# Example:
# Input:  [ 1, 3, 5, 1, -10]
# Output:  [ 2, 4, 3, -4.5]
# If the array has 0 or 1 values or is null, your method should return an empty array.
# Have fun coding it and please don't forget to vote and rank this kata! :-)

# ---
# ## Solution

def averages(arr):
    # Checks if the array is empty, has only one element, or is None.
    # In such cases, it returns an empty array as per the task requirements.
    if arr is None or len(arr) < 2:
        return []
    
    # Creates a list of averages. It iterates from the first element to the second-to-last,
    # to always have access to the current element (arr[i]) and its successor (arr[i+1]).
    # Calculates the average of the pair and adds it to the new list.
    return [(arr[i] + arr[i+1]) / 2 for i in range(len(arr) - 1)]
