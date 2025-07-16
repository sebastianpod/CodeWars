# All unique

# ---
# ## CodeWars Description
# Write a program to determine if a string contains only unique characters. Return true if it does and false otherwise.
# The string may contain any of the 128 ASCII characters. Characters are case-sensitive, e.g. 'a' and 'A' are considered different characters.

# ---
# ## Solution

def has_unique_chars(string):
    # If the string is empty, return False as it cannot contain unique characters.
    if string == '':
        return False
    else:
        # Create a list of characters from the string, after removing spaces.
        x = [i for i in string.replace(' ','')]
        # Convert the list to a dictionary keys view. This automatically removes duplicate characters.
        x = dict.fromkeys(x)
        # Join the unique characters back into a string.
        # Compare this string of unique characters with the original string (without spaces).
        # If they are identical, all characters in the original string were unique.
        return True if ''.join(x) == string.replace(' ','') else False
