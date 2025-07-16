# Ordered Count of Characters

# ---
# ## CodeWars Description
# Count the number of occurrences of each character and return it as a (list of tuples) in order of appearance. For empty output return (an empty list).
# Consult the solution set-up for the exact data structure implementation depending on your language.
# Example:
# orderedCount("abracadabra") == [['a', 5], ['b', 2], ['r', 2], ['c', 1], ['d', 1]]

# ---
# ## Solution

from collections import OrderedDict

def ordered_count(inp):
    # Use OrderedDict to store character counts while preserving the order of first appearance.
    # OrderedDict remembers the order in which items were inserted.
    char_counts = OrderedDict()
    
    # Iterate through each character in the input string.
    for char in inp:
        # If the character is already a key in char_counts, increment its count.
        # Otherwise, add the character as a new key with a count of 1.
        char_counts[char] = char_counts.get(char, 0) + 1
    
    # Convert the OrderedDict items to a list of lists (or tuples, as per problem example).
    # The example shows lists like [['a', 5]], so we convert to a list of lists.
    return [[char, count] for char, count in char_counts.items()]
