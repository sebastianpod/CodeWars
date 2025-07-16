# Anagram Detection

# ---
# ## CodeWars Description
# An anagram is the result of rearranging the letters of a word to produce a new word (see wikipedia).
# Note: anagrams are case insensitive
# Complete the function to return true if the two arguments given are anagrams of each other; return false otherwise.
# Examples
# "foefet" is an anagram of "toffee"
# "Buckethead" is an anagram of "DeathCubeK"

# ---
# ## Solution

def is_anagram(test, original):
    # Convert both strings to lowercase to handle case-insensitivity.
    # Sort the characters of both strings.
    # If the sorted lists of characters are identical, the strings are anagrams.
    return sorted(test.lower()) == sorted(original.lower())
