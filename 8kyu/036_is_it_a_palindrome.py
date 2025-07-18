# Is it a palindrome?

# ---
# ## CodeWars Description
# Write a function that checks if a given string (case insensitive) is a palindrome.
# A palindrome is a word, number, phrase, or other sequence of symbols that reads the same backwards as forwards, such as madam or racecar

# ---
# ## Solution

def is_palindrome(s):
    s = s.upper()
    return True if s == s[::-1] else False
