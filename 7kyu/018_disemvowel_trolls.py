# disemvowel trolls

# ---
# ## CodeWars Description
# Trolls are attacking your comment section!
# A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
# Your task is to write a function that takes a string and return a new string with all vowels removed.
# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
# Note: for this kata y isn't considered a vowel.

# ---
# ## Solution

def disemvowel(string_):
    # Iterate through each character in the input string.
    # If a character is not a vowel (case-insensitive), include it in the new string.
    # Join the filtered characters to form the final string.
    return ''.join(i for i in string_ if i not in ['a', 'A', 'e', 'E', 'i', 'I', 'o' ,'O', 'u', 'U'])
