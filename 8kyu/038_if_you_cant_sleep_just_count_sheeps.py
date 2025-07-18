# If you can't sleep, just count sheeps!!

# ---
# ## CodeWars Description
# Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.

# ---
# ## Solution

def count_sheep(n):
    result = ''
    for i in range(n):
        result += str(i+1) + ' sheep...'
    return result
