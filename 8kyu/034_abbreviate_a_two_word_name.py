# Abbreviate a Two Word Name

# ---
# ## CodeWars Description
# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
# The output should be two capital letters with a dot separating them.
# It should look like this:
# Sam Harris => S.H
# patrick feeney => P.F

# ---
# ## Solution

def abbrev_name(name):
    name = name.split()
    name = name[0][0].upper() + '.' + name[1][0].upper()
    return name
