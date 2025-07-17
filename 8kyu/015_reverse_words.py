# reverse words

# ---
# ## CodeWars Description
# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.
# Examples
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"

# ---
# ## Solution

def reverse_words(s):
    lista = []
    empty = ' '
    txt = ''
    for i in s+empty:
        if i == ' ':
            txt += i
            lista.append(txt)
            txt = ''
        else:
            txt += i
    for i in lista[::-1]:
        txt += i
    return txt.rstrip()
