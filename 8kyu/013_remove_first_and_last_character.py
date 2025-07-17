# Remove First and Last Character

# ---
# ## CodeWars Description
# Your goal is to create a function that removes the first and last characters of a string. You're given one parameter, the original string.
# Important: Your function should handle strings of any length ≥ 2 characters. For strings with exactly 2 characters, return an empty string.
# Examples
# removeChar('eloquent') // -> 'loquen'
# removeChar('country')  // -> 'ountr'
# removeChar('person')   // -> 'erso'
# removeChar('ab')       // -> '' (empty string)
# removeChar('xyz')      // -> 'y'

# ---
# ## Solution

def remove_char(s):
    return s[1:len(s)-1]
