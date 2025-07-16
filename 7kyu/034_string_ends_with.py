# String ends with?

# ---
# ## CodeWars Description
# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).
# Examples:
# solution('abc', 'bc') // returns true
# solution('abc', 'd') // returns false

# ---
# ## Solution

def solution(text, ending):
    # Slice the 'text' string from the end, with a length equal to the 'ending' string's length.
    # Compare this sliced part with the 'ending' string.
    # If they are equal, it means 'text' ends with 'ending'.
    return text[-len(ending):] == ending
