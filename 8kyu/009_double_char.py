# double char

# ---
# ## CodeWars Description
# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.
# Examples (Input -> Output):
# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "

# ---
# ## Solution

def double_char(s):
    # Iterate through each character in the input string 's'.
    # Repeat each character twice (i*2).
    # Join all the repeated characters to form the new string.
    return ''.join(i*2 for i in s)
