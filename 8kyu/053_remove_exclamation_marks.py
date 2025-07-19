# Remove exclamation marks

# ---
# ## CodeWars Description
# Write function RemoveExclamationMarks which removes all exclamation marks from a given string.

# ---
# ## Solution

def remove_exclamation_marks(s):
    strng = ''
    for char in s:
        if char == '!':
            strng += ''
        else:
            strng += char
    return strng
