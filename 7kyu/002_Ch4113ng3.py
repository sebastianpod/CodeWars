# Ch4113ng3

# ---
# ## Task Description
# Write a function that replaces specific letters in a given string with numbers:
# 'a' or 'A' should be replaced with '4'.
# 'e' or 'E' should be replaced with '3'.
# 'l' should be replaced with '1'.
# Other characters should remain unchanged.

# ---
# ## CodeWars Description
# Ch4113ng3
# Make your strings more nerdy: Replace all 'a'/'A' with 4, 'e'/'E' with 3 and 'l' with 1 e.g. "Fundamentals" --> "Fund4m3nt41s"

# ---
# ## Solution

def nerdify(txt):
    return ''.join('4' if i.upper() == 'A' else '3' if i.upper() == 'E' else '1' if i == 'l' else i for i in txt)
