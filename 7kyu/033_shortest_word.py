# Shortest Word

# ---
# ## CodeWars Description
# Simple, given a string of words, return the length of the shortest word(s).
# String will never be empty and you do not need to account for different data types.

# ---
# ## Solution

def find_short(s):
    # Split the input string into a list of words.
    # For each word, calculate its length.
    # Find the minimum length among all words and return it.
    return min([len(i) for i in s.split()])
