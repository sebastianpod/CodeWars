# add length

# ---
# ## CodeWars Description
# What if we need the length of the words separated by a space to be added at the end of that same word and have it returned as an array?
# Example(Input --> Output)
# "apple ban" --> ["apple 5", "ban 3"]
# "you will win" -->["you 3", "will 4", "win 3"]
# Your task is to write a function that takes a String and returns an Array/list with the length of each word added to each element .
# Note: String will have at least one element; words will always be separated by a space.

# ---
# ## Solution

def add_length(str_):
    # Split the input string into words.
    # For each word, create a new string combining the word and its length, separated by a space.
    # Return a list of these new strings.
    return [f'{i} {len(i)}' for i in str_.split()]
