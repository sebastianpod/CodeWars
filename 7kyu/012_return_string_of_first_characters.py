# Return String of First Characters

# ---
# ## CodeWars Description
# In this exercise, a string is passed to a method and a new string has to be returned with the first character of each word in the string.
# For example:
# "This Is A Test" ==> "TIAT"
# Strings will only contain letters and spaces, with exactly 1 space between words, and no leading/trailing spaces.

# ---
# ## Solution

def make_string(s):
    # Split the input string 's' into a list of words using space as a delimiter.
    # For each word 'i' in the resulting list, take its first character (i[0]).
    # Join all these first characters together to form a new string.
    return ''.join(i[0] for i in s.split())
