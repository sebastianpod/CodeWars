# Triple Trouble

# ---
# ## CodeWars Description
# Create a function that will return a string that combines all of the letters of the three inputed strings in groups. Taking the first letter of all of the inputs and grouping them next to each other. Do this for every letter, see example below!
# E.g. Input: "aa", "bb" , "cc" => Output: "abcabc"
# Note: You can expect all of the inputs to be the same length.

# ---
# ## Solution

def triple_trouble(one, two, three):
    combined_str = ""
    for i in range(len(one)):
        combined_str += one[i] + two[i] + three[i]
    return combined_str
