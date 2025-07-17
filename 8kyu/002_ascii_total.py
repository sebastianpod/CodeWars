# ASCII total

# ---
# ## CodeWars Description
# You'll be given a string, and have to return the sum of all characters as an int. The function should be able to handle all printable ASCII characters.
# Examples:
# uniTotal("a") == 97
# uniTotal("aaa") == 291

# ---
# ## Solution

def uni_total(s):
    # Iterate through each character in the input string 's'.
    # For each character, get its ASCII (Unicode) value using ord().
    # Sum all these ASCII values and return the total.
    return sum(ord(i) for i in s)
