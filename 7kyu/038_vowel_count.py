# Vowel Count

# ---
# ## CodeWars Description
# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
# The input string will only consist of lower case letters and/or spaces.

# ---
# ## Solution

def get_count(s):
    # Count occurrences of each vowel ('a', 'e', 'i', 'o', 'u') in the string.
    # Sum these individual counts to get the total number of vowels.
    return s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u')
