# Capitalization and Mutability

# ---
# ## CodeWars Description
# Your coworker was supposed to write a simple helper function to capitalize a string (that contains a single word) before they went on vacation.
# Unfortunately, they have now left and the code they gave you doesn't work. Fix the helper function they wrote so that it works as intended (i.e. it must make the first character in the string upper case).
# The string will always start with a letter and will never be empty.
# Examples:
# "hello" --> "Hello"
# "Hello" --> "Hello" (the first letter was already capitalized)
# "a"     --> "A"

# ---
# ## Solution

def swap(st):
    # Initialize an empty string to build the result.
    strng = ''
    # Iterate through each character in the input string 'st'.
    for char in st:
        # Check if the character is one of the specified vowels.
        if char in ['a', 'e', 'i', 'o', 'u']:
            # If it's a vowel, capitalize it and append to the result string.
            char = char.capitalize()
            strng += char
        else:
            # If it's not a vowel, append it as is to the result string.
            strng += char
    # Return the modified string.
    return strng
