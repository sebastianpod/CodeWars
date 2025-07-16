# Divide and Conquer

# ---
# ## CodeWars Description
# Given a mixed array of number and string representations of integers, add up the non-string integers and subtract the total of the string integers.
# Return as a number.

# ---
# ## Solution

def div_con(x):
    # Initialize a variable to store the running total.
    int_ = 0
    # Iterate through each element in the input list 'x'.
    for i in x:
        # Check if the current element 'i' is an integer type.
        if type(i) == int:
            # If it's an integer, add its value to the total.
            int_ += i
        else:
            # If it's not an integer (meaning it's a string representation of an integer),
            # convert it to an integer and subtract its value from the total.
            int_ -= int(i)
    # Return the final calculated total.
    return int_
