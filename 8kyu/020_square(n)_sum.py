# Square(n) Sum

# ---
# ## CodeWars Description
# Complete the square sum function so that it squares each number
# passed into it and then sums the results together.
# For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.

# ---
# ## Solution

def square_sum(numbers):
    # Calculate the square of each number in the input list.
    # Sum all the squared numbers.
    return sum(n**2 for n in numbers)
