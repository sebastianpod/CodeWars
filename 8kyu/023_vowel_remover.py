# vowel remover

# ---
# ## CodeWars Description
# Create a function called shortcut to remove the lowercase vowels (a, e, i, o, u ) in a given string.
# Examples
# "hello"     -->  "hll"
# "codewars"  -->  "cdwrs"
# "goodbye"   -->  "gdby"
# "HELLO"     -->  "HELLO"
# don't worry about uppercase vowels
# y is not considered a vowel for this kata

# ---
# ## Solution

def shortcut(s):
    strng = ''
    for char in s:
        if char in ['a', 'e', 'i', 'o', 'u']:
            pass
        else:
            strng += char
    return strng
