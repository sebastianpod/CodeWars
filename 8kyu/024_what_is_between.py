# what is between?

# ---
# ## CodeWars Description
# Complete the function that takes two integers (a, b, where a < b) and return an array of all integers between the input parameters, including them.
# For example:
# a = 1
# b = 4
# --> [1, 2, 3, 4]

# ---
# ## Solution

def between(a,b):
    c = []
    for char in range(a,b+1):
        c.append(char)
    return c
